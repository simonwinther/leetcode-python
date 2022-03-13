from typing import List


def floodFill(image: List[List[int]], sr: int, sc: int, newColour: int) -> List[List[int]]:
    R, C = len(image), len(image[0])

    colour = image[sr][sc]

    if colour == newColour:
        return image

    def dfs(r, c):
        if image[r][c] == colour:
            image[r][c] = newColour
            if r >= 1:
                dfs(r - 1, c)
            if r + 1 < R:
                dfs(r + 1, c)
            if c >= 1:
                dfs(r, c - 1)
            if c + 1 < C:
                dfs(r, c + 1)

    dfs(sr, sc)
    return image


print(floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, newColour=2))
