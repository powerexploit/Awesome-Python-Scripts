# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 16:21:31 2020

@author: Abhay Paliwal
"""

"""This code is to convert any int32 number to it's English representation
   without using any in-built library """

"""The function int_to_en takes one integer parameter 'num' and returns 
    a string made of English representation of the number that is passed."""


def int_to_en(num):
    intEng = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
    thousand = 1000
    million = thousand * 1000
    billion = million * 1000
    trillion = billion * 1000

    assert(0 <= num)

    if (num < 20):
        return intEng[num]

    if (num < 100):
        if num % 10 == 0: return intEng[num]
        else: return intEng[num // 10 * 10] + ' ' + intEng[num % 10]

    if (num < thousand):
        if num % 100 == 0: return intEng[num // 100] + ' hundred'
        else: return intEng[num // 100] + ' hundred and ' + int_to_en(num % 100)
    
    if (num < million):
        if num % thousand == 0: return int_to_en(num // thousand) + ' thousand'
        else: return int_to_en(num // thousand) + ' thousand, ' + int_to_en(num % thousand)

    if (num < billion):
        if (num % million) == 0: return int_to_en(num // million) + ' million'
        else: return int_to_en(num // million) + ' million, ' + int_to_en(num % million)

    if (num < trillion):
        if (num % billion) == 0: return int_to_en(num // billion) + ' billion'
        else: return int_to_en(num // billion) + ' billion, ' + int_to_en(num % billion)

    if (num % trillion == 0): return int_to_en(num // trillion) + ' trillion'
    else: return int_to_en(num // trillion) + ' trillion, ' + int_to_en(num % trillion)

    raise AssertionError('num is too large: %s' % str(num))
    
if __main__ == '__name__':
   
    number = int(input("Enter Number"))    
    print(int_to_en(number))
