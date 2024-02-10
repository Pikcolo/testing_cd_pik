from caesar_cipher.caesar_cipher import caesarCipher
import unittest

class CaesarCipherTest(unittest.TestCase):
    def test_give_k_is_3_if_s_is_lower(self):
        s = 'pik'
        k = 3
        is_ceasaripher = caesarCipher(s, k)
        self.assertEqual(is_ceasaripher, 'sln')

    def test_give_k_is_3_if_s_is_upper(self):
        s = 'PIK'
        k = 3
        is_ceasaripher = caesarCipher(s, k)
        self.assertEqual(is_ceasaripher, 'SLN')

    def test_give_k_is_3_if_s_is_num(self):
        s = '123456789'
        k = 3
        is_ceasaripher = caesarCipher(s, k)
        self.assertEqual(is_ceasaripher, '123456789')
    
    def test_give_k_is_3_if_s_is_special(self):
        s = '+-*/@#$%^&'
        k = 3
        is_ceasaripher = caesarCipher(s, k)
        self.assertEqual(is_ceasaripher, '+-*/@#$%^&')

    def test_give_k_is_3_if_s_is_lower_and_upper(self):
        s = 'pIK'
        k = 3
        is_ceasaripher = caesarCipher(s, k)
        self.assertEqual(is_ceasaripher, 'sLN')

    def test_give_k_is_3_if_s_is_isalpha_and_have_num(self):
        s = 'Pik12'
        k = 3
        is_ceasaripher = caesarCipher(s, k)
        self.assertEqual(is_ceasaripher, 'Sln12')

    def test_give_k_is_3_if_s_is_isalpha_num_spacial(self):
        s = 'Pik12@#'
        k = 3
        is_ceasaripher = caesarCipher(s, k)
        self.assertEqual(is_ceasaripher, 'Sln12@#')

    def test_give_k_is_3_if_s_is_empty(self):
        s = ''
        k = 3
        is_ceasaripher = caesarCipher(s, k)
        self.assertEqual(is_ceasaripher, '')

    def test_give_k_is_5_if_s_is_all(self):
        s = 'PikLoveMoM999@%*/'
        k = 5
        is_ceasaripher = caesarCipher(s, k)
        self.assertEqual(is_ceasaripher, 'UnpQtajRtR999@%*/')
