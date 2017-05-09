'''
Created on 1 Sep 2016

@author: James
'''
import unittest

from source import Problem16

class Problem16Test(unittest.TestCase):


    def test_problem16_basecase(self):
        prob16 = Problem16.Problem16()
        
        sol = prob16.power_digit_sum(15)
        
        self.assertEqual(sol, 26, 'blah')
        
    def test_problem16_complex(self):
        prob16 = Problem16.Problem16()
        
        sol = prob16.power_digit_sum(1000)
                
        self.assertEqual(sol, 1366, 'blah')