import unittest 

from source import Problem03

class ProblemTest03(unittest.TestCase):
    
    def test_problem03_basecase(self):
        lp = Problem03.Problem03()
        
        allprimes = lp.findAllPrime(13195)
        n = lp.LargestPrime(allprimes)
        
        self.assertEqual(n, 29, "Not found")
        
    def test_problem03_alteredbasecase(self):
        lp = Problem03.Problem03()
        
        allprimes = lp.findAllPrime(65975)
        n = lp.LargestPrime(allprimes)
        
        self.assertEqual(n, 29, "Not found")
        
    def test_problem03_challenge(self):
        lp = Problem03.Problem03()
        
        allprimes = lp.findAllPrime(600851475143)
        n = lp.LargestPrime(allprimes)
        
        self.assertEqual(n, 6857, "Not found")