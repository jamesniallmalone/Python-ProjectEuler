'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

Created on 29 Aug 2016

@author: James
'''
from pip._vendor.requests.packages.urllib3.connectionpool import xrange

class Problem07(object):
    '''
    classdocs
    '''
    def __init__(self):
        self.list_primes = [2]
        
    def find_nth_prime_number(self, limit):
        item = 3
        while len(self.list_primes) < limit:
            if all(item % num != 0 for num in xrange(2, int(item** 0.5 ) +1)):
                self.list_primes.append(item)
            item += 1
                
        return self.list_primes[-1]
        
        #pass