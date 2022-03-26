from typing import List
from collections import defaultdict


def findCircleNum(isConnected: List[List[int]]) -> int:
    if not isConnected:
        return 0
    n = len(isConnected)
    visited = set()

    def dfs(p):
        for q, adj in enumerate(isConnected[p]):
            if adj == 1 and q not in visited:
                visited.add(q)
                dfs(q)

    counter = 0
    for i in range(n):
        if i not in visited:
            dfs(i)
            counter += 1
    return counter


print(findCircleNum(isConnected=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(findCircleNum(isConnected=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
