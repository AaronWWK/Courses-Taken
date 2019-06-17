def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None """
    # Your code here

    listKey = []
    for item in list:
        listKey.append(list.count(item))
    # print(listKey)
    dictA = dict(zip(listKey,list))

    # list = [3,9,5,3,5,3]
    # listnum = []
    # for i in list:
    #     listnum.append(0)
    #
    # dict = dict(zip(list,listnum))
    # for item in list:
    #     dict[item] += 1
    # print(str(dict))
    """
    #将两个list合成dict
    # 1、现在有两个列表，list1 = ['key1','key2','key3']和list2 = ['1','2','3']，把他们转为这样的字典：{'key1':'1','key2':'2','key3':'3'}
    # >>>list1 = ['key1','key2','key3']
    # >>>list2 = ['1','2','3']
    # >>>dict(zip(list1,list2))
    # {'key1':'1','key2':'2','key3':'3'}
    """
    listKey2 =[]
    for keys in dictA.keys():
        listKey2.append(keys)
    for i in listKey2:
        if i % 2 == 0:
            del dictA[i]
    # print(str(dictA ))
    if dictA == {}:
        return None

    else:
        listKeyMax = []
        for values in dictA.values():
            listKeyMax.append(values)
        return max(listKeyMax)
# list = [3,9,5,3,5,3]
list = [2,2,4,4]
print(largest_odd_times(list))
