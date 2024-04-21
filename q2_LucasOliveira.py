import unittest
from unittest.mock import patch
import random
from io import StringIO

from q1_LucasOliveira import processar_transacao, criar_transacao, transacao_com_dinheiro

class test_de_(unittest.TestCase):

    def configuracao_do_test(self):
        self.user_name = "admin"
        self.user_Fund = round(random.uniform(1, 2000), 2)

    def test_fundo_de_transferencia(self):
        with patch('builtins.input', side_effect=['Confirmar']):
            result = processar_transacao(self.user_Fund, self.user_name, "Transferência de Fundos")
            self.assertEqual(result, "Transação concluída")

        with patch('builtins.input', side_effect=['Cancelar']):
            result = processar_transacao(self.user_Fund, self.user_name, "Transferência de Fundos")
            self.assertEqual(result, "Transação encerrada")

    def test_credito(self):
        with patch('builtins.input', side_effect=['Confirmar']):
            result = processar_transacao(self.user_Fund, self.user_name, "Crédito")
            self.assertEqual(result, "Transação concluída")

        with patch('builtins.input', side_effect=['Cancelar']):
            result = processar_transacao(self.user_Fund, self.user_name, "Crédito")
            self.assertEqual(result, "Transação encerrada")

    def test_criar_transação(self):
    # Verificando a transação de tipo "Cash"
        with patch('builtins.input', side_effect=['Cash', '100']):  # Entrada para tipo de transação e valor
            result = criar_transacao(self.user_Fund, self.user_name)
            self.assertEqual(result, "Transação concluída")

        # Verificando a transação de tipo "Fund Transfer" com confirmação
        with patch('builtins.input', side_effect=['Fund Transfer', 'Confirmar']):
            result = criar_transacao(self.user_Fund, self.user_name)
            self.assertEqual(result, "Transação concluída")

        # Verificando a transação de tipo "Fund Transfer" com cancelamento
        with patch('builtins.input', side_effect=['Fund Transfer', 'Cancelar']):
            result = criar_transacao(self.user_Fund, self.user_name)
            self.assertEqual(result, "Transação encerrada")

        # Verificando a transação de tipo "Credit" com confirmação
        with patch('builtins.input', side_effect=['Credit', 'Confirmar']):
            result = criar_transacao(self.user_Fund, self.user_name)
            self.assertEqual(result, "Transação concluída")

        # Verificando a transação de tipo "Credit" com cancelamento
        with patch('builtins.input', side_effect=['Credit', 'Cancelar']):
            result = criar_transacao(self.user_Fund, self.user_name)
            self.assertEqual(result, "Transação encerrada")

        # Verificando a transação de tipo inválido
        with patch('builtins.input', side_effect=['Invalid']):
            result = criar_transacao(self.user_Fund, self.user_name)
            self.assertEqual(result, "Tipo de Transação Não existe - Transação cancelada")
            
    def test_dinheiro(self):
        with patch('builtins.input', side_effect=['100']):
            with patch('sys.stdout', new_callable=StringIO) as fake_out:
                result = transacao_com_dinheiro(self.user_Fund)
                self.assertEqual(result, "Transação concluída")
                self.assertIn("Emitindo Comprovante de Pagamento", fake_out.getvalue())


if __name__ == '__main__':
    unittest.main()
