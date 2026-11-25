# Resumo para a prova: Chatbot, API e KPIs

## Siglas

| Sigla | Significado | Em uma linha |
|---|---|---|
| **API** | Application Programming Interface (Interface de Programação de Aplicações) | Regras e protocolos para sistemas trocarem dados de forma padronizada e segura |
| **NLP / PLN** | Natural Language Processing / Processamento de Linguagem Natural | Faz o bot entender a linguagem humana (intenção e entidades) |
| **NLTK** | Natural Language Toolkit | Biblioteca Python de NLP (`Chat` de regras do slide) |
| **NER** | Named Entity Recognition | Reconhecer entidades no texto (`doc.ents` do spaCy) |
| **LOC / GPE** | Location / Geo-Political Entity | Rótulos de "lugar" no NER do spaCy |
| **IA / ML** | Inteligência Artificial / Machine Learning | O que o bot híbrido usa para aprender |
| **CRM** | Customer Relationship Management | Sistema com dados e pedidos dos clientes |
| **HTTP / HTTPS** | HyperText Transfer Protocol (S = Secure) | Protocolo das APIs web; HTTPS = com criptografia |
| **TLS** | Transport Layer Security | Criptografa os dados **em trânsito** |
| **MFA** | Multi-Factor Authentication | Senha + outro fator (código no celular) |
| **PCI-DSS** | Payment Card Industry Data Security Standard | Norma de segurança para dados de cartão |
| **LGPD / GDPR** | Lei Geral de Proteção de Dados / General Data Protection Regulation (Europa) | Leis de privacidade |
| **JSON** | JavaScript Object Notation | Formato texto chave-valor que as APIs trocam |
| **URL** | Uniform Resource Locator | Endereço da API (`https://.../geoname?name=Paris`) |
| **CI/CD** | Continuous Integration / Continuous Delivery (Deployment) | Testa e publica automaticamente a cada mudança |
| **PDCA** | Plan, Do, Check, Act | Planejar, Executar, Verificar, Agir: ciclo de melhoria contínua |
| **KPI** | Key Performance Indicator | Indicador-chave de desempenho |
| **CSAT** | Customer Satisfaction | Média das notas pós-atendimento |
| **SMART** | Specific, Measurable, Achievable, Relevant, Time-bound | Meta específica, mensurável, alcançável, relevante e com prazo |
| **FAQ** | Frequently Asked Questions | Perguntas frequentes, o que o bot de regras automatiza |
| **regex** | Regular Expression | Padrão de texto (`r"oi\|olá"`, `\d{4,}`) |

## Teoria (livro da Unidade 4)

**Aula 1: Conceitos e arquitetura**
- **Bot de regras:** padrões feitos à mão, previsível, bom para tarefas simples e limitado ao que foi programado.
- **Bot híbrido:** regras + NLP/ML; entende perguntas complexas e melhora com o tempo.
- **Intenção** = o que o usuário quer (consultar pedido). **Entidade** = o dado específico (nº do pedido). **Resposta** = o resultado.
- **Camadas:** Interface → NLP → Lógica de negócios (o "cérebro": consulta o banco ou a API) → Resposta.
- **API no chatbot:** dados **em tempo real** (estoque, pedidos, clima). Um banco consulta saldo **por meio de uma API segura**.

**Aula 2: Funcionalidades** (analogia do restaurante)
- **Automação** (o tablet faz o pedido) · **Personalização/contextualização** (o chef lembra suas preferências) · **Escalonamento** (o garçom assume).
- **Gatilhos de escalonamento:** palavras-chave, feedback negativo ou repetitivo, ou o bot sem resposta clara.
- Passar ao humano os dados já coletados, para o cliente **não repetir**.

**Aula 3: Implementação** (analogia da casa)
- **Planejamento:** O que resolver? Quem são os usuários? Quais problemas? **Design:** tom, estilo e como o bot reage.
- **Ferramentas de desenvolvimento (NLP):** Dialogflow, Rasa, Microsoft Bot Framework. **Monitoramento:** Botpress, Chatbot Analytics. **Fluxos de regras:** ManyChat, Chatfuel.
- **Testes:** de **funcionalidade** (FAQ, navegação, pedido) e de **NLP** (gírias, erros de digitação, ambiguidade). **Validação:** com usuários reais + PDCA.
- **Fluxo do slide:** Planejamento → Desenvolvimento (NLTK, spaCy) → Teste (Unittest) → Implantação (CI/CD) → Monitoramento.

