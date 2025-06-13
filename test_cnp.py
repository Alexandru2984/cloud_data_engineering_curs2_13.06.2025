import unittest
from cnp import este_cnp_valid

class TestCNP(unittest.TestCase):

    def test_cnp_corect(self):
        self.assertTrue(este_cnp_valid("1960508223454"))

    def test_cnp_scurt(self):
        self.assertFalse(este_cnp_valid("19605082234"))

    def test_cnp_lung(self):
        self.assertFalse(este_cnp_valid("1960508223457999"))

    def test_cnp_cu_litere(self):
        self.assertFalse(este_cnp_valid("1a60508223457"))

    def test_cnp_cu_cifra_de_control_gresita(self):
        self.assertFalse(este_cnp_valid("1960508223458"))

    def test_cnp_cu_data_invalidă(self):
        self.assertFalse(este_cnp_valid("1961331223457"))  # luna 13

if __name__ == '__main__':
    unittest.main()
