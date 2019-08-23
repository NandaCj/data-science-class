a = 5
b = 10

if a < b:
    print("A is less than B..")

A = True
B = None

if A :
    print("A is True....")

if B :
    print("B is not None")

L = [5]

if L :
    print("L is not empty")

if (L or B) :
    if A:
        pass
    else:
        if A :
            pass
        elif B:
            pass
    if B :
        pass
    if a :
        pass

i = 0

while i < 5 :
    print(i)
    i += 1


name = 'kumaravel'
# print(dir(name))
# print(name.count('a'))
# print(name.upper())

detail = "...name is kumaravel and job is IT professional..."
print(detail.split())
print(detail.lstrip("..."))
print(dir(detail))