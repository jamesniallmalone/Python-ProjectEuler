'''
Created on 30 Aug 2016

@author: James
'''
import unittest

from source import Problem12

class Problem12Test(unittest.TestCase):
        
    def test_problem12_basecase(self):
        problem12 = Problem12.Problem12()
        
        nth_tri = problem12.find_triangle_index(5)
        
        self.assertEqual(nth_tri, 7, 'Incorrect')
        
        tri_num = problem12.find_triangle(nth_tri)
        
        self.assertEqual(tri_num, 28, 'Incorrect')
        
    def test_problem12_complex(self):
        problem12 = Problem12.Problem12()
        
        nth_tri = problem12.find_triangle_index(500)
        
        self.assertEqual(nth_tri, 12375, 'Incorrect')
        
        tri_num = problem12.find_triangle(nth_tri)
        
        self.assertEqual(tri_num, 76576500, 'Incorrect')