#!/usr/bin/env python
# File: test_primes.py
# Name: D.Saravanan
# Date: 03/05/2024

""" prime module test """


from primes import is_prime
from primes import is_natural
from primes import sum_primes


def test_prime_number():
    assert is_prime(1) is False
    assert is_prime(4) is False
    assert is_prime(5) is True


def test_natural_number():
    assert is_natural(0) is False
    assert is_natural(6) is True


def test_prime_number_sum():
    assert sum_primes([]) == 0
    assert sum_primes([11, 15, 17, 18, 20, 100]) == 28
