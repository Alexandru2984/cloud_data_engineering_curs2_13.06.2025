import unittest
from email import este_valid
import time

# assert 2 == 3, "Aceste doua numere nu sunt egale"

class TestValidareEmail(unittest.TestCase):

    def test_email_contine_caractere(self):
        self.assertEqual(2, 2, "Cele doua trebuie sa fie egale")

    def test_de_test(self):
        self.assertNotEqual(2, 3, "Cele 2 nu trebuie sa fie egale")

    def test_contine_coada_de_maimuta(self):
        # self.assertTrue(este_valid("@."), "Trebuie sa contina @")
        self.assertFalse(este_valid("assd"), "Trebuie sa contina @")

    def test_contine_punct(self):
        # self.assertTrue(este_valid("@."), "Trebuie sa contina .")
        self.assertFalse(este_valid("csdvf@com"), "Trebuie sa contina .")

    def test_are_ceva_inainte_de_coada_de_maimuta(self):
        self.assertFalse(este_valid("@ceva.ro"), "Trebuie sa contina ceva inainte de @")

    def test_caractere_neobisnuite(self):
        self.assertFalse(este_valid("$@ceva.com"), "Trebuie sa nu contina caractere speciale")
        self.assertFalse(este_valid("#@ceva.com"), "Trebuie sa nu contina caractere speciale")
        self.assertFalse(este_valid("!@ceva.com"), "Trebuie sa nu contina caractere speciale")
        self.assertFalse(este_valid(">@ceva.com"), "Trebuie sa nu contina caractere speciale")
        self.assertFalse(este_valid("(@ceva.com"), "Trebuie sa nu contina caractere speciale")
        self.assertFalse(este_valid(")@ceva.com"), "Trebuie sa nu contina caractere speciale")
        self.assertFalse(este_valid(" @ceva.com"), "Trebuie sa nu contina caractere speciale")
        self.assertFalse(este_valid("?@ceva.com"), "Trebuie sa nu contina caractere speciale")

    def test_numar_caractere(self):
        self.assertFalse(este_valid("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@ceva.com"),"Numarul maxim este de 64 de caractere")

    def test_are_ceva_dupa_punct(self):
        self.assertFalse(este_valid("a@."), "Trebuie sa aiba minim 2 caractere dupa punct")
        self.assertFalse(este_valid("a@.--"), "Trebuie sa contina doar litere dupa punct")
        self.assertFalse(este_valid("a@.tt."))
        

    def test_minim_intre_puncte(self):    
        self.assertFalse(este_valid("a@..tt"))

    def test_1_coada_de_maimuta(self):
        self.assertFalse(este_valid("a@@.tt"))

    def test_(self):
        self.assertFalse(este_valid("a@-.tt"))



if __name__ == "__main__":
    unittest.main()

