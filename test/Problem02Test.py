import unittest 

from source import Problem02

class ProblemTest02(unittest.TestCase):
    
    def test_problem02_basecase(self):
        fib = Problem02.Problem02()
        
        all_primes = fib.find_range_below(100)
        
        self.assertEqual(all_primes, [1, 2, 3, 5, 8, 13, 21, 34, 55, 89], "Failed to create range")
        
        sum_of_range = fib.sum_even_range(all_primes)
        
        self.assertEqual(sum_of_range, 44, "Sum fail.")
        
    def test_problem02_challenge(self):
        fib = Problem02.Problem02()
        
        all_primes = fib.find_range_below(4000000)
        
        sum_of_range = fib.sum_even_range(all_primes)
        
        self.assertEqual(sum_of_range, 4613732, "Sum fail.")