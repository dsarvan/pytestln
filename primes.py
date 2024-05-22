#!/usr/bin/env python
# File: primes.py
# Name: D.Saravanan
# Date: 03/05/2024

""" prime module """

import math


def is_prime(number: int) -> bool:
    """
    function should take a number and return True if it's prime and False otherwise

    A prime number is any natural number greater than 1 that is only divisible
    by 1 and itself.

    We can check by dividing numbers between 2 and the square root of the number.

    If there's no remainder from the division, then it has a divisor
    that's neither 1 nor itself, and therefore not prime.

    If it does not find a divisor in the iteration, then it must be prime.

    """

    if number < 2:
        return False
    for n in range(2, math.isqrt(number) + 1):
        if number % n == 0:
            return False
    return True


def is_natural(number: int):
    """natural number"""
    if number > 0:
        is_prime(number)
        return True
    return False


def sum_primes(numbers):
    """sum prime numbers"""
    return sum((x for x in numbers if is_prime(x)))
