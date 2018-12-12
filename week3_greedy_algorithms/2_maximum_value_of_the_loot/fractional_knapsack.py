# Uses python3
import sys
import random
import math

def get_optimal_value(capacity, weights, values):
    curValue = 0.
    curWeight = 0
    valueByWeight = []

    # calc valueByWeight
    for i in range(len(values)):
        valueByWeight.append(values[i] / weights[i])
    # sort by values (reversed)
    valueByWeight, values, weights = zip(*sorted(zip(valueByWeight, values, weights), reverse=True))
    valueByWeight = list(valueByWeight)
    values = list(values)
    weights = list(weights)
    # sort by valByWeight w/in value
    # print(valueByWeight, values, weights)
    for x in range(len(valueByWeight)):
        checkWeight = curWeight + weights[x]
        # check overcapacity and fill w/ fraction if over
        # print(checkWeight, capacity)
        if(checkWeight >= capacity):
            spaceLeftOver = capacity - curWeight
            pctToFill = spaceLeftOver / weights[x]
            curValue = curValue + (values[x] * pctToFill)
            curWeight = curWeight + (weights[x] * pctToFill)
            break
        else:
            curValue = curValue + values[x]
            curWeight = curWeight + weights[x]

    return curValue

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]

    # while 1:
    #     n = random.randint(1,10**3)
    #     capacity = random.randint(1, 2 * 10**6)
    #     values = []
    #     weights = []
    #     for i in range(n):
    #         values.append(random.randint(1, 2 * 10**6))
    #         weights.append(random.randint(1, 2 * 10**6))
    #
    #     opt_value = get_optimal_value(capacity, weights, values)
    #     print(capacity)
    #     print("{:.10f}".format(opt_value))


    opt_value = get_optimal_value(capacity, weights, values)
    # print(capacity, values, weights)
    print("{:.10f}".format(opt_value))
