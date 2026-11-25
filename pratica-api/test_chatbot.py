"""Testes da Aula 3 (etapa 3: Teste — Unittest).  Rodar: python -m unittest -v"""
import unittest

from chatbot_api import app, dados, resetar

TOKEN = {"Authorization": "Bearer segredo123"}


class TestChatbotAPI(unittest.TestCase):
    def setUp(self):
        resetar()                       # cada teste começa do zero
        self.cliente = app.test_client()  # "navegador" de mentira, sem subir servidor

    def test_status_online(self):
        r = self.cliente.get("/status")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.get_json(), {"status": "online"})

    def test_saudacao(self):
        r = self.cliente.post("/mensagem", json={"texto": "oi"})
        self.assertEqual(r.get_json()["resposta"], "Olá, como posso ajudar?")

    def test_despedida(self):
        r = self.cliente.post("/mensagem", json={"texto": "tchau"})
        self.assertEqual(r.get_json()["resposta"], "Até mais!")

    def test_mensagem_sem_texto_da_400(self):
        r = self.cliente.post("/mensagem", json={})
        self.assertEqual(r.status_code, 400)

    def test_nao_entendeu_transfere_para_humano(self):
        r = self.cliente.post("/mensagem", json={"texto": "quero cancelar meu cartão"})
        self.assertTrue(r.get_json()["transferido"])

    def test_consulta_pedido_no_crm(self):
        r = self.cliente.post("/mensagem", json={"texto": "Cadê meu pedido 1001?"})
        self.assertEqual(r.get_json()["resposta"], "Seu pedido está: Enviado")

    def test_pedido_inexistente_da_404(self):
        self.assertEqual(self.cliente.get("/pedidos/9999").status_code, 404)

    def test_avaliacao_invalida_da_400(self):
        r = self.cliente.post("/avaliacao", json={"nota": 7})
        self.assertEqual(r.status_code, 400)

    def test_kpis_sem_token_da_401(self):
        self.assertEqual(self.cliente.get("/kpis").status_code, 401)

    def test_pedir_atendente_escala_na_hora(self):
        r = self.cliente.post("/mensagem", json={"texto": "quero falar com um atendente"})
        self.assertTrue(r.get_json()["transferido"])

    def test_auditoria_guarda_usuario_anonimizado(self):
        self.cliente.post("/mensagem", json={"texto": "oi", "usuario": "kadu"})
        self.assertNotEqual(dados["auditoria"][0]["usuario"], "kadu")

    def test_excluir_dados_do_usuario(self):
        self.cliente.post("/mensagem", json={"texto": "oi", "usuario": "kadu"})
        r = self.cliente.delete("/usuarios/kadu")
        self.assertEqual(r.status_code, 204)
        self.assertEqual(dados["auditoria"], [])

    def test_metodo_errado_da_405(self):
        self.assertEqual(self.cliente.delete("/status").status_code, 405)

    def test_calculo_dos_kpis(self):
        for _ in range(10):
            self.cliente.post("/visita")
        self.cliente.post("/mensagem", json={"texto": "oi", "usuario": "ana"})
        self.cliente.post("/mensagem", json={"texto": "tchau", "usuario": "ana"})
        self.cliente.post("/mensagem", json={"texto": "oi", "usuario": "bia"})
        self.cliente.post("/mensagem", json={"texto": "reembolso", "usuario": "bia"})
        self.cliente.post("/avaliacao", json={"nota": 5})
        self.cliente.post("/avaliacao", json={"nota": 4})

        k = self.cliente.get("/kpis", headers=TOKEN).get_json()
        self.assertEqual(k["engajamento"], 20.0)  # 2 usuários / 10 visitantes
        self.assertEqual(k["conclusao"], 75.0)    # 3 resolvidas / 4 interações
        self.assertEqual(k["transbordo"], 25.0)   # 1 transferida / 4 interações
        self.assertEqual(k["csat"], 4.5)          # (5 + 4) / 2


if __name__ == "__main__":
    unittest.main()
