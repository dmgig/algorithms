# Uses python3
import sys
import random

def fibonacci_number_again(n, m):
    print(get_pisano_period(m))
    fnum = n % get_pisano_period(m)
    return fibonacci_number_fast(fnum)

def get_pisano_period(m):
    A, B, i = [], [], 0
    while 1:
        f = (fibonacci_number_fast(i) % m) % 10
        A.append(f)
        if i > 0:
            B.append(f)
        if A[0:len(B)] != B:
            B = []
        if len(A) / 2 == len(B):
            return int(len(B))
        i = i + 1

# def fibonacci_number_again(n, m):
#     # n = (n % 61)
#     # # sum = 0
#     for i in range(0, n+1):
#         fibo = fibonacci_number_fast(i % 60)
#         # fibo = fibo % 10
#         print(fibo % m)
#     # return fibonacci_number_fast(n) % m

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
    print(fibonacci_number_again(n, m))
