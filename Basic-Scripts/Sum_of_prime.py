def is_prime(a): #function to check whether number is prime 
    return all(a % i for i in range(2, a))

def sum_of_primes(n): 
    sum = 0
    x = 2
    while x < n:
        if is_prime(x):
            sum = sum + x
        x = x+1
    return sum

def main():  #main function definition
    print("Enter value upto which sum of primes to be calculated:")
    n=int(input())
    print(sum_of_primes(n))

if __name__ == '__main__':  
    main()