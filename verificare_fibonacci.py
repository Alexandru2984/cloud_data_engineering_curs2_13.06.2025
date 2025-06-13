import unittest
from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_primul_element(self):
        self.assertEqual(fibonacci(0), 0)

    def test_al_doilea_element(self):
        self.assertEqual(fibonacci(1), 1)

    def test_al_treilea_element(self):
        self.assertEqual(fibonacci(2), 1)

    def test_elementul_5(self):
        self.assertEqual(fibonacci(5), 5)

    def test_elementul_10(self):
        self.assertEqual(fibonacci(10), 55)

if __name__ == '__main__':
    unittest.main()
