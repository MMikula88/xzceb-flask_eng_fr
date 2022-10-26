import unittest

from translator import englishToFrench, frenchToEnglish

class Teste2f(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishToFrench('Yes'), 'Yes')


class Testf2e(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertNotEqual(frenchToEnglish('Oui'), 'Oui')

unittest.main()
