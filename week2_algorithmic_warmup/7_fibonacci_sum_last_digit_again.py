# Uses python3
import sys
import random

def fibonacci_sum_last_digit_again(m, n):
    n = (n % 60)
    m = (m % 60)
    if(m > n):
        n = n + 60
    sumM = 0
    sumN = 0
    for i in range(0, n + 1):
        fibo = fibonacci_number_fast(i)
        if(i >= m):
            sumM = (sumM + (fibo % 10))
    return sumM % 10

def fibonacci_number_fast(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    store = [0, 1]
    for j in range(2, n + 1):
        store.append(store[len(store) - 2] + store[len(store) - 1])
    return store.pop()

if __name__ == '__main__':

    input = sys.stdin.read()
    m, n = map(int, input.split())

    print(fibonacci_sum_last_digit_again(m, n))
