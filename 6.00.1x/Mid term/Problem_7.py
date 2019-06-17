def dict_interdiff(d1,d2):

    intersect1 = {}
    intersect2 = {}
    difference ={}

    for k in d1.keys() :
        if k in d2.keys():              ### 遍历字典中的 key 的方法，   返回的是一个包含值的list
                                        ###遍历 value ：   d2.values
            intersect1[k] = d1[k]
            intersect2[k] = d2[k]
        else:
            difference[k] = d1[k]
    for k in d2.keys():
        if not k in d1.keys():
            difference[k] = d2[k]
    return intersect1,intersect2,difference


d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

print(dict_interdiff(d1, d2))
