'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Created on 20 Aug 2016

@author: James
'''

class Problem04(object):

    def __init__(self):
        pass
    
    def ReverseNumber(self, original_num):
        return str(original_num) == str(original_num)[::-1]
        
    
    def LargestPalindrome(self, max_digits):
        upperbound = 10**max_digits
        lowerbound = 10**(max_digits-1)
        palindrome = 0
        
        for n in range(upperbound, lowerbound,-1):
            for m in range(upperbound, lowerbound,-1):
                
                product = n*m
                
                if product > palindrome:
                    if self.ReverseNumber(product):
                        palindrome = product
                
                    
        return palindrome
        