'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

Created on 29 Aug 2016

@author: James
'''
from builtins import sorted

class Problem17(object):
    
    units = {1:'one',2:'two',3:'three',4:'four',5:'five',
             6:'six',7:'seven',8:'eight',9:'nine',10:'ten',
             11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',
             16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',
             20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',
             70:'seventy',80:'eighty',90:'ninety',100:'hundred',1000:'thousand'}
    
    def __init__(self):
        pass
    
    def count_letters(self, word):
        #print(word)
        return len(word)
    
    
    def iterate_nums(self, limit):
        total = 0
        
        for current_num in range(limit+1):
            #print('---------------------------------------')

            str_limit = str(current_num)
            length_num = len(str_limit)
            
            if length_num == 4:
                leftmost_num = int(str_limit[-4])
                
                if(leftmost_num > 0):
                    total += self.count_letters(self.units[leftmost_num])
                    total += self.count_letters(self.units[1000])
                
            if length_num >= 3:
                thirdnum = int(str_limit[-3])
                
                if thirdnum > 0:
                    total += self.count_letters(self.units[thirdnum])
                    total += self.count_letters(self.units[100])
                
            if length_num > 2 and current_num % 100 != 0:
                joining_word = 'and'
                #print(joining_word)
                total += len(joining_word)
                
            remainder = current_num % 100
            
            for i in sorted(self.units.keys(), reverse=True):
                if remainder >= i and remainder != 0:
                    remainder -= i
                    total += self.count_letters(self.units[i])
            
        return total