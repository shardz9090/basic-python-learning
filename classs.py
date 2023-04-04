# Constructor
class name:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def first(self):
        print("shardul")

    def last(self):
        print("mishra")


# who = name()
# print(who.first())
# who.first()
# who.last()

poi = name(10, 20)
poi.x = 17
poi.y = 20
print(poi.x, poi.y)
print("----------------------------------------")

# Constructor


class namess:
    def __init__(self, namee):
        self.namee = namee

    def what(self):
        print(f"hi i am {self.namee}")


sema = namess("shardul mishra")
sema.what()
print("----------------------------------------")

# Inheritence


class Dog:
    def doggo(self):
        print("nice dog")


class Newdog(Dog):
    pass


dog1 = Newdog()
dog1.doggo()
print("----------------------------------------")
