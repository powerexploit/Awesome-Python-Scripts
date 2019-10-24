def maxNumber( num1, num2 ):
    '''
    The brief:
        As input we have 2 int numbers. To pick the greater without if-else clauses we have
        to made a simple account.
        - To begin we have to calculate sum the two numbers;
        - Then we plus the result with the absolute value of the difference between num1 and num2;
        - Adding the absolute value of difference to the result, we've completed the smallest number to
            reach in the greater value;
        - The the total value of the sum is (num1+num2)+(the complement to the smaller be the equal to the greater),
            and this is equal to the greater two times;
        - At least we return the floor division of the sum by 2
    '''
    return ( num1 + num2 + abs( num1 - num2 ) ) // 2

# Now you have to construct the tests. Let's Hack. :)