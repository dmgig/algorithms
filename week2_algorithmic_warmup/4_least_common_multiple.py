# Uses python2
import sys
import random

def greatest_common_divisor_fast(a, b):
    if b == 0:
        return a
    divisor = a % b
    return greatest_common_divisor_fast(b, divisor)

def least_common_multiple_fast(a, b):
    gcd = greatest_common_divisor_fast(a, b)
    return long((a*b)/gcd)

if __name__ == '__main__':
    input = sys.stdin.read();
    a, b = map(int, input.split())
    print(least_common_multiple_fast(a, b))
