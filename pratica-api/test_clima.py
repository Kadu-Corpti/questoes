"""Testes do chatbot do clima.  Rodar: python -m unittest test_clima -v

Usamos unittest.mock para FINGIR a API. Assim o teste:
  - não precisa de internet
  - sempre recebe a mesma resposta (resultado previsível)
"""
import unittest
from unittest.mock import MagicMock, patch

import chatbot_clima as bot


def resposta_falsa(json_dict):
    """Cria um objeto que se comporta como a resposta do requests."""
    falsa = MagicMock()
    falsa.json.return_value = json_dict
    falsa.raise_for_status.return_value = None
    return falsa


class TestRegras(unittest.TestCase):
    def test_tokenizar_tira_pontuacao(self):
        self.assertEqual(bot.tokenizar("Oi, tudo bem?"), ["oi", "tudo", "bem"])

    def test_dois_nao_e_saudacao(self):
        self.assertEqual(bot.identificar_intencao("Quero dois guarda-chuvas"), "desconhecida")

    def test_intencao_clima(self):
        self.assertEqual(bot.identificar_intencao("Vai chover amanhã?"), "consultar_clima")

    def test_extrair_cidade_composta(self):
        self.assertEqual(bot.extrair_cidade("Vai chover no Rio de Janeiro?"), "Rio de Janeiro")

    def test_extrair_cidade_sem_pegar_o_resto(self):
        self.assertEqual(bot.extrair_cidade("tempo em Paris no inverno"), "Paris")

    def test_extrair_cidade_minuscula(self):
        self.assertEqual(bot.extrair_cidade("tempo em curitiba"), "curitiba")

    def test_sentimento_negativo_escala(self):
        self.assertIn("atendente humano", bot.gerar_resposta("esse bot é péssimo"))


class TestAPI(unittest.TestCase):
    @patch("chatbot_clima.requests.get")
    def test_consulta_completa(self, get_falso):
        # 1ª chamada (geocoding) e 2ª chamada (clima), nessa ordem
        get_falso.side_effect = [
            resposta_falsa({"results": [{"name": "Recife", "country": "Brasil",
                                         "latitude": -8.05, "longitude": -34.9}]}),
            resposta_falsa({"current": {"temperature_2m": 31.0, "precipitation": 0.0,
                                        "wind_speed_10m": 12.0}}),
        ]
        texto = bot.gerar_resposta("Como está o tempo em Recife?")
        self.assertIn("Recife (Brasil): 31.0 °C", texto)
        self.assertIn("bem quente", texto)
        self.assertEqual(get_falso.call_count, 2)  # chamou a API duas vezes

    @patch("chatbot_clima.requests.get")
    def test_cidade_inexistente(self, get_falso):
        get_falso.return_value = resposta_falsa({"generationtime_ms": 0.1})  # sem "results"
        self.assertEqual(bot.gerar_resposta("tempo em Xyzabc"), "Não encontrei a cidade 'Xyzabc'.")


if __name__ == "__main__":
    unittest.main()
