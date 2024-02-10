from grid_challenge.grid_challenge import gridChallenge
import unittest

class GridChallengeTest(unittest.TestCase):
    def test_case_alphabet1_sort(self):
        grid = ["abc", "def", "ghi"]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_case_alphabet2_sort(self):
        grid = ["abcdefg", "hijklmn", "opqrstu"]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_case_duplicate_str_sort(self):
        grid = ["aaaa", "bbbb", "cccc"]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_case_duplicate2_str_sort(self):
        grid = ["aabb", "ccdd", "eeff"]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_case_duplicate2_switch(self):
        grid = ["abba", "cddc", "effe"]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_case_alphabet_not_sort(self):
        grid = ["abfg", "zxcw", "erty"]
        self.assertEqual(gridChallenge(grid), "NO")

    def test_case_alphabet_random_switch_in3char(self):
        grid = ["qwa", "aoi", "pik"]
        self.assertEqual(gridChallenge(grid), "NO")

    def test_case_alphabet_random_switch_in3char_upper(self):
        grid = ["ASD", "API", "SQL"]
        self.assertEqual(gridChallenge(grid), "NO")

