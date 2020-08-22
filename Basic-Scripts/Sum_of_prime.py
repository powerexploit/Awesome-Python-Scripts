def is_prime(is_a_prime):
    '''Function 
       to check whether the number is prime or not.'''
    return all(is_a_prime % i for i in range(2, is_a_prime))

def sum_of_primes(number):
    '''Function 
       to get the total sum of the prime numbers in the given range.'''
    sum = 0
    is_a_prime = 2
    while is_a_prime < number:
        if is_prime(is_a_prime):
            sum = sum + is_a_prime
        is_a_prime = is_a_prime+1
    return sum

if __name__ == '__main__':  
    print("Enter value upto which sum of primes to be calculated:")
    number=int(input())
    print(sum_of_primes(number))
