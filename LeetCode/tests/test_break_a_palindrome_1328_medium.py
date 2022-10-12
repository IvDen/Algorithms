import unittest

from LeetCode.tasks.break_a_palindrome_1328_medium import Solution


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_base0(self):
        self.assertEqual(self.solution.breakPalindrome('a'), '')

    def test_base1(self):
        self.assertEqual(self.solution.breakPalindrome('abccba'), 'aaccba')

    def test_base2(self):
        self.assertEqual(self.solution.breakPalindrome('aa'), 'ab')

    def test_base3(self):
        self.assertEqual(self.solution.breakPalindrome('aba'), 'abb')

    def test_base_empty_input(self):
        self.assertEqual(self.solution.breakPalindrome(''), '')


if __name__ == "__main__":
    unittest.main()
