# Uses python3
import sys
import math
import random

# def optimal_summands(n):
#     p = 0
#     k = []
#     while p < n:
#         print(abs((n/2)-p))
#         arrLen = math.floor(math.sqrt(abs((n-p)/2)-p)))
#         print('arrLen', arrLen)
#         if(len(k) == 0):
#             k2 = list(range(1, arrLen))
#         else:
#             k2 = list(range(k[len(k)-1], k[len(k)-1]+arrLen))
#         # print(int(math.floor(math.sqrt(n))))
#         k = k + k2
#         print('k', k)
#         p = sum(k)
#         if(p > n):
#             print('p',p)
#             fix = k.pop()
#             print('fix',fix)
#             prevSum = p - fix
#             print('prevSum',prevSum)
#             add = n - prevSum
#             print('add', add)
#             k[len(k)-1] = k[len(k)-1] + add
#     return k

def optimal_summands(n):
    k = []
    for i in range(1, n + 1):
        n = n - i
        if n <= i:
            k.append(n + i)
            break
        elif n == 0:
            k.append(i)
            break
        else:
            k.append(i)
    return k

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
    print(sum(summands))

    # stress test
    # while 1:
    #     exp = random.randint(1,3)
    #     n = random.randint(1,10**exp)
    #     slow = optimal_summands_slow(n)
    #     fast = optimal_summands(n)
    #     if slow == fast:
    #         print('TRUE')
    #     else:
    #         print('FALSE')
    #         break
