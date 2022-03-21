from typing import List
import bisect


def intervalIntersection(firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    for l in secondList:
        bisect.insort_left(firstList, l)

    result = []
    max_end = firstList[0][1]

    for start, end in firstList[1:]:
        if start > max_end:
            max_end = end
        else:
            if max_end <= end:
                result.append([start, max_end])
                max_end = end
            else:
                result.append([start, end])
    return result


print(intervalIntersection(firstList=[[0, 2], [5, 10], [13, 23], [24, 25]],
                           secondList=[[1, 5], [8, 12], [15, 24], [25, 26]]))
