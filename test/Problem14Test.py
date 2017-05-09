'''
Created on 31 Aug 2016

@author: James
'''
import unittest

from source import Problem14

class Problem14Test(unittest.TestCase):


    def test_problem14_basecase(self):
        p14 = Problem14.Problem14()
        
        terms = p14.collatz(13)
        
        self.assertEqual(10, terms, 'incorrect')
        
        
    def test_problem14_complex(self):
        p14 = Problem14.Problem14()
        
        terms = p14.longest_collatz_sequence(1000000)
        
        self.assertEqual(837799, terms, 'incorrect')
        