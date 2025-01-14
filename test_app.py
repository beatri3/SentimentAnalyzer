import unittest
import os
from unittest.mock import patch
from sentiment_analyzer import analisar_sentimento
from file_handler import ler_comentarios, guardar_classificacao
from visualizer import gerar_grafico
from main import analisar_comentarios
import config

class TestApp(unittest.TestCase):

    def setUp(self):
        """Configuração inicial para os testes."""
        self.input_dir = config.INPUT_DIR
        self.output_dir = config.OUTPUT_DIR
        os.makedirs(self.output_dir, exist_ok=True)

        # Criar um ficheiro de exemplo para os testes
        self.sample_file = os.path.join(self.input_dir, "test_comments.txt")
        with open(self.sample_file, "w", encoding="utf-8") as f:
            f.write("This product is excellent!\n")
            f.write("Horrible, I will never buy it again.\n")
            f.write("The product is available in stores.\n")

    def tearDown(self):
        """Limpar os ficheiros criados durante os testes."""
        if os.path.exists(self.sample_file):
            os.remove(self.sample_file)
        for file in os.listdir(self.output_dir):
            os.remove(os.path.join(self.output_dir, file))

    # Teste da função 'analisar_sentimento'
    def test_analisar_sentimento(self):
        self.assertEqual(analisar_sentimento("This product is excellent!"), "Positivo")
        self.assertEqual(analisar_sentimento("Horrible, I will never buy it again."), "Negativo")
        self.assertEqual(analisar_sentimento("The product is available in stores."), "Neutro")

    # Teste da função 'ler_comentarios'
    def test_ler_comentarios(self):
        comentarios = ler_comentarios(self.sample_file)
        self.assertEqual(len(comentarios), 3)
        self.assertEqual(comentarios[0].strip(), "This product is excellent!")
        self.assertEqual(comentarios[1].strip(), "Horrible, I will never buy it again.")

    # Teste da função 'guardar_classificacao'
    def test_salvar_classificacao(self):
        positives = ["This product is excellent!"]
        negatives = ["Horrible, I will never buy it again."]
        neutrals = ["The product is available in stores."]

        guardar_classificacao("test", positives, negatives, neutrals)

        # Verificar se o ficheiro CSV foi criado
        output_file = os.path.join(self.output_dir, "test-classificacao.csv")
        self.assertTrue(os.path.exists(output_file))

        # Verificar o conteúdo do ficheiro
        with open(output_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
        self.assertIn("Negativos,\"Horrible, I will never buy it again.\"\n", lines)

    # Teste da função 'gerar_grafico'
    def test_gerar_grafico(self):
        count = {"Positivos": 1, "Negativos": 1, "Neutros": 1}
        base_name = "test_graph"

        gerar_grafico(count, base_name)

        # Verificar se o ficheiro gráfico foi criado
        output_file = os.path.join(self.output_dir, f"{base_name}-analise.png")
        self.assertTrue(os.path.exists(output_file))

    # Teste de integração
    @patch('builtins.print')  # Mutar apenas o print da chamada 'analisar_comentarios'
    def test_fluxo_completo(self, _):
        analisar_comentarios(self.sample_file)

        # Verificar se os ficheiros foram criados
        base_name = "test_comments"
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, f"{base_name}-analise.png")))
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, f"{base_name}-classificacao.csv")))

if __name__ == "__main__":
    unittest.main()
