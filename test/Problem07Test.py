'''
Created on 29 Aug 2016

@author: James
'''
import unittest

from source import Problem07

class ProblemTest07(unittest.TestCase):

    def test_problem07_basecase(self):
        problem7 = Problem07.Problem07()
        
        upperbound = 6
        
        nth_prime = problem7.find_nth_prime_number(upperbound)
        
        self.assertEqual(nth_prime, 13, "Wrong prime number")
        
    def test_problem7_complex(self):
        problem7 = Problem07.Problem07()
        
        upperbound = 10001
        
        nth_prime = problem7.find_nth_prime_number(upperbound)
        
        self.assertEqual(nth_prime, 104743, "Wrong prime number")
        