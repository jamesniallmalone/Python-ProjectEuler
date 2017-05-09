'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Created on 30 Aug 2016

@author: James
'''

class Problem09(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def is_pythagorean_triplet(self,a,b,c):
        return a**2 + b**2 == c**2
    
    def find_product(self,a,b,c):
        return a*b*c
    
    def find_pythagorean_product(self, limit):
        for a in range(limit):
            for b in range(limit):
                c = limit - a - b
                
                if c <= b:
                    break
                
                if self.is_pythagorean_triplet(a, b, c):
                    return self.find_product(a, b, c)
        
        print('End reached. Could not be found')
        return 0
        
        