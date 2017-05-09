'''
Created on 29 Aug 2016

@author: James
'''
import unittest
from source import Problem06

class ProblemTest06(unittest.TestCase):


    def test_problem06_basecase(self):
        lp = Problem06.Problem06()
        
        upperbound = 10
        
        sum_squares = lp.sum_squares(upperbound)
        self.assertEqual(sum_squares, 385, "Sum of all the squared numbers")
        
        square_sums = lp.square_sum(upperbound)
        self.assertEqual(square_sums, 3025, "Sum of all the squared numbers")
        
        self.assertEqual(lp.difference(square_sums, sum_squares), 2640, "Not Calculated correctly")
        
    def test_problem06_challenge(self):
        lp = Problem06.Problem06()
        
        upperbound = 100
        
        sum_squares = lp.sum_squares(upperbound)
        self.assertEqual(sum_squares, 338350, "Sum of all the squared numbers")
        
        square_sums = lp.square_sum(upperbound)
        self.assertEqual(square_sums, 25502500, "Sum of all the squared numbers")
        
        self.assertEqual(lp.difference(square_sums, sum_squares), 25164150, "Not Calculated correctly")