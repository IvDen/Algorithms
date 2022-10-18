import unittest

from YaContest.tasks.tricky_cipher import tricky_cipher


class TestClass(unittest.TestCase):

    def test_case0(self):
        self.assertEqual(tricky_cipher(['2', 'Volozh,Arcady,Yurievich,11,2,1964',
                                        'Segalovich,Ilya,Valentinovich,13,9,1964']),
                         '710 64F \n')


if __name__ == '__main__':
    unittest.main()
