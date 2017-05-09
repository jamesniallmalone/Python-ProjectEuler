'''

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Created on 29 Aug 2016

@author: James
'''

class Problem03(object):

    def __init__(self):
        pass
        
    def findAllPrime(self, product):
        list_of_primes = []
        
        under_consideration = 2
        while(product >= under_consideration):
            if product % under_consideration == 0:
                list_of_primes.append(under_consideration)
                product /= under_consideration
            
            under_consideration += 1
            
        
        return list_of_primes
    
    def LargestPrime(self, product):
        return product[-1]