import functools

fun = lambda x, y : x*y

# print(fun(10, 20))



def func(x, y):
    return x*y

# print(func(10, 20))


#--------------------- filter ----------------
L = [1,2,3,4,5,6]

Y = filter(lambda x : x%2 ==0 , L)

print(Y)
print(list(Y))

#--------------------- Map ----------------

M = map(lambda x: x*x , L)
print(list(M))

#--------------------- reduce ----------------

R = functools.reduce(lambda x, y : x+y , L)
print(R)

#--------------------- Test ----------------

print(list(map(lambda x: x*2, L)))

print(list(filter(lambda x : x % 2 ==0 , L )))
