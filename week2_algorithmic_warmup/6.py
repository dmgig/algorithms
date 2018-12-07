# Uses python3
import sys
import random

def fibonacci_sum_last_digit(n):
    n = (n % 60)
    sum = 0
    for i in range(0, n+1):
        fibo = fibonacci_number_fast(i)
        sum = (sum + (fibo % 10))
    return sum % 10

def fibonacci_number_fast(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    store = [0,1]
    for j in range(2, n+1):
        store.append(store[len(store)-2] + store[len(store)-1])
    return store.pop()

# if __name__ == '__main__':
#
#     input = sys.stdin.read()
#     n = int(input)
#
#     n = random()
#
#     print(fibonacci_sum_last_digit(n))

def fibonacci_sum_last_digit_stress_test():
    while 1:
        n = random.randint(0,10**18)
        fibonacci_sum_last_digit(n)
        print("FINAL: %i %i" % (n, fibonacci_sum_last_digit(n)))

fibonacci_sum_last_digit_stress_test()
