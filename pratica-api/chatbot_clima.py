"""
=====================================================================
 CHATBOT DO CLIMA: exemplo de chatbot que USA UMA API
=====================================================================
É a mesma ideia dos exercícios do professor, só que menor:

  Exercício 1 (turístico)  ->  cidade -> coordenadas -> dados da API
  Exercício 2 (pedidos)    ->  intenção, entidade e sentimento por regras

API usada: Open-Meteo (https://open-meteo.com). É gratuita e NÃO precisa
de chave, então dá para rodar direto.

Camadas do livro (Aula 1), e onde cada uma está no código:
  1. INTERFACE ........... conversar()           (input / print)
  2. NLP (regras) ........ identificar_intencao(), extrair_cidade(),
                           analisar_sentimento()
  3. LÓGICA DE NEGÓCIOS .. gerar_resposta() + buscar_coordenadas()
                           + buscar_clima()     (é aqui que a API é chamada)
  4. RESPOSTA ............ o texto que gerar_resposta() devolve

Rodar:
    pip install requests
    python chatbot_clima.py

Exemplos de pergunta:
    Oi
    Como está o tempo em São Paulo?
    Vai chover no Rio de Janeiro?
    Qual a temperatura em Xyzabc?        (cidade que não existe)
    Esse bot é péssimo                   (sentimento negativo -> humano)
"""
import re

import requests

# Endereços (URLs) das duas rotas da API que vamos usar
URL_GEOCODING = "https://geocoding-api.open-meteo.com/v1/search"  # nome -> coordenadas
URL_CLIMA = "https://api.open-meteo.com/v1/forecast"              # coordenadas -> clima


# ---------------------------------------------------------------------
# CAMADA 2: NLP BASEADO EM REGRAS
# ---------------------------------------------------------------------

def tokenizar(texto):
    """Quebra o texto em palavras, já SEM pontuação.

    No exercício 2, o split() deixava 'oi,' e 'bem?' com pontuação.
    Aqui o re.findall(r"\\w+") pega só letras e números:
        "Oi, tudo bem?"  ->  ['oi', 'tudo', 'bem']
    """
    return re.findall(r"\w+", texto.lower())


def identificar_intencao(texto):
    """INTENÇÃO = o que o usuário quer fazer.

    Comparamos com os TOKENS (palavras inteiras), não com o texto todo.
    Assim 'dois' e 'noite' NÃO viram saudação (pegadinha do exercício 2).
    A ordem dos if importa: o primeiro que combinar vence.
    """
    palavras = tokenizar(texto)

    if any(p in palavras for p in ["atendente", "humano"]):
        return "falar_com_humano"
    if any(p in palavras for p in ["tempo", "clima", "temperatura", "chover", "chuva"]):
        return "consultar_clima"
    if any(p in palavras for p in ["oi", "olá", "ola"]):
        return "saudacao"
    return "desconhecida"


def extrair_cidade(texto):
    """ENTIDADE = a informação específica que completa a intenção (a cidade).

    1ª tentativa: palavras com letra MAIÚSCULA depois de em/no/na.
        "tempo em São Paulo amanhã?"        -> "São Paulo"
        "Vai chover no Rio de Janeiro?"     -> "Rio de Janeiro"
        "tempo em Paris no inverno"         -> "Paris"
        (no exercício 1 dava "Paris no inverno")
    2ª tentativa: se escreveu tudo minúsculo, pega só a palavra seguinte.
        "tempo em curitiba"  -> "curitiba"
    """
    maiusculas = re.search(
        r"\b(?:em|no|na)\s+([A-ZÀ-Ú]\w*(?:\s+(?:d[aeo]s?\s+)?[A-ZÀ-Ú]\w*)*)",
        texto,
    )
    if maiusculas:
        return maiusculas.group(1)

    qualquer = re.search(r"\b(?:em|no|na)\s+(\w+)", texto, re.IGNORECASE)
    if qualquer:
        return qualquer.group(1)

    return None


def analisar_sentimento(texto):
    """Sentimento por lista de palavras (regras, como no exercício 2)."""
    palavras = tokenizar(texto)
    negativas = ["ruim", "péssimo", "pessimo", "horrível", "frustrado", "irritado", "inútil"]
    positivas = ["ótimo", "otimo", "obrigado", "obrigada", "excelente", "valeu"]

    if any(p in palavras for p in negativas):
        return "negativo"
    if any(p in palavras for p in positivas):
        return "positivo"
    return "neutro"


# ---------------------------------------------------------------------
# CAMADA 3: LÓGICA DE NEGÓCIOS (integração com a API)
# ---------------------------------------------------------------------

