import unittest 

from source import Problem04

class ProblemTest04(unittest.TestCase):
    
    def test_problem04_basecase(self):
        lp = Problem04.Problem04()
        
        largestpalindrome = lp.LargestPalindrome(2)
        
        self.assertEqual(largestpalindrome, 9009, "Not found")
        
    def test_problem04_challenge(self):
        lp = Problem04.Problem04()
        
        largestpalindrome = lp.LargestPalindrome(3)
        
        self.assertEqual(largestpalindrome, 906609, "Not found")