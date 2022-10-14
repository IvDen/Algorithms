import unittest

from Sorting.tasks.merge_sorting import sort_by_merge


class TestClass(unittest.TestCase):

    def test_case0(self):
        self.assertEqual(sort_by_merge([6,6,5,5,4,3,2,1],1, 8), [1,2,3,4,5,5,6,6])

    def test_case1(self):
        self.assertEqual(sort_by_merge([4, 3, 2, 1], 1, 4), [1, 2, 3, 4])

    def test_case2(self):
        self.assertEqual(sort_by_merge([1, 1, 1, 1], 1, 4), [1, 1, 1, 1])


if __name__ == '__main__':
    unittest.main()
