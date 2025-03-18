# Importing the Miller-Rabin primality test functions 
from MillerRabin import *

def generate_odd_number(bits):
    """
    Function to generate a random odd number with a specified number of bits.
    """
    start_time = time.time()  # Start measuring time
    # Define the smallest and largest numbers with the given bit length
    smallest = 2**(bits-1)
    largest = 2**bits - 1

    # Loop to generate a random odd number within the specified range
    while True:
        number = random.randrange(smallest, largest + 1)
        # Check if the number is odd
        if number % 2 != 0:
            duration = time.time() - start_time  # Measure duration
            return number, duration  # Return the odd number and time taken

def generate_and_test(bits, rounds):
    """
    Function to generate an odd number and test its primality.
    """
    # Generate an odd number
    number, duration = generate_odd_number(bits)
    # Test the number for primality; regenerate if not probable prime
    while not miller_rabin_multiple_iterations(number, rounds):
        number, duration = generate_odd_number(bits)
    # Print the probable prime number and generation time
    print(f"{number} is probably prime.")
    print(f"Generating number time: {duration:.12f} seconds.")
    return number  # Return the probable prime number

def generate_two_primes_and_measure_time(bits, rounds):
    """
    Function to generate two probable prime numbers and measure the time taken.
    """
    # Generate and test the first number, measuring the time taken
    start_time = time.time()
    first_number = generate_and_test(bits, rounds)
    first_duration = time.time() - start_time  # Time for first number

    print(f"Time taken to generate and test the first number: {first_duration} seconds.\n")

    # Generate and test the second number, measuring the time taken
    start_time = time.time()
    second_number = generate_and_test(bits, rounds)
    second_duration = time.time() - start_time  # Time for second number

    print(f"Time taken to generate and test the second number: {second_duration} seconds.")

    # Return the generated numbers and the durations
    return first_number, second_number, first_duration, second_duration

def main():
    """
    Main function to generate two 512-bit probable prime numbers.
    """
    bits = 512  # Number of bits for the prime numbers
    rounds = 50  # Number of rounds for the Miller-Rabin primality test
    # Generate the two numbers and measure time
    p1, p2, t1, t2 = generate_two_primes_and_measure_time(bits, rounds)

# Ensures the main function is called when the script is run directly
if __name__ == "__main__":
    main()
