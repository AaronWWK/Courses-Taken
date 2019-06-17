def genPrimes():
    """

    """

    n=2
    while True:
        if n == 2:
            yield n
        else:
            num = 1
            for i in range(2,n-1):
                if n % i == 0:
                    num += 1
            if num == 1:
                yield n
        n += 1

foo = genPrimes()
print(foo.__next__())
print(foo.__next__())
print(foo.__next__())
print(foo.__next__())
