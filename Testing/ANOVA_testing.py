#! /usr/bin/env python3

import unittest
import ANOVA
from decimal import *

class TestAnova(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
        
    def test_ssb(self):
        low_cal = [Decimal(x) for x in [8, 9, 6, 7, 3]]
        low_fat = [Decimal(x) for x in [2, 4, 3, 5, 1]]
        low_carb = [Decimal(x) for x in [3, 5, 4, 2, 3]]
        control = [Decimal(x) for x in [2, 2, -1, 0, 3]]
        
        result = ANOVA.ssb(low_cal, low_fat, low_carb, control)
        self.assertEqual(result, Decimal(75.7500))
        
    def test_sse(self):
        low_cal = [Decimal(x) for x in [8, 9, 6, 7, 3]]
        low_fat = [Decimal(x) for x in [2, 4, 3, 5, 1]]
        low_carb = [Decimal(x) for x in [3, 5, 4, 2, 3]]
        control = [Decimal(x) for x in [2, 2, -1, 0, 3]]
    
        result = ANOVA.sse(low_cal, low_fat, low_carb, control)
        self.assertEqual(result, Decimal(47.2000))

    def test_fStatistic(self):
        low_cal = [Decimal(x) for x in [8, 9, 6, 7, 3]]
        low_fat = [Decimal(x) for x in [2, 4, 3, 5, 1]]
        low_carb = [Decimal(x) for x in [3, 5, 4, 2, 3]]
        control = [Decimal(x) for x in [2, 2, -1, 0, 3]]
    
        result = ANOVA.fStatistic(low_cal, low_fat, low_carb, control)
        self.assertEqual(result, Decimal(47.2000))

if __name__ == '__main__':
    unittest.main()
