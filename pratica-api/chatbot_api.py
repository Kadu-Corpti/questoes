"""
Mini projeto: API de um chatbot BASEADO EM REGRAS (livro U4 + slides).

Segue a arquitetura em camadas do livro (Aula 1):
  1. Interface ............ as rotas HTTP (o site/app/WhatsApp chamam a API)
  2. Processamento (NLP) .. os padrões de regras do NLTK (Chat)
  3. Lógica de negócios ... consultar o "CRM" de pedidos, decidir escalonar
  4. Resposta ............. o JSON devolvido ao usuário

Também tem:
  - Escalonamento para humano quando o bot não entende (Aula 2)
  - Testes com unittest (Aula 3)
  - Token de acesso, anonimização, auditoria e exclusão de dados (Aula 4)
  - KPIs: Engajamento, Conclusão, CSAT e Transbordo (slide "Medindo o Sucesso")

Rodar:  python chatbot_api.py   (abre em http://127.0.0.1:5000)
"""
import hashlib
import re

from flask import Flask, jsonify, request
from nltk.chat.util import Chat

# ---------------------------------------------------------------
# CAMADA 2: PROCESSAMENTO. Regras (o mesmo exemplo do slide, com mais pares)
# ---------------------------------------------------------------
pares = [
    [r"oi|olá", ["Olá, como posso ajudar?"]],
    [r"tchau", ["Até mais!"]],
    [r"(.*)horário(.*)", ["Atendemos de segunda a sexta, das 8h às 18h."]],
    [r"(.*)devol(.*)", ["Você pode devolver o produto em até 7 dias."]],
]
chatbot = Chat(pares)

# Palavras que pedem atendente na hora (gatilho de escalonamento, Aula 2)
PALAVRAS_ESCALONAMENTO = ["atendente", "humano", "reclamação"]

# ---------------------------------------------------------------
# CAMADA 3: LÓGICA DE NEGÓCIOS. "CRM" simulado (na vida real, outra API)
# ---------------------------------------------------------------
CRM = {
    "1001": {"cliente": "Ana", "status": "Enviado"},
    "1002": {"cliente": "Bruno", "status": "Em separação"},
}

# Controle de acesso: só a gestão pode ver as métricas (Aula 4)
TOKEN_GESTAO = "segredo123"

dados = {}


def resetar():
    """Zera os contadores (usado nos testes)."""
    dados.update(
        visitantes=0,          # quantas pessoas entraram no site
        usuarios_chat=set(),   # quem usou o chat (anonimizado, sem repetir)
        interacoes=0,          # mensagens recebidas = tarefas iniciadas
        resolvidas=0,          # o bot respondeu sozinho = tarefas OK
        transferidas=0,        # foi para um humano (transbordo/escalonamento)
        notas=[],              # notas de 1 a 5 (CSAT)
        auditoria=[],          # registro de cada interação (Aula 4)
    )


def anonimizar(usuario):
    """Guarda um código no lugar do nome (anonimização, Aula 4)."""
    return hashlib.sha256(usuario.encode()).hexdigest()[:10]


def registrar(usuario_anon, texto, transferido):
    dados["auditoria"].append(
        {"usuario": usuario_anon, "texto": texto, "transferido": transferido}
    )


def escalonar(usuario_anon, texto):
    dados["transferidas"] += 1
    registrar(usuario_anon, texto, True)
    return jsonify({"resposta": "Vou te transferir para um atendente humano.",
                    "transferido": True}), 200


def responder(usuario_anon, texto, resposta):
    dados["resolvidas"] += 1
    registrar(usuario_anon, texto, False)
    return jsonify({"resposta": resposta, "transferido": False}), 200


resetar()
app = Flask(__name__)
app.json.ensure_ascii = False  # mostra "Olá" em vez de "Olá"


# ---------------------------------------------------------------
# CAMADA 1: INTERFACE. As rotas (endpoints) da API
# ---------------------------------------------------------------
@app.get("/status")
def status():
    return jsonify({"status": "online"}), 200


@app.post("/visita")
def registrar_visita():
    dados["visitantes"] += 1
    return jsonify({"visitantes": dados["visitantes"]}), 201


@app.post("/mensagem")
def mensagem():
    corpo = request.get_json(silent=True) or {}
    texto = corpo.get("texto", "").strip()
    usuario = anonimizar(corpo.get("usuario", "anonimo"))

    if not texto:
        return jsonify({"erro": "Campo 'texto' é obrigatório"}), 400

    dados["usuarios_chat"].add(usuario)
    dados["interacoes"] += 1
    minusculo = texto.lower()

    # 1) Pediu humano explicitamente? Escala na hora.
    if any(p in minusculo for p in PALAVRAS_ESCALONAMENTO):
        return escalonar(usuario, texto)

    # 2) Falou de pedido? Lógica de negócios: consulta o CRM (integração via API)
    achou = re.search(r"pedido (\d+)", minusculo)
    if achou:
        pedido = CRM.get(achou.group(1))
        if pedido:
            return responder(usuario, texto, f"Seu pedido está: {pedido['status']}")

    # 3) Regras do NLTK
    resposta = chatbot.respond(texto)
    if resposta is None:  # nenhuma regra casou: limitação do bot de regras
        return escalonar(usuario, texto)

    # CAMADA 4: RESPOSTA
    return responder(usuario, texto, resposta)


@app.get("/pedidos/<numero>")
def consultar_pedido(numero):
    pedido = CRM.get(numero)
    if pedido is None:
        return jsonify({"erro": "Pedido não encontrado"}), 404
    return jsonify(pedido), 200


@app.post("/avaliacao")
def avaliacao():
    corpo = request.get_json(silent=True) or {}
    nota = corpo.get("nota")
    if not isinstance(nota, int) or not 1 <= nota <= 5:
        return jsonify({"erro": "A nota deve ser um número de 1 a 5"}), 400
    dados["notas"].append(nota)
    return jsonify({"mensagem": "Obrigado pela avaliação!"}), 201


@app.delete("/usuarios/<usuario>")
def excluir_dados(usuario):
    """Direito do usuário de excluir seus dados (privacidade/LGPD, Aula 4)."""
    anon = anonimizar(usuario)
    dados["auditoria"] = [r for r in dados["auditoria"] if r["usuario"] != anon]
    return "", 204


def porcentagem(parte, total):
    return round(parte / total * 100, 1) if total else 0.0


@app.get("/kpis")
def kpis():
    if request.headers.get("Authorization") != f"Bearer {TOKEN_GESTAO}":
        return jsonify({"erro": "Não autorizado"}), 401

    notas = dados["notas"]
    return jsonify({
        # (Usuários Chat / Total Visitantes) * 100
        "engajamento": porcentagem(len(dados["usuarios_chat"]), dados["visitantes"]),
        # (Tarefas OK / Tarefas Iniciadas) * 100
        "conclusao": porcentagem(dados["resolvidas"], dados["interacoes"]),
        # Média das notas pós-atendimento
        "csat": round(sum(notas) / len(notas), 1) if notas else 0.0,
        # (Transf. Humano / Total Interações) * 100
        "transbordo": porcentagem(dados["transferidas"], dados["interacoes"]),
    }), 200


if __name__ == "__main__":
    app.run(debug=True)
