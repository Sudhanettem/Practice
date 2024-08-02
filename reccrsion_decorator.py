#recursion
def func(n):
    if n==1 :return 1
    return n*func(n-1)
print(func(3))
print(func(4))
print(func(5))


#decoration

def logtime(func):
    def tst():
        print("first")
        val = func()
        print("After")
        return val
    return tst

@logtime
def test ():
    print("Hello Sudha")


test()