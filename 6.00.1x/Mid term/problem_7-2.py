def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above

    If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
    If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
    If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}
    '''

    # my_list =[]
    # inver_d = {}
    # for key,value in d.items():
    #     my_list.append(key)
    #     print(my_list)
    #     inver_d[value] = my_list[:]  ##不能直接用my_list，因为后面会删除掉其中的内容
    #     print(str(inver_d))
    #     # inver_d[value].append(key)
    #     my_list.remove(key)
    #     # inver_d[value]= inver_d[value].sort()
    # return inver_d


    my_list =[]
    inver_d = {}
    for key,value in d.items():
        inver_d[value] = my_list[:]
        print(str(inver_d))
        inver_d[value].append(key)
        print(str(inver_d))
        # inver_d[value]= inver_d[value].sort()
    return inver_d



d = {1:10, 2:20, 3:30, 4:30}
print(str(dict_invert(d)))
