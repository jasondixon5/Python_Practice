#! /usr/bin/env python3

import unittest

def fun(x):
    if x % 2:
        return x + 1
    else:
        return x
    
class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 3)
        self.assertEqual(fun(2), 3)
        self.assertEqual(fun(4), 5)
        self.assertEqual(fun(7), 7)
        self.assertEqual(fun(8), 8)