def buscar_coordenadas(cidade):
    """1ª CHAMADA À API: GET /v1/search  (nome da cidade -> latitude/longitude)

    É o mesmo papel do /geoname do exercício 1.
    """
    resposta = requests.get(
        URL_GEOCODING,
        params={"name": cidade, "count": 1, "language": "pt"},  # vira ?name=...&count=1&language=pt
        timeout=10,                 # se a API não responder em 10 s, desiste (não trava)
    )
    resposta.raise_for_status()     # erro HTTP 4xx/5xx -> lança exceção
    dados = resposta.json()         # texto JSON -> dicionário Python

    # Quando a cidade não existe, a API NÃO manda a chave "results".
    # Por isso usamos .get(): devolve None em vez de dar KeyError.
    resultados = dados.get("results")
    if not resultados:
        return None

    return resultados[0]  # ex.: {"name": "São Paulo", "latitude": -23.5, "longitude": -46.6, "country": "Brasil", ...}


def buscar_clima(latitude, longitude):
    """2ª CHAMADA À API: GET /v1/forecast  (coordenadas -> clima atual)

    É o mesmo papel do /radius do exercício 1: só funciona com lat/lon,
    por isso precisa da 1ª chamada antes (encadeamento de APIs).
    """
    resposta = requests.get(
        URL_CLIMA,
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,precipitation,wind_speed_10m",  # o que queremos
            "timezone": "auto",
        },
        timeout=10,
    )
    resposta.raise_for_status()
    return resposta.json()["current"]  # ex.: {"temperature_2m": 25.7, "precipitation": 0.0, ...}


def dica(temperatura, chuva):
    """Faixas de valores, como as faixas de pedido do exercício 2."""
    if chuva > 0:
        return "Leve guarda-chuva!"
    if temperatura >= 30:
        return "Está bem quente, beba água."
    if temperatura <= 15:
        return "Está frio, leve um casaco."
    return "Clima agradável."


def gerar_resposta(texto):
    intencao = identificar_intencao(texto)
    sentimento = analisar_sentimento(texto)

    # ESCALONAMENTO PARA HUMANO (livro, Aula 2). Gatilhos:
    #   - palavra-chave (pediu atendente)
    #   - feedback negativo do usuário
    #   - o bot não tem uma resposta clara (intenção desconhecida)
    # Aqui o sentimento É USADO (no exercício 2 ele era calculado e ignorado).
    if intencao == "falar_com_humano" or sentimento == "negativo":
        return "Sinto muito! Vou te transferir para um atendente humano."
    if intencao == "desconhecida":
        return ("Não entendi. Pergunte, por exemplo: 'Como está o tempo em Recife?'. "
                "Se preferir, digite 'atendente'.")

    if intencao == "saudacao":
        return "Olá! Pergunte sobre o clima de alguma cidade."

    # intenção == "consultar_clima"
    cidade = extrair_cidade(texto)
    if not cidade:
        return "De qual cidade você quer saber o clima? Ex.: 'tempo em Salvador'."

    local = buscar_coordenadas(cidade)
    if local is None:
        return f"Não encontrei a cidade '{cidade}'."

    clima = buscar_clima(local["latitude"], local["longitude"])
    temperatura = clima["temperature_2m"]
    chuva = clima["precipitation"]

    # CAMADA 4: RESPOSTA
    return (f"{local['name']} ({local.get('country', '?')}): {temperatura} °C, "
            f"chuva {chuva} mm, vento {clima['wind_speed_10m']} km/h. "
            f"{dica(temperatura, chuva)}")


# ---------------------------------------------------------------------
# CAMADA 1: INTERFACE
# ---------------------------------------------------------------------

def conversar():
    print("=== CHATBOT DO CLIMA ===  (digite 'sair' para encerrar)")

    while True:
        mensagem = input("\nVocê: ").strip()   # strip(): "sair " também encerra

        if mensagem.lower() == "sair":
            print("Bot: Até mais!")
            break

        # Os except vão do MAIS ESPECÍFICO para o MAIS GENÉRICO.
        # Timeout é um tipo de RequestException, então precisa vir antes.
        try:
            print("Bot:", gerar_resposta(mensagem))
        except requests.exceptions.Timeout:
            print("Bot: A API do clima demorou demais. Tente de novo.")
        except requests.exceptions.RequestException as erro:
            print("Bot: Erro ao consultar a API:", erro)
        except Exception as erro:
            print("Bot: Ocorreu um erro inesperado:", erro)


# Só roda o chat quando o arquivo é executado direto.
# Se outro arquivo fizer "import chatbot_clima" (ex.: os testes), não abre o input().
if __name__ == "__main__":
    conversar()
