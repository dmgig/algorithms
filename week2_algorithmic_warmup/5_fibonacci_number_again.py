# Uses python3
import sys
import random

def fibonacci_number_again(n, m):
    for i in range(0, n):
        f = fibonacci_number_fast(i)
        print(f)
        print(f % m)
        if(f != 0 and f % m == 0):
            break
    fnum = n % ((i - 1) * 2)
    return fibonacci_number_fast(fnum) % m

def fibonacci_number_fast(n):
    if(n < 2):
        return n
    store = [0,1]
    for j in range(1, n):
        store.append(store[j-1] + store[j])
    return store[j-1] + store[j]

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(fibonacci_number_again(n, m))
