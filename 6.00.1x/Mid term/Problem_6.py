def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    Lcopy = L[:]

    L = []
    for i in range(len(Lcopy),0,-1):  ##一定要写步长

        L.append(Lcopy[i-1])   ##把整体倒叙
        #print(L)
    Lcopy2 = L[:]    ## 将L复制到Lcopy2
    for item in Lcopy2:
        if type(item) == list:   ##判断item 是不是list  如果不是就结束
            #print(item)
            L.remove(L[0])    ## ()内是要移除的对象   因为L不是空的list，所以将原来在前面的几项移除，每次循环，都删除第一个
            L.append(deep_reverse(item))    ##加上倒置之后的每一个小项

    # Lcopy2 = L[:]
    # L=[]                  ### 如果采用这种方式，当list中的项不是 list的时候， L会被换成空值，使得最终结果也是空值
    # for item in Lcopy2:
    #     if type(item) == list:
    #         L.append(deep_reverse(item))
    #print(L)
    return L

L = [[1, 2], [3, 4], [5, 6, 7]]

L = deep_reverse(L)
#print(deep_reverse(L))
print(L)
