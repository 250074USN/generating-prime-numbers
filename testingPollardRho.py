import time  # Importing the time module to measure execution time
from PollardRho import pollard_rho  # Importing the Pollard Rho factorization function from a custom module

#Function to test the Pollard Rho algorithm on (p-1)/2.  
def testPollard_rhoPminus1(p):

    n = (p - 1) / 2  # Calculating (p-1)/2

    # Check if n is a decimal (not an integer)
    if not n.is_integer():
        print("n is not an integer, Pollard Rho cannot proceed.")
        return

    n = int(n)  # Convert n to an integer
    start_time = time.time()  # Start time measurement
    factor = pollard_rho(n)  # Factorizing n using Pollard Rho
    duration = time.time() - start_time  # Calculating the duration of the factorization process
    
    # Output 
    if factor is not None:
        print("P = ", p)
        print(f"A non-trivial factor of (p-1)/2 : {factor}")
        print(f"Pollard Rho used: {duration:.15f} seconds\n")
    else:
        print(f"Failed to find a factor for {n}")

def main():
    """
    Main function to apply the testPollard_rhoPminus1 function on two large primes.
    """
    # Two large prime numbers
    p1 = 8957134963543217186967243359836050763300489442081745226747166181037596091286404632293693442399781881628965122280499929432247726250010005348714259936358949 
    p2 = 11488841940613266549967413190260501514413031301429045878897967120544950008794839158798344062017314672573618361100274319784350687597555132597915410951028313

    # Testing Pollard Rho on (p1-1)/2 and (p2-1)/2
    testPollard_rhoPminus1(p1)  
    testPollard_rhoPminus1(p2)

# Ensuring that the main function is executed when the script is run directly
if __name__ == "__main__":
    main()
