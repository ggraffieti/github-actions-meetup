import math


def addition(first_number, second_number, *other_numbers):
    """
    Calculate the sum between two or more numbers
    :param first_number: the first numner to sum
    :param second_number: the second number to sum
    :param other_numbers: additional other numbers
    :return: the sum between the given numbers
    """
    sum = first_number + second_number
    for n in other_numbers: 
        sum += n
    return sum 


def multiplication(first_number, second_number, *other_numbers):
    """
    Calculate the product between the given numbers
    :param first_number: the first number to multiply
    :param second_number: the second number to multiply
    :param other_numbers: additional numbers to multiply
    :return: the product between the given numbers
    """
    product = first_number * second_number
    for n in other_numbers: 
        product *= n
    return product


def subtraction(first_number, second_number):
    """
    Subtract the second number to the first number
    :param first_number: The base number
    :param second_number: The number to subtract to the base number
    :return: The subtraction between the two numbers
    """
    return first_number - second_number


def division(first_number, second_number):
    """
    Calculate the division between the two numbers
    :param first_number: the divident
    :param second_number: the divisor
    :return: the quotient between the divident and the divisor
    """
    return first_number / second_number


def power(base, exponent):
    """
    Calculate the power between the given base and exponent.
    :param base: the base of the power
    :param exponent: the exponent of the number
    :return: the power base^exponent
    """
    if exponent == 0: 
        return 1
    if exponent == 1: 
        return base
    if exponent == 2: 
        return multiplication(base, base)
    else: 
        return multiplication(base, power(base, exponent - 1))


def square_root(number):
    if number < 0:
        raise ArithmeticError("Square root of a negative number")
    if number == 0:
        return 0
    else:
        guess = number / 2
        for _ in range(10):
            guess = (1/2) * (guess + (number / guess))
        return guess


if __name__ == "__main__": 
    print(addition(5, 6, 9, 10))
    print(multiplication(5, 6))
    print(subtraction(5, 6))
    print(division(5, 6))
    print(power(5, 3))
    print(square_root(15))
