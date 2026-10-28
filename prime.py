
''' Prime Factor Generator:
Prime.py
Chris Coggins


This program will generate the prime factors of a given integer.
it is implemented using test driven development standards
'''


#validate whether the input is a functional positive integer
def validate_type(number):
    try:
        if type(number) != int or number <= 0:                              # is number not an integer or less than zero
            raise ValueError("Prime number must be a positive integer")     # raise exception
    except ValueError:
        print(f"{number} is not apositive integer")                                # print error message
    return number

def generate_prime_factors(number,factors):
    divisor = [2,3]

    for divisor in divisor:                             # use the same loop for prime value in the array
        test = number                                   #initialize test variable for iterative testing
        while test / divisor  >= 1:                     # while loop to interate values

            if test % divisor  == 0:                    # if the remainder = 0 then the number is divisable evenly
                factors.append(divisor)                 # append divisor to the factors list
            test = test / divisor                       # iterate test value by divisor if number has more than 2 prime factors


    return factors                          # return the factors variable to the main function


def main():

    number = 10                                         # variable from which to generate the prime factors
    factors = []                                            # variable to hold the prime factors
    validate_type(number)                                   # call Validate_type function to verify the variable is a positive integer
    factors = generate_prime_factors(number,factors)        # cal generate_prime_factors to calculate the factors for a given number
    print (f'the {number} has {factors} as prime factors')   # print the number and it's factors to the terminal

if __name__ == '__main__':
    main()

