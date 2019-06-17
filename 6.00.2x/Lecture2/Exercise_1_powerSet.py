
from Num_and_Binary import *
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            # print(num_to_Binary(i >> j))
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo

items = ['a','b','c']
# result = powerSet(items)
# for i in result:
#     print(i)

def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list
        of which item(s) are in each bag.
    """
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        items2 = items.copy()
        for j in range(N):
            if (i >> j) % 2 == 1:
                combo.append(items[j])
                items2.remove(items[j])
        n = len(items2)
        for i in range(2**n):
            combo2 = []
            for j in range(n):
                if (i >> j) % 2 == 1:
                    combo2.append(items2[j])
            yield (combo,combo2,)
result = yieldAllCombos(items)
for i in result:
    print(i)
