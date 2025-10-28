# def test():
#     print("hello...")

# test()


def add(clac):
    def wapper(*a):
        print(a[0]+a[1])
        clac(*a)
    return wapper

def mul(clac):
    def wapper(*a):
        print(a[0]*a[1])
        clac(*a)
    return wapper
@add
@mul
def clac(a,b):
    print("add = ")

clac(10,23)