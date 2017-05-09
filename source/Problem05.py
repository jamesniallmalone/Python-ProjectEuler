'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Created on 20 Aug 2016

@author: James
'''
from math import floor

class Problem05(object):
          
    def __init__(self, upperlimit):
        self.list_primes = [2]
        self.listnum = []
        for item in range(2, upperlimit+1):
            self.listnum.append(item)
            
    def is_number_prime(self, sample_number):
        for num in self.list_primes:
            if sample_number % num == 0:
                return False
        
        return True
                
    def lowestCommonMultiple(self,x,y):
        if x % y == 0: # already a factor. nothing to do here.
            return x
        
        #find if number is prime
        
        closest_factor_to_prevlcm = y * (floor(x/y)+1) if floor(x/y) > 0 else y
        
        if self.is_number_prime(y):
            closest_factor_to_prevlcm = x * y
            self.list_primes.append(y)
        
        while (True):    
            if ((closest_factor_to_prevlcm % x == 0) and (closest_factor_to_prevlcm % y == 0)):
                lcm = closest_factor_to_prevlcm
                break
            closest_factor_to_prevlcm += y
            
        
        return lcm
        
        
    def findLCM(self):
        
        lcm = self.lowestCommonMultiple(self.listnum[0], self.listnum[1])
        
        for item in self.listnum:
            lcm = self.lowestCommonMultiple(lcm, item)
        
        return lcm
        