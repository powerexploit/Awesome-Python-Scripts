# using python 3.7
def rec_fib( num ):
    if num == 0 or num == 1:
        return num

    return rec_fib( num-1 ) + rec_fib( num-2 )

# tests
num = int( input( 'Enter with a positive integer: ' ) )
print( rec_fib(num) )