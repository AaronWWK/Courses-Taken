


def get_sum(a, b):
    return a + b
def run_a_func(func, a, b):
    return func(a, b)
print(run_a_func(get_sum, 1, 2))  # get_sum 没有括号，是因为把函数本身作为参数放进去


tuple = (1,2,3,)
a,b,c = tuple
print(a)
print(b)
print(c)
L = list(tuple)
print(L)
abs = (2,2)
print(abs[1])
