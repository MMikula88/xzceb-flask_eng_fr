import unittest

from translator import english_to_french, french_to_english

class Teste2f(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Yes'), 'Yes')


class Testf2e(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Oui'), 'Oui')

unittest.main()
