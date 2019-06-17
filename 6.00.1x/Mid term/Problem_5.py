def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    listnew = []
    answer = 0
    for i in range(0,len(listA)):
        listnew.append(listA[i]*listB[i])

    print(listnew)
    for i in range(len(listnew)):
        answer +=listnew[i]
    return answer


listA = [1, 2, 3]
listB = [4, 5, 6]

print(dotProduct(listA,listB))
