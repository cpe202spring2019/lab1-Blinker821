import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """Tests max_list for ValueError"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
    def test_max_list_iter1(self):
        """Tests max_list for an empty list"""
        tlist = []
        self.assertEquals(max_list_iter(tlist), None)
    def test_max_list_iter2(self):
        """Tests max_list for a normal list"""
        tlist = [1,2,3]
        self.assertEquals(max_list_iter(tlist), 3)
    def test_max_list_iter3(self):
        """Tests max_list for another normal list"""
        tlist = [3, 21, 4]
        self.assertEquals(max_list_iter(tlist), 21)

    def test_reverse_rec(self):
        """Tests reverse_rec normally"""
        self.assertEquals(reverse_rec([1,2,3]),[3,2,1])
    def test_reverse_rec1(self):
        """Tests reverse_rec normally again"""
        tlist = [42, 13, 7]
        self.assertEquals(reverse_rec(tlist), [7,13,42])
    def test_reverse_rec2(self):
        """Tests reverse_rec for ValueError"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)

    def test_bin_search(self):
        """Tests bin_search normally"""
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
    def test_bin_search1(self):
        """Tests bin_search for upper edge case"""
        list_val = [12, 34, 92, 6]
        low = 2
        high = len(list_val)-1
        self.assertEqual(bin_search(6, low, high, list_val), 3)
    def test_bin_search2(self):
        """Tests bin_search for lower edge case"""
        list_val = [12, 34, 92, 6]
        low = 2
        high = len(list_val)-1
        self.assertEqual(bin_search(92, low, high, list_val), 2)
    def test_bin_search3(self):
        """Tests_bin_search for ValueError"""
        list_val = None
        low = 0
        high = 10
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(92, low, high, list_val)
    def test_bin_search4(self):
        """Tests bin_search for target not in list"""
        list_val = [3,4,5,6]
        low = 0
        high = 3
        self.assertEqual(bin_search(12, low, high, list_val), None)

if __name__ == "__main__":
        unittest.main()

    
