

def quick_sort(L):
    for i in range(1,len(L)):
        for j in range(i,0,-1):
            if L[j] < L[j-1]:
                L[j],L[j-1] = L[j-1],L[j]
                print(L)
    return L[:]


L = [4,6,1,7,9,18,10,1,3,2]
print(quick_sort(L))
