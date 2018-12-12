#Uses python3

import sys
import math

def max_dot_product(a, b):
    #write your code here
    res = 0
    adsCnt = len(b)
    slotsCnt = n
    maxFill = max(adsCnt, slotsCnt)
    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)
    for i in range(maxFill):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
