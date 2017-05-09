'''
Created on 29 Aug 2016

@author: James
'''
import unittest

from source import Problem17

class ProblemTest17(unittest.TestCase):

    def test_problem17_basecase(self):
        problem17 = Problem17.Problem17()
        
        upperbound = 5
        
        sum_letters_used = problem17.iterate_nums(upperbound)
        
        #print('letters used: ' + str(sum_letters_used))
        
        self.assertEqual(sum_letters_used, 19, "Numbers inclusive")
        
    def test_problem17_complex(self):
        problem17 = Problem17.Problem17()
        
        upperbound = 1000
        
        sum_letters_used = problem17.iterate_nums(upperbound)
        
        #print('letters used: ' + str(sum_letters_used))
        
        self.assertEqual(sum_letters_used, 21124, "Numbers inclusive")