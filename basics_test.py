import sys
import os
import get_column_stats
import unittest
import random

class TestCalc(unittest.TestCase):
    def test_mean(self):
        a = get_column_stats.calc_mean(self)
        self.assertEqual(a,self.mean) 

    def test_stdev(self):
        b = get_column_stats.calc_stdev(self)
        self.assertEqual(b,self.stdev) 

if __name__=='__main__':
    unittest.main()

