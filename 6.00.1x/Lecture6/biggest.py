def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    num = 0
    k2 = ''
    for k,v in aDict.items():
        if len(v) > num:
            num = len(v)
            k2 = k
    return k2

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
print(biggest(animals))


##### the given answer
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = None
    biggestValue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestValue:
            result = key
            biggestValue = len(aDict[key])
    return result




def biggest(aDict):
    num = []
    big = ''
    for k in aDict.keys():
        num.append(len(aDict[k]))
    biggest = max(num)
    for k in aDict.keys():
        if len(aDict[k]) == biggest:
            big = k
    return big

print(biggest({'b': [1, 7, 5, 4, 3, 18, 10, 0], 'a': []}))
