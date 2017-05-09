'''
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

Created on 31 Aug 2016

@author: James
'''
from pip._vendor.requests.packages.urllib3.connectionpool import xrange

class Problem14(object):
    '''
    classdocs
    '''

#Store the lengths of the collatz sequence in a hash table. No need to recompute
    def __init__(self):
        #we know we always reach 1 eventually.
        self.cache = {1:1}
        
    def collatz(self, n):
        if n not in self.cache:
            self.cache[n] = self.collatz(3 * n + 1 if n%2 else n/2) + 1
            
        return self.cache[n]
    
    def longest_collatz_sequence(self, t):    
        return max(xrange(1,t), key= self.collatz)
    
    