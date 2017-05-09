'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Created on 29 Aug 2016

@author: James
'''

class Problem06(object):
    '''
    classdocs
    '''
    def __init__(self):
        pass
    
    def sum_squares(self, sequence_length):
        total = 0
        
        for num in range(sequence_length+1):
            total += num * num
        
        return total
    
    def square_sum(self, sequence_length):
        total = 0
        
        for num in range(sequence_length+1):
            total += num
        
        return total * total
    
    def difference(self, sum_squares, square_sums):
        return sum_squares - square_sums