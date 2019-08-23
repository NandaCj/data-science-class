# print(range(12))

"""
def func_name(args):
    # postional args
    # keyword args
    
    expressions
    
"""

def func():
    print("fun without args is called ...")

func()

def func_1(a , b, x=None , y=None , z=None,):
    # x, y positional args
    # keyword/default args
    print(a, b, x, y, z)
    print(a)
    print(b)
    print(x)


value = func_1(10, b=20 ,  x=30 , z = 50,)
print(value)

# print(5 * [None])


def mult(a, b, c, d):
    # return statement are optional
    x = a*b*c*d
    #
    return x

result = mult(1,2,3,4)

print("result", result)

x = []

def update_x():
    # y = []

    for i in range(10):
        x.append(i)
    # x = 20
    return x

fun_result = update_x()
print(fun_result)
print(x)

global z
# z = 100

def f1():

    global z
    # print(z)
    z = 30
    print(z )

def f2():
    global z
    print(z)

f1()
f2()







name = 'Nandha Gopal'
print(name.split(" "))

print([x for x in name])







