from typing import List


def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    stack = []

    for pos, vel in sorted(zip(position, speed))[::-1]:
        dist = target - pos
        if not stack:
            stack.append(dist / vel)
        elif dist / vel > stack[-1]:
            stack.append(dist / vel)
    return len(stack)


print(carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]))
print(carFleet(target=10, position=[3], speed=[3]))
print(carFleet(target=100, position=[0, 2, 4], speed=[4, 2, 1]))
