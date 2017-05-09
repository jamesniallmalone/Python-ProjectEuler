'''
Created on 20 Aug 2016

@author: James
'''
import unittest

from source import Problem05

class ProblemTest05(unittest.TestCase):

    def test_problem05_basecase(self):
        lp = Problem05.Problem05(10)
        
        lcm = lp.findLCM()
        self.assertEqual(lcm, 2520, "Not found")
        
    def test_problem05_challenge(self):
        lp = Problem05.Problem05(20)
        
        lcm = lp.findLCM()
        self.assertEqual(lcm, 232792560, "Not found")