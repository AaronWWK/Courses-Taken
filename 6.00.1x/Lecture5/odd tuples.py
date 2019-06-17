

def oddTuples(aTup):
    aTup2 = ()
    for i in range(0,len(aTup),2):

        aTup2=aTup2+(aTup[i],)

    return aTup2

aTup = ('I', 'am', 'a', 'test', 'tuple')
print(oddTuples(aTup))
