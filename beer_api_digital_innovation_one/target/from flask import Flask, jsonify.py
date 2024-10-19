from flask import Flask, jsonify # type: ignore

app = Flask(__name__)

# Dados de exemplo para o estoque
estoque = {
    "cervejas": {
        "daniels": 100,
        "IPA": 50,
        "Weiss": 30
    }
}

# Rota para resetar o estoque
@app.route('/reset_estoque', methods=['POST'])
def reset_estoque():
    global estoque
    estoque = {
        "cervejas": {
            "daniels": 100,
            "IPA": 50,
            "Weiss": 30
        }
    }
    return jsonify({"message": "Estoque resetado com sucesso"}), 200
import unittest
from app import app, estoque # type: ignore

class TestResetEstoqueAPI(unittest.TestCase):

    def setUp(self):
        # Configurando o ambiente de testes
        self.app = app.test_client()
        self.app.testing = True

    def test_reset_estoque(self):
        # Modificar o estoque atual antes do reset
        estoque['cervejas']['daniels'] = 0
        estoque['cervejas']['IPA'] = 0
        estoque['cervejas']['Weiss'] = 0

        # Fazendo a requisição POST para resetar o estoque
        response = self.app.post('/reset_estoque')

        # Verificar o código de status
        self.assertEqual(response.status_code, 200)

        # Verificar a mensagem de sucesso
        self.assertIn(b'Estoque resetado com sucesso', response.data)

        # Verificar se o estoque foi resetado corretamente
        self.assertEqual(estoque['cervejas']['daniels'], 100)
        self.assertEqual(estoque['cervejas']['IPA'], 50)
        self.assertEqual(estoque['cervejas']['Weiss'], 30)

if __name__ == '__main__':
    unittest.main()

