"""
The digital root (also repeated digital sum) of a natural number in 
a given number base is the (single digit) value obtained by an iterative 
process of summing digits, on each iteration using the result from the previous 
iteration to compute a digit sum. The process continues until a single-digit number 
is reached. - https://en.wikipedia.org/wiki/Digital_root

> digital_root(52)
// 7
(5 + 2)
"""


def digital_root(n):
    return (n - 1) % 9 + 1 if n else 0
