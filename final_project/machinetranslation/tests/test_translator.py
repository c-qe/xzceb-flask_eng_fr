'''
test_translator.py

@author: c-qe
'''
import unittest

from translator import english_to_french, french_to_english

class TestenglishToFrench(unittest.TestCase):
    '''unittest testcase'''
    def test_en_fr(self):
        '''Function to test english_to_french translations and null input response.'''
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Bonjour"), "Hello")
        self.assertIsNone(english_to_french(None))

class TestfrenchToEnglish(unittest.TestCase):
    '''unittest testcase'''
    def test_fr_en(self):
        '''Function to test french_to_english translations and null input response.'''
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Hello"), "Bonjour")
        self.assertIsNone(french_to_english(None))

if __name__ == '__main__':
    unittest.main()
