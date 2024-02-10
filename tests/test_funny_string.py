from funny_string.funny_string import funnyString
import unittest

class FunnyStringTest(unittest.TestCase):
    def test_give_3acxz_is_funny(self):
        s = 'acxz'
        is_funnystring = funnyString(s)
        self.assertEqual(is_funnystring, 'Funny')
    
