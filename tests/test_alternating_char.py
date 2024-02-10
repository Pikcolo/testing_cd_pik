from alternating_char.alternating_char import alternatingCharacters
import unittest

class alternatingCharactersTest(unittest.TestCase):
    def test_give_AAAAA_is_4_in_deletions(self):
        s = "AAAAA"
        n_deletions = alternatingCharacters(s)
        self.assertEqual(n_deletions, 4)

    def test_give_AAABBB_is_5_in_deletions(self):
        s = "AAAABBB"
        n_deletions = alternatingCharacters(s)
        self.assertEqual(n_deletions, 5)

    def test_give_ABAAABBBABBAAABB_is_8_in_deletions(self):
        s = "ABAAABBBABBAAABB"
        n_deletions = alternatingCharacters(s)
        self.assertEqual(n_deletions, 8)

    def test_give_AAAAAAAABBBBBBB_is_13_in_deletions(self):
        s = "AAAAAAAABBBBBBB"
        n_deletions = alternatingCharacters(s)
        self.assertEqual(n_deletions, 13)

    def test_give_ABABABABABABBBAA_is_3_in_deletions(self):
        s = "ABABABABABABBBAA"
        n_deletions = alternatingCharacters(s)
        self.assertEqual(n_deletions, 3)

    def test_give_ABABABBAABAB_is_2_in_deletions(self):
        s = "ABABABBAABAB"
        n_deletions = alternatingCharacters(s)
        self.assertEqual(n_deletions, 2)

    def test_give_ABABABABABABABAA_is_1_in_deletions(self):
        s = "ABABABABABABABAA"
        n_deletions = alternatingCharacters(s)
        self.assertEqual(n_deletions, 1)

    def test_give_ABABABABABABAB_is_2_in_deletions(self):
        s = "ABABABABABABAB"
        n_deletions = alternatingCharacters(s)
        self.assertEqual(n_deletions, 0)