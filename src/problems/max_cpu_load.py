from heapq import *


class job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    def __lt__(self, other):
        return self.end < other.end


def find_max_cpu_load(jobs):
    jobs.sort(key=lambda x: x.start)
    max_cpu_load, current_load = 0, 0
    min_heap = []

    for j in jobs:
        while len(min_heap) > 0 and j.start >= min_heap[0].end:
            current_load -= min_heap[0].cpu_load
            heappop(min_heap)
        heappush(min_heap, j)
        current_load += j.cpu_load
        max_cpu_load = max(max_cpu_load, current_load)
    return max_cpu_load


def main():
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(1, 4, 3), job(2, 5, 4), job(7, 9, 6)])))
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(6, 7, 10), job(2, 4, 11), job(8, 12, 15)])))
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(1, 4, 2), job(2, 4, 1), job(3, 6, 5)])))


main()
