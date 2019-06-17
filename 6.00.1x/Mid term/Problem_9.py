# def flatten(aList):
#     '''
#     aList: a list
#     Returns a copy of aList, which is a flattened version of aList
#     '''
    # aListcopy = aList[:]
    # for item in aListcopy:
    #     aList.remove(item)
    #     if type(item) == list:
    #
    #         for i in item:
    #             if type(i) == list:
    #                 aList.append(flatten(i))
    #
    #                 # if len(i) <= 1:
    #                 #     if type(i[0]) == list:
    #                 #         aList.append(flatten(i))
    #                 # # print(aList)
    #                 #     else:
    #                 #         aList.append(i[0])
    #                 # else:
    #                 #     aList.append(flatten(i))
    #                 # #aList.append(flatten(i))
    #                 # # print(aList)
    #             else:
    #                 aList.append(i)
    #     else:
    #         aList.append(item)       ##为了保持原来的顺序
    # return aList
    #
    # aListcopy = aList[:]
    #

    # newList = []
    # for item in aList:
    #     if type(item) != type([]):
    #         newList.append(item)
    #     else:
    #         newList.extend(flatten(item))
    # return newList
    #

def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    aListcopy = aList[:]
    for item in aListcopy:
        if type(item) == type([]):
            aList.remove(item)      ##将原来的删掉
            aList.extend(flatten(item))
            	# list.extend(seq)   ！！！！！  多了解一些函数
                # 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）

        else:
            aList.remove(item)    ###保持原来的顺序
            aList.append(item)
    return aList


aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# after flatten:  aList = [1,'a','cat',2,3,'dog',4,5]
print(flatten(aList))
print(aList)
