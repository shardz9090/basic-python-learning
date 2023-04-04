shardul = {
    "name": "shardul mishra",
    "age": "20",
    "address": "biratnagar"
}
shardul["gender"] = "male"
print(shardul["name"])
print(shardul["address"])
print(shardul["age"])
print(shardul["gender"])
print("----------------------------------------")

giveinp = input("phone = ")
digits = {
    "1": "One",
    "2": "two",
    "3": "three"
}
output = ""
for ch in giveinp:
    output += digits.get(ch, "!") + " "
print(output)
print("----------------------------------------")

try:
    a = int(input("enter your age"))
    b = 100/a
    print(b)
except ValueError:
    print("enter int value")
except ZeroDivisionError:
    print("cant divide by zero")
