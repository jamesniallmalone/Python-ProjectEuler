'''
Created on 20 Aug 2016

@author: James
'''
import unittest

from source import Problem01

class ProblemTest01(unittest.TestCase):


    def test_problem01_basecase(self):
        lp = Problem01.Problem01()
        
        lp.termsInFizzBuzz(10)
        
        self.assertEqual(lp.sumTerms(), 23, "Not found")
        
    def test_problem01_challenge(self):
        lp = Problem01.Problem01()
        
        lp.termsInFizzBuzz(1000)
        
        self.assertEqual(lp.sumTerms(), 233168, "Not found")
