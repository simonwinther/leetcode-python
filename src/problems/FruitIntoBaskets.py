from typing import List


def totalFruit(fruits: List[int]) -> int:
    """
    :param fruits:
    :return:
    You are visiting a farm that has a single row of fruit trees arranged from left to right.
    The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

    You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

    You only have two baskets, and each basket can only hold a single type of fruit.
    There is no limit on the amount of fruit each basket can hold.
    Starting from any tree of your choice, you must pick exactly one fruit from every tree
    (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.

    Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
    Given the integer array fruits, return the maximum number of fruits you can pick.
    """
    windowStart: int = 0
    windowEnd: int = 0
    maxNumFruits: int = 0
    fruitBaskets = dict()

    while windowStart <= windowEnd < len(fruits):
        if fruits[windowEnd] not in fruitBaskets:
            fruitBaskets[fruits[windowEnd]] = 1
        else:
            fruitBaskets[fruits[windowEnd]] += 1

        while len(fruitBaskets) > 2:
            fruitBaskets[fruits[windowStart]] -= 1
            if fruitBaskets[fruits[windowStart]] == 0:
                del fruitBaskets[fruits[windowStart]]
            windowStart += 1
        maxNumFruits = max(maxNumFruits, windowEnd - windowStart + 1)
        windowEnd += 1
    return maxNumFruits


print(totalFruit([1, 2, 3, 2, 2]))
