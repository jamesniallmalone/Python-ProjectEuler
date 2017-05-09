'''
Created on 30 Aug 2016

@author: James
'''
import unittest

from source import Problem09

class ProblemTest09(unittest.TestCase):


    def test_problem09_basecase(self):
        prob09 = Problem09.Problem09()
        
        prod = prob09.find_pythagorean_product(12)
        
        self.assertEqual(prod, 60, 'Incorrect.')
        
        
    def test_problem09_complex(self):
        prob09 = Problem09.Problem09()
        
        prod = prob09.find_pythagorean_product(1000)
        
        self.assertEqual(prod, 31875000, 'Incorrect.')