# Uses python3
import sys
import math
import random

def fibonacci_number_again(n, m):
    fnum = n % get_pisano_period(m)
    return fibonacci_number_fast(fnum) % m

def get_pisano_period(m):
    a = 0
    b = 1
    c = a + b;
    for i in range(0, m * m):
        c = (a + b) % m
        a = b
        b = c
        if a == 0 and b == 1:
            return i + 1;

def fibonacci_number_fast(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    store = [0,1]
    for j in range(2, n+1):
        store.append(store[len(store)-2] + store[len(store)-1])
    return store.pop()

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    # print(get_pisano_period(m))
    print(fibonacci_number_again(n, m))
