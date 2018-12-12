# Uses python3
import sys
from collections import namedtuple
import operator
import random

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):

    points = []

    if len(segments) == 0:
        return points

    # sort segments [a,b] by a
    sortedSegments = sorted(segments, key=operator.itemgetter(0))

    # print('init', sortedSegments)

    while sortedSegments:

        overlappingSegments = []
        overlappingSegmentsTracker = []
        # check all segments against segment 0 for overlap
        # print('len(sortedSegments)', len(sortedSegments))
        for j in range(1, len(sortedSegments)):
            # print('check', sortedSegments[j][0], '<=', sortedSegments[0][1], '?')
            if(sortedSegments[j][0] <= sortedSegments[0][1]):
                # print(sortedSegments[j])
                overlappingSegments.append(sortedSegments[j])
                overlappingSegmentsTracker.append(j)
                # print('len(overlappingSegments)', len(overlappingSegments))
            else:
                break

        # print('overlap', overlappingSegments)
        # print('len overlap', len(overlappingSegments))
        # print('overlappingSegmentsTracker', overlappingSegmentsTracker)

        # if no overlapping segments
        if len(overlappingSegments) > 0:
            possiblityA = sortedSegments[0][1]
            del sortedSegments[0]
            # append first point
            possiblityB = sortedSegments[0][1]
            points.append(min(possiblityA, possiblityB))
            for k in overlappingSegmentsTracker:
                del sortedSegments[k-1]
            points = points + optimal_points(sortedSegments)
            return points
        else:
            points.append(sortedSegments[0][1])
            del sortedSegments[0]
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
