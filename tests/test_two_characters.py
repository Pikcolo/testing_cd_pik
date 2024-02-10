from two_characters.two_characters import alternate
import unittest

class TwoCharactersTest(unittest.TestCase):
    def test_give_beabeefeab_is_5_in_result(self):
        s = 'beabeefeab'
        are_two_chars = alternate(s)
        self.assertEqual(are_two_chars, 5)

    def test_give_pkpxpz_is_2_in_result(self):
        s = 'pkpxpz'
        are_two_chars = alternate(s)
        self.assertEqual(are_two_chars, 2)

    def test_give_pikzalnwsussybaka_is_3_in_result(self):
        s = 'pikzalnwsussybaka'
        are_two_chars = alternate(s)
        self.assertEqual(are_two_chars, 3)

    def test_give_zzzxxxcccvvvbbbnnn_is_0_in_result(self):
        s = 'zzzxxxcccvvvbbbnnn'
        are_two_chars = alternate(s)
        self.assertEqual(are_two_chars, 0)

    def test_give_PIKlnwsuSSybAka_is_3_in_result(self):
        s = 'PIKlnwsussybaka'
        are_two_chars = alternate(s)
        self.assertEqual(are_two_chars, 3)

    def test_give_suSSybAka999_is_2_in_result(self):
        s = 'suSSybAka99'
        are_two_chars = alternate(s)
        self.assertEqual(are_two_chars, 2)

    def test_give_beesuSSybAka999_with_special_is_3_in_result(self):
        s = 'beesuSSybAka999*/@#'
        are_two_chars = alternate(s)
        self.assertEqual(are_two_chars, 3)

    def test_give_string_lower_than_2_result_is_0(self):
        s = 'p'
        are_two_chars = alternate(s)
        self.assertEqual(are_two_chars, 0)

    def test_give_string_equal_2_result_is_2(self):
        s = 'pe'
        are_two_chars = alternate(s)
        self.assertEqual(are_two_chars, 2)