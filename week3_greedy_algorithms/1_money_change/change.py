# Uses python3

'''
Problem Description

Task. The goal in this problem is to  nd the minimum number of coins needed to change the input value (an integer) into coins with denominations 1, 5, and 10.

Input Format. The input consists of a single integer m.

Constraints. 1 ≤ 0 ≤ 10**3.

Output Format. Output the minimum number of coins with denominations 1, 5, 10 that changes m.

Sample 1.
Input: 2
Output: 2 -- 2 = 1 + 1.

Sample 2.
Input: 28
Output: 6 -- 28 = 10 + 10 + 5 + 1 + 1 + 1.
'''

import sys
import math
import random

def calc_coins(money, coinValue):
    coinCount = math.floor(money/coinValue)
    moneyRemaining = money % coinValue
    return [moneyRemaining, coinCount]

def get_change(m):
    moneyRemaining = m
    coinCountTotal = 0

    coinValues = [10, 5, 1]
    for i in range(3):
        moneyRemaining, coinCount = calc_coins(moneyRemaining, coinValues[i])
        # print('idx:', i, 'val:', coinValues[i], moneyRemaining, coinCount)
        coinCountTotal = coinCountTotal + coinCount

    return coinCountTotal

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
    # while 1:
    #     m = random.randint(1,10**3)
    #     print(get_change(m))
