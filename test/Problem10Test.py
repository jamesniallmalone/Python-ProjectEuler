'''
Created on 30 Aug 2016

@author: James
'''
import unittest

from source import Problem10

class Problem10Test(unittest.TestCase):

    def test_problem10_basecase(self):
        prob10 = Problem10.Problem10()
        
        sum_prime = prob10.sum_prime_numbers(10)
        
        self.assertEqual(sum_prime, 17, 'Incorrect.')
        
    def test_problem10_complex(self):
        prob10 = Problem10.Problem10()
        
        sum_prime = prob10.sum_prime_numbers(2000000)
        
        self.assertEqual(sum_prime, 142913828922, 'Incorrect.')