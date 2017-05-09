'''

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Created on 20 Aug 2016

@author: James
'''

class Problem01(object):

    def __init__(self):
        self.terms = []
        
    def termsInFizzBuzz(self, upperlimit):
        for term in range(upperlimit):
            if term % 3 == 0 or term % 5 == 0:
                self.terms.append(term)
                
    def sumTerms(self):
        total = 0
        for term in self.terms:
            total += term
        return total