import unittest

from tasks.increasing_triplet_subsequence_334_medium import Solution


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_base0(self):
        self.assertEqual(self.solution.increasingTriplet([1, 2, 3, 4, 5]), True)

    def test_base1(self):
        self.assertEqual(self.solution.increasingTriplet([5, 4, 3, 2, 1]), False)

    def test_base2(self):
        self.assertEqual(self.solution.increasingTriplet([2, 1, 5, 0, 4, 6]), True)

    def test_empty_input(self):
        self.assertEqual(self.solution.increasingTriplet([]), False)

    def test_no_increment(self):
        self.assertEqual(self.solution.increasingTriplet([1, 1, 1, 1, 1]), False)
