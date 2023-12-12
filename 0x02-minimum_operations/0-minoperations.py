#!/usr/bin/env python3
"""
Calculates the fewest number of operations needed
To result in exactly n H characters in the file
"""


def minOperations(n):
    """
    Returns an integer
    If n is impossible to achieve, returns 0
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
