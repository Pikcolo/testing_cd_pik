from funny_string.funny_string import funnyString
import unittest

class FunnyStringTest(unittest.TestCase):
    def test_give_bacxz_is_funny(self):
        s = 'acxz'
        is_funnystring = funnyString(s)
        self.assertEqual(is_funnystring, 'Funny')

    def test_give_hjlnp_is_funny(self):
        s = 'hjlnp'
        is_funnystring = funnyString(s)
        self.assertEqual(is_funnystring, 'Funny')

    def test_give_uvzxrumuztyqyvpnji_is_funny(self):
        s = 'uvzxrumuztyqyvpnji'
        is_funnystring = funnyString(s)
        self.assertEqual(is_funnystring, 'Funny')

    def test_give_jkmsxzwrxzy_is_not_funny(self):
        s = 'yrzxrxskrtlpwpmtpxvowrxrpxq'
        is_funnystring = funnyString(s)
        self.assertEqual(is_funnystring, 'Not Funny')

    def test_give_bcxz_is_not_funny(self):
        s = 'bcxz'
        is_funnystring = funnyString(s)
        self.assertEqual(is_funnystring, 'Not Funny')

    def test_give_jkmsxzwrxzy_is_funny(self):
        s = 'jkmsxzwrxzy'
        is_funnystring = funnyString(s)
        self.assertEqual(is_funnystring, 'Not Funny')



