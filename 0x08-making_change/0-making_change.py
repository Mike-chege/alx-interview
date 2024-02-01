#!/usr/bin/python3
"""
Determining the fewest number of coins
Needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    Coins is a list of the values of the coins in your possession
    The value of a coin will always be an integer greater than 0
    """
    temp_value = 0
    coins.sort(reverse=True)

    if total < 0:
        return 0

    for coin in coins:
        if total % coin <= total:
            temp_value += total // coin
            total = total % coin

    return temp_value if total == 0 else -1
