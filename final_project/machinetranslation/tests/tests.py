import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_e2f_null(self):
        self.assertEqual(english_to_french(None), None)
    
    def test_e2f_hello(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_f2e_null(self):
        self.assertEqual(french_to_english(None), None)
    
    def test_f2e_hello(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()
