# Uses python3
import sys
import random
import math

# def get_optimal_value(capacity, weights, values):
#     curValue = 0.
#     curWeight = 0
#     sack = []
#     # sort by values (reversed)
#     values, weights = zip(*sorted(zip(values, weights), reverse=True))
#     values = list(values)
#     weights = list(weights)
#     # sort by weights w/in values
#     orderedValuesDict = {}
#     for i in range(len(values)):
#         if values[i] in orderedValuesDict:
#             orderedValuesDict[values[i]].append(weights[i])
#         else:
#             orderedValuesDict[values[i]] = [weights[i]]
#     for k in orderedValuesDict:
#         # sort by weight
#         sortedWeights = sorted(orderedValuesDict[k])
#         # print('sortedWeights', sortedWeights)
#         # fill sack
#         for x in range(len(sortedWeights)):
#             checkWeight = curWeight + sortedWeights[x]
#             # check overcapacity and fill w/ fraction if over
#             if(checkWeight > capacity):
#                 spaceLeftOver = checkWeight - curWeight
#                 pctToFill = spaceLeftOver / sortedWeights[x]
#                 curValue = curValue + (k * pctToFill)
#                 curWeight = curWeight + (sortedWeights[x] * pctToFill)
#             else:
#                 curValue = curValue + k
#                 curWeight = curWeight + sortedWeights[x]
#             # print('curValue, curWeight', curValue, curWeight)
#
#     return curValue


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