**Aula 4: Limitações, desafios e segurança** (analogia do parque)
- **Limitações:** linguagem ambígua; integração **incompatível** com CRM e APIs; **tempo de resposta** (as "filas do parque").
- **Desafios:** treinar as intenções, atualizar sempre, **escalabilidade** (picos de uso), **múltiplos canais**.
- **Segurança:** sequestro de sessão → **criptografia**; controle de acesso → **MFA**.
- **Privacidade:** deixar o usuário **excluir ou corrigir** seus dados; **anonimizar**.
- **Bot de banco:** APIs seguras + PCI-DSS + TLS (em trânsito) + criptografia dos dados armazenados + MFA + monitoramento + **auditoria** + testes de **intrusão** (vulnerabilidades) e de **carga** (alta demanda) + escalonar para humano.

**KPIs (slide)**
- Engajamento = Usuários do chat ÷ Visitantes × 100
- Conclusão = Tarefas OK ÷ Tarefas iniciadas × 100
- CSAT = média das notas
- Transbordo = Transferidos para humano ÷ Total de interações × 100 (**quanto menor, melhor**)

## Códigos: o que cai

**HTTP**
- **Métodos:** GET consulta · POST envia ou cria · PUT/PATCH atualiza · DELETE remove.
- **Status:** 200 OK · 201 Created · 204 No Content · 400 erro do cliente · 401 sem autorização · 404 não existe · 405 método errado · 500 erro do servidor.

**Slide (NLTK `Chat`)**
- `pares = [[regex, [respostas]], ...]` → bot de **regras**. `|` = **OU**.
- Casa a partir do **início** da frase e ignora maiúsculas: "Oi, tudo bem?" casa; "bom dia, oi" devolve `None`; **"oito" casa com "oi"** (pegadinha).
- `respond(texto)` **devolve** a resposta (serve para API). `converse()` é um loop no terminal até digitar "quit".

**Exercício 1: Chatbot turístico (OpenTripMap)**
- **Fluxo:** NLP acha a cidade → `GET /geoname` (cidade → lat/lon) → `GET /radius` (lat/lon → lugares) → imprime os nomes.
- `getpass()`: a chave **não fica no código** nem aparece na tela.
- `requests.get(url, params=..., timeout=20)`:
  - `params` monta `?name=Paris&apikey=...`
  - `timeout` evita travar se a API não responder.
- `raise_for_status()` lança exceção em 4xx/5xx (ex.: chave errada) → cai no `except RequestException`.
- `.json()` converte o texto JSON em `dict` ou `list`. `.get("chave")` não quebra se a chave faltar.
- Os `except` vão do **específico** (`RequestException`) para o **genérico** (`Exception`).
- **Cidade:**
  - O spaCy acha a entidade em `doc.ents` (LOC). A regex `em|no|na ...` **sobrescreve** o spaCy.
  - "Museus em Paris no inverno?" → "Paris no inverno" (pegadinha).
- **Categoria:** percorre o dicionário em ordem e o `break` para no primeiro; "igrejas e templos" → `architecture`. Sem categoria → não filtra.
- `radius: 10000` = **10 km**, `limit: 20`. O filtro de categoria é feito **depois** e pode zerar a lista; melhor mandar `kinds` para a API.

**Exercício 2: Intenção, entidade e sentimento**
- `tokenizar` = `lower().split()` → a pontuação fica grudada: `['oi,', 'tudo', 'bem?']`.
- Os `if/elif` são testados **em ordem**: "Quanto custa a **entrega**?" vira `consultar_pedido`.
- `"oi" in texto` acha "oi" **dentro** de palavras: "d**oi**s" e "n**oi**te" viram saudação.
- `\b\d{4,}\b` = 4 ou mais dígitos: "pedido 123" → pede o número.
- **Faixas (`<=`):** ≤1000 atrasado · 1001–10000 perdido e reembolsado · >10000 entregue.
- **Intenção** = `identificar_intencao()`. **Entidade** = `extrair_numero_pedido()`.
- `sentimento` é **calculado e nunca usado**. Melhoria: se for negativo, **escalonar para humano**.
- O negativo é testado primeiro: "frustrado, mas obrigado" → negativo.
- É tudo **baseado em regras**. Intenção desconhecida → melhoria: escalonar para humano.
