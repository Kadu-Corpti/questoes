# Mini projeto: API de Chatbot (Aulas 3, 4 e 5)

Uma API em **Flask** para um chatbot **baseado em regras** com NLTK, usando o mesmo exemplo do slide da Aula 3.
O código segue o livro da Unidade 4:

| Conceito do livro | Onde está no código |
|---|---|
| Camada de **interface** (Aula 1) | as rotas `@app.get` / `@app.post` / `@app.delete` |
| Camada de **processamento/NLP** (Aula 1) | `pares` + `Chat(pares)` |
| Camada de **lógica de negócios** (Aula 1) | consulta ao `CRM` e decisão de escalonar |
| Camada de **resposta** (Aula 1) | o `jsonify(...)` devolvido |
| **Escalonamento para humano** (Aula 2) | `escalonar()`: quando pede "atendente" ou nenhuma regra casa |
| **Testes** (Aula 3) | `test_chatbot.py` com `unittest` |
| **Controle de acesso** (Aula 4) | token `Bearer` na rota `/kpis` |
| **Anonimização e auditoria** (Aula 4) | `anonimizar()` e `dados["auditoria"]` |
| **Direito de excluir dados** (Aula 4) | `DELETE /usuarios/<usuario>` |
| **KPIs** (slide "Medindo o Sucesso") | rota `/kpis` |

## Como rodar

```bash
pip install -r requirements.txt
```

```bash
python chatbot_api.py
```

A API fica em `http://127.0.0.1:5000`.

## Rodar os testes (Aula 3, etapa "Teste" com Unittest)

```bash
python -m unittest -v
```

Os testes usam `app.test_client()`, então não precisa deixar o servidor ligado.

## Endpoints

| Método | Rota | O que faz | Respostas possíveis |
|---|---|---|---|
| GET | `/status` | Diz se a API está no ar | 200 |
| POST | `/visita` | Conta 1 visitante do site | 201 |
| POST | `/mensagem` | Envia `{"texto": "...", "usuario": "..."}` e recebe a resposta do bot | 200, 400 (sem texto) |
| GET | `/pedidos/<numero>` | Consulta um pedido no CRM | 200, 404 |
| POST | `/avaliacao` | Envia `{"nota": 1 a 5}` (CSAT) | 201, 400 (nota inválida) |
| DELETE | `/usuarios/<usuario>` | Apaga os registros do usuário (privacidade) | 204 |
| GET | `/kpis` | Engajamento, Conclusão, CSAT e Transbordo. Exige `Authorization: Bearer segredo123` | 200, 401 |

Usar um método que a rota não aceita (ex.: `DELETE /status`) devolve **405**.

## Testando com curl (com o servidor ligado)

```bash
curl http://127.0.0.1:5000/status
```

```bash
curl -X POST http://127.0.0.1:5000/visita
```

```bash
curl -X POST http://127.0.0.1:5000/mensagem -H "Content-Type: application/json" -d '{"texto": "oi", "usuario": "kadu"}'
```

```bash
curl -X POST http://127.0.0.1:5000/mensagem -H "Content-Type: application/json" -d '{"texto": "cadê meu pedido 1001?", "usuario": "kadu"}'
```

```bash
curl -X POST http://127.0.0.1:5000/mensagem -H "Content-Type: application/json" -d '{"texto": "quero cancelar", "usuario": "kadu"}'
```

```bash
curl -X POST http://127.0.0.1:5000/avaliacao -H "Content-Type: application/json" -d '{"nota": 5}'
```

```bash
curl http://127.0.0.1:5000/kpis -H "Authorization: Bearer segredo123"
```

```bash
curl -i -X DELETE http://127.0.0.1:5000/usuarios/kadu
```

## Desafios para treinar

1. Adicione um par novo em `pares` para responder "obrigado". Depois escreva o teste.
2. Hoje `"oito"` recebe "Olá, como posso ajudar?". Por quê? Corrija o padrão para `r"(oi|olá)\b"`.
3. Crie `DELETE /pedidos/<numero>` que remove o pedido do CRM e devolve 204.
4. Na resposta de `/kpis`, adicione o total de interações.
5. Crie a rota `GET /auditoria`, protegida pelo mesmo token de `/kpis`.
