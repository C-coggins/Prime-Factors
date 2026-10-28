''' Test Prime Suite

test_prime.py
Chris Cogggins

this is the suite of tests for the implmentation of test driven development for the prime factor generator progrma
used with:
prime.py

'''
from prime import validate_type             # import the validate function from the main program
from prime import generate_prime_factors    # import the generate prime function from the main program

def test_reject_string():
    validate_type(str(6))           # string test case

def test_reject_float():
    validate_type(float(6))         # Float test case

def test_reject_negative():
    validate_type(int(-6))          # Negative test case

def test_enter_1_returns_empty():
    assert generate_prime_factors(1,[]) == []   #test "1" input returns an empty factors array

def test_enter_2_returns_2():
    assert generate_prime_factors(2, []) == [2]  # test "2" input returns "2" in the factors array

def test_enter_3_returns_3():
    assert generate_prime_factors(3, []) == [3]  # test "2" input returns "2" in the factors array