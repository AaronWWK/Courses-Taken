listA = [1, 4, 3, 0]

print(sorted(listA))  #do not mutate listA

listA.sort()
print(listA)
print(listA.sort())
print(listA.sort)


L = [1,2,3]
B = L
print(L == B)


A = [1,2,3,4]
A.insert(2,8)
print(A)

B = A.pop(1) ###remove 1 element in listA, and return that element .pop(index)
print(B)
print(A)
A.reverse()
print(A)

aList = [0, 1, 2, 3, 4, 5]
bList = aList
aList[2] = 'hello'
print(aList is bList)
