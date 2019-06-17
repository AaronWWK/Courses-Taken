class Food(object):
    def __init__(self,n,v,w):
        self.name = n
        self.value = v
        self.calories = w
    def getValue(self):
        return self.value
    def getCost(self):
        return self.calories
    def getdensity(self):
        return self.getValue() / self.getCost()
    def __str__(self):
        return self.name + ': <' + str(self.name) + ',' \
                + str(self.calories) + '>'
def buildMenu(names, values, claories):
    mune = []
    for i in range(len(values)):
        mune.append(Food(names[i], values[i], calories[i]))
        """names, values, calories lists of same length.
           name a list of strings
           values and calories lists of numbers
           returns list of Foods"""
def greedy(items, maxCost, keyFunction):
    itemsCopy = sorted(items, key = keyFunction, reverse = True)
    result = []
    totalValue, totalCost = 0.0 , 0.0
    for i in range(len(itemsCopy)):
        if (totalCost + itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)

def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken =', val)
    for item in takem:
        print('     ', item)
def testGreedys(foods, maxUnits):
    print('Use greedy by value to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.getValue)
