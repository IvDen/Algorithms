import unittest

from YaContest.tasks.tree_bin_iterative_changes import tree_bin_iterative_changes


class TestClass(unittest.TestCase):

    def test_case0(self):
        self.assertEqual(tree_bin_iterative_changes('6 2\n5'),
                         '7 10 5 2 8 4 9 1 6 3 \n')

    def test_case1(self):
        self.assertEqual(tree_bin_iterative_changes('10 6\n5 7 4 7 8 7'),
                         '7 10 5 2 8 4 9 1 6 3 \n')


if __name__ == '__main__':
    unittest.main()
