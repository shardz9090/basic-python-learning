from multipledispatch import dispatch

# Function overloading methods


def math(a, b):
    return ((a+b)*2)


name = math(2, 2)
print(name)


def math(a, b, c):
    return ((a+b+c)*3)


fame = math(2, 2, 2)
print(fame)

print("----------------------------------------")


def add(a=None, b=None):
    if a != None and b == None:
        print(a)
    else:
        print(a+b)


add(2, 2)
add(2)
print("----------------------------------------")

# function overloading only uses latest defined method in python, above program wont work if line 4 is  called after
# line 8. so import multiplieddispatch


@dispatch(int, int)
def zath(a, b):
    print(a*b)


@dispatch(int, int, int)
def zath(a, b, c):
    print(a*b*c)


zath(3, 3)
zath(3, 3, 3)
print("----------------------------------------")


def names(all):
    for x in all:
        print(x)


all = ["a", "b", "c"]
names(all)
print("----------------------------------------")

# recursive function


def new_recurs(z):
    if (z <= 0):
        return 0
    else:
        za = z + new_recurs(z-1)
        return za


fa = new_recurs(5)
print(fa)
print("----------------------------------------")
