import random  # Importing random for generating random integers
import time  # Importing time to measure the duration of algorithm execution

#Function to decompose (n-1) into 2^k * m where m is odd.
def find_M_and_K(n): 
    
    k = 0  # Initialize exponent k
    m = n - 1  # Start with m as n - 1
    while m % 2 == 0:  # Keep dividing m by 2 until it's odd
        m //= 2
        k += 1
    return m, k  # Return the odd m and exponent k

#Function to compute x = a^m % n for a random a.
def compute_x(n): 
    m = find_M_and_K(n)[0]  # Get the odd number m
    a = random.randint(2, n - 2)  # Generate a random integer a
    x = pow(a, m, n)  # Compute x = a^m % n
    return x

#Function to repeatedly square x and check conditions for primality.
def squaring_x(x, n):
    k = find_M_and_K(n)[1]  # Get the exponent k
    for _ in range(0, k): 
        if x == n - 1:
            return True  # Condition met for probable primality
        else:
            x = pow(x, 2, n)  # Square x modulo n
    return False  # If no conditions met, return False

# Implementation of the Miller-Rabin primality test for an odd integer n.
def miller_rabin(n):
    if n < 1:
        return False  # Negative numbers are not prime
    if n in [2, 3]:  # Check if n is 2 or 3 (primes)
        return True
    if n <= 1 or n % 2 == 0:
        return False  # Check if n is less than 2 or even (hence composite)
    x = compute_x(n)
    if x == 1:
        return True  # Condition for probable primality
    else: 
        return squaring_x(x, n)  # Further squaring and checks for primality
    
# Function to run the Miller-Rabin test multiple times to increase accuracy.
def miller_rabin_multiple_iterations(n, k): 
    start_time = time.time()  # Start time measurement
    for _ in range(k):  # Perform k iterations
        if not miller_rabin(n):
            duration = time.time() - start_time
            return False  #  composite
        
    duration = time.time() - start_time
    print("Miller Rabin used:", duration, "seconds")
    return True  # probably prime

def main():
    k = 50  # Number of iterations for Miller-Rabin test
    
    # Two large numbers (probably primes) to be tested
    p1 = 8957134963543217186967243359836050763300489442081745226747166181037596091286404632293693442399781881628965122280499929432247726250010005348714259936358949 
    p2 = 11488841940613266549967413190260501514413031301429045878897967120544950008794839158798344062017314672573618361100274319784350687597555132597915410951028313
    
    # Running the Miller-Rabin test on the two numbers
    miller_rabin_multiple_iterations(p1, k)
    miller_rabin_multiple_iterations(p2, k)
    
# Ensures main is executed when the script is run directly
if __name__ == "__main__":
    main()
