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
    assert generate_prime_factors(3, []) == [3]  # test "3" input returns "3" in the factors array

def test_enter_4_returns_2_2():
    assert generate_prime_factors(4, []) == [2,2]  # test "4" input returns "2,2" in the factors array

def test_enter_6_returns_2_3():
    assert generate_prime_factors(6, []) == [2,3]  # test "6" input returns "2,3" in the factors array

def test_enter_8_returns_2_2_2():
    assert generate_prime_factors(8, []) == [2,2,2]  # test "8" input returns "2,2,2" in the factors array

def test_enter_9_returns_3_3():
    assert generate_prime_factors(9, []) == [3,3]  # test "9" input returns "3,3" in the factors array

def test_enter_5_returns_5():         # as an aside to test 5 as a prime value
    assert generate_prime_factors(5, []) == [5]  # test "5" input returns "5" in the factors array