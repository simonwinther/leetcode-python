from typing import List
from collections import defaultdict, deque


def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    neighbors = defaultdict(list)
    for n1, n2 in edges:
        neighbors[n1].append(n2)
        neighbors[n2].append(n1)

    def dfs(node, end, seen):
        if node == end:
            return True
        if node in seen:
            return False

        seen.add(node)
        for n in neighbors[node]:
            if dfs(n, end, seen):
                return True
        return False

    seen = set()
    return dfs(source, destination, seen)


print(validPath(n=3, edges=[[0, 1], [1, 2], [2, 0]], source=0, destination=2))
print(validPath(n=6, edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source=0, destination=5))
