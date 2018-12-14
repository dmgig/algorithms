#Uses python3

import sys
import math
import random

NEGINF = -999999999

def largest_number(D):
    global NEGINF
    res = ""
    while len(D) > 0:
        maxD = NEGINF
        for x in range(len(D)):
            if is_greater_than(D[x], maxD):
                maxD = D[x]
        res = res + str(maxD)
        del D[D.index(maxD)]
    return res

def is_greater_than(a, b):
    global NEGINF
    if a == NEGINF or b == NEGINF:
        return int(a) >= int(b)
    aa = int(str(a) + str(b))
    bb = int(str(b) + str(a))
    return aa >= bb

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

    # while 1:
    #     testArr = []
    #     for i in range(random.randint(1,100)):
    #         testArr.append(random.randint(1,10**3))
    #     print(largest_number(testArr))
