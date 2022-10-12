import unittest

from YaContest.tasks.search_dist_to_zero import task_3


class TestClass(unittest.TestCase):

    def test_case0(self):
        self.assertEqual(task_3([0, ]), [0, ])

    def test_case1(self):
        self.assertEqual(task_3([0, 1, 4, 9, 0]), [0, 1, 2, 1, 0])

    def test_case2(self):
        self.assertEqual(task_3([0, 7, 9, 4, 8, 20]), [0, 1, 2, 3, 4, 5])

    def test_case3(self):
        self.assertEqual(task_3([0, 1]), [0, 1])

    def test_case4(self):
        self.assertEqual(task_3([1, 0]), [1, 0])

    def test_case5(self):
        self.assertEqual(task_3([0, 1, 2, 0, 3, 4, 0]), [0, 1, 1, 0, 1, 1, 0])

    def test_case6(self):
        self.assertEqual(task_3([0, 0, 0, 0, 0, 0, 0]), [0, 0, 0, 0, 0, 0, 0])

    def test_case7(self):
        self.assertEqual(task_3([64, 68, 37, 11, 77, 80, 48, 82, 0]), [8, 7, 6, 5, 4, 3, 2, 1, 0])

    def test_case8(self):
        self.assertEqual(task_3([0, 1, 2, 0, 0, 4, 0]), [0, 1, 1, 0, 0, 1, 0])


if __name__ == '__main__':
    unittest.main()