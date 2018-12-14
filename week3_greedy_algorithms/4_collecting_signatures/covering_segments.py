# Uses python3
import sys
from collections import namedtuple
import operator
import random

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):

    points = []
    sortedSegments = sorted(segments , key=lambda k: int(str(k[0]) + str(k[1])))

    cnt = 0
    while sortedSegments:
        overlappingSegments = []
        overlappingSegmentsTracker = []
        point_finder = sortedSegments[0]
        new_point = sortedSegments[0][1]
        sortedSegmentsCopy = sortedSegments.copy()
        for i in range(1, len(sortedSegmentsCopy)):
            if(sortedSegmentsCopy[i][0] <= sortedSegmentsCopy[0][1] and
               sortedSegmentsCopy[i][0] <= point_finder[1]):
                point_finder = [
                    max(point_finder[0], sortedSegments[i][0]),
                    min(point_finder[1], sortedSegments[i][1])
                ]
                new_point = point_finder[1]
                overlappingSegmentsTracker.append(i)
            else:
                break

        for k in sorted(overlappingSegmentsTracker, reverse=True):
            del sortedSegments[k]
        del sortedSegments[0]

        if len(points) == 0 or new_point != points[len(points)-1]:
            points.append(new_point)

    return points

if __name__ == '__main__':

    # stdin run
    ###########
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))

    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')

    # stresstest run
    ################
    # while 1:
    #
    #     n = random.randint(1,100)
    #     data = []
    #     for i in range(n):
    #         possibleStart = random.randint(0,10**9)
    #         possibleEnd = random.randint(0,10**9)
    #         data = data + [min(possibleStart, possibleEnd), max(possibleStart, possibleEnd)]
    #
    #     segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    #     # print('----')
    #     # print('input', n, segments)
    #     #
    #     #
    #     # print('----')
    #     points = optimal_points(segments)
    #     print(len(points))
    #     for p in points:
    #         print(p, end=' ')
    #     print('----')
