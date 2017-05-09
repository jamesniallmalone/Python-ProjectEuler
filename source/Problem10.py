'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Created on 30 Aug 2016

@author: James
'''
from pip._vendor.requests.packages.urllib3.connectionpool import xrange

class Problem10(object):
    def __init__(self):
        pass
    
    def mark(self, sieve, x):
        for i in xrange(2*x, len(sieve), x):
            sieve[i] = False
    
    def sum_prime_numbers(self, limit):
        sieve = [True] * limit
        
        for x in xrange(2, int(len(sieve) ** 0.5 ) +1):
            if sieve[x]: self.mark(sieve, x)
        
        total = sum(i for i in xrange(2, len(sieve)) if sieve[i])
        
        return total