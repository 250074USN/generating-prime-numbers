import random  #for generating random numbers 
from math import gcd  # Importing gcd function for computing the greatest common divisor
from MillerRabin import miller_rabin_multiple_iterations  # Importing the Miller-Rabin primality test function from MillerRabinCandidate8000

# The function used in Pollard's Rho algorithm.
def f(x, n, c):
    # Function to calculate the next value in the sequence for Pollard's Rho
    return (x*x + c) % n

# Pollard's Rho Algorithm for integer factorization.
def pollard_rho(n, iterations=1000):
    # Check if the number is probably prime using the Miller-Rabin test
    if miller_rabin_multiple_iterations(n, 50):
        print(f"{n} is probably a prime.")
        return None  # if n is probably prime

    # Main loop for the Pollard Rho algorithm
    for i in range(1, iterations):
        x = random.randint(2, n - 1)  # Randomly selecting initial x
        y = x  # Setting y equal to x initially
        c = random.randint(1, n - 1)  # Randomly selecting c
        p = 1  # Initializing p, which will hold the factor when found

        # Loop to find a factor
        while p == 1:
            x = f(x, n, c)  # Update x 
            y = f(f(y, n, c), n, c)  # y moves twice as fast)
            p = gcd(abs(x - y), n)  # Calculate gcd of |x - y| and n

            # Check if a factor is found
            if p != 1 and p != n:
                return p  # the factor found

    return None  # no factor found 

def main():
    
    # A large prime number p
    p = 12301252854767350045152272645861329769989700540244628158625992836836641662232957808222527096009060905683795828439107590979480839199511064030630953712904903
    # large composiste to test
    n = p-1  # Setting n to p-1 for factorization
    factor = pollard_rho(n)  # Calling Pollard's Rho to factorize n
    
    # Output here
    if factor is not None:
        print(f"A non-trivial factor of {n} is {factor}")
    else:
        print(f"Failed to find a factor for {n}")

if __name__ == "__main__":
    main()
