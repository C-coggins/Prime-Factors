
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


def main():

    number = 5                  # variable from which to generate the prime factors
    validate_type(number)           # call Validate_type function to verify the variable is a positive integer

if __name__ == '__main__':
    main()

