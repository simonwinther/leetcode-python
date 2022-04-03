from typing import List


def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
    def dfs(node, path):
        if node == len(graph) - 1:
            paths.append(path)
            return
        for neighbor in graph[node]:
            dfs(neighbor, path + [neighbor])

    paths = []
    dfs(0, [0])
    return paths
