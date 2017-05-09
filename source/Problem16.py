'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

Created on 1 Sep 2016

@author: James
'''

class Problem16(object):

    def __init__(self):
        pass
    
    def find_power(self, exponent):
        return 2 ** exponent
    
    def strip_number_to_array(self, number):
        arr = []
        
        numstr = str(number)
        
        for ind in numstr:
            arr.append(int(ind))
            
        return arr
    
    def sum_array(self, arr):
        return sum(arr) 
    
    def power_digit_sum(self, power):
        return self.sum_array(self.strip_number_to_array(self.find_power(power)))