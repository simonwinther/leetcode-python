from typing import List
from collections import deque, defaultdict


def findItinerary(tickets: List[List[str]]) -> List[str]:
    flights = defaultdict(list)
    for src, dest in tickets:
        flights[src].append(dest)
    for key in flights.keys():
        flights[key] = deque(sorted(flights[key]))
    result = deque()
    stack = ["JFK"]
    while len(stack) > 0:
        src = stack[-1]
        while src in flights:
            dest = flights[src].popleft()
            if len(flights[src]) == 0:
                del flights[src]
            stack.append(dest)
            src = dest
        result.appendleft(stack.pop())
    return list(result)


print(findItinerary(tickets=[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
