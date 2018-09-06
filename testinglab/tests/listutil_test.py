import unittest
from listutil import count_unique

class TestListUtil(unittest.TestCase):

    def test_borderline(self):
        self.assertEqual(count_unique([ ]),0)

    def test_typical(self):
        l = ['a','a','b','b','a','c','c','c','c','d']
        self.assertEqual(count_unique(l),4)

    def test_impossible(self):
        with self.assertRaises(Exception):count_unique('str')

    def test_extreme(self):
        l = ['a', 'b', 'c', 'd', 'e'
            , 'f', 'g', 'h', 'i', 'j'
            , 'k', 'l','c', 'm', 'n', 'o'
            , 'p', 'q', 'r','a,' 's', 't'
            , 'u', 'v','b','b', 'w', 'x', 'y', 'z']
        self.assertEqual(count_unique(l),26)

    def test_capital(self):
        self.assertEqual(count_unique(['a','b','B','b','a','C','c']),3)









if __name__ == '__main__':
    unittest.main()