import unittest

from YaContest.tasks.interval_time_through_thorns_to_a_client import interval_time_through_thorns_to_a_client


class TestClass(unittest.TestCase):

    def test_case0(self):
        self.assertEqual(interval_time_through_thorns_to_a_client(['8',
                                 '50 7 25 3632 A',
                                 '14 23 52 212372 S',
                                 '15 0 5 3632 C',
                                 '14 21 30 212372 A',
                                 '50 7 26 3632 C',
                                 '14 21 30 3632 A',
                                 '14 21 40 212372 B',
                                 '14 23 52 3632 B']), '156 142 \n')

    def test_case1(self):
        self.assertEqual(interval_time_through_thorns_to_a_client(['9',
                                 '01 01 01 3632 C',
                                 '50 7 25 3632 A',
                                 '14 23 52 212372 S',
                                 '15 0 5 3632 C',
                                 '14 21 30 212372 A',
                                 '50 7 26 3632 C',
                                 '14 21 30 3632 A',
                                 '14 21 40 212372 B',
                                 '14 23 52 3632 B']), '156 142 \n')

    def test_case3(self):
        self.assertEqual(interval_time_through_thorns_to_a_client(['10',
                                 '01 01 01 3632 A',
                                 '01 01 02 3632 C',
                                 '50 7 25 3632 A',
                                 '14 23 52 212372 S',
                                 '15 0 5 3632 C',
                                 '14 21 30 212372 A',
                                 '50 7 26 3632 C',
                                 '14 21 30 3632 A',
                                 '14 21 40 212372 B',
                                 '14 23 52 3632 B']), '157 142 \n')


if __name__ == '__main__':
    unittest.main()
