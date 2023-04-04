i = 1 
while i <=5:
    print("*" * i)
    i=i+1
else:
    print("done")
print("----------------------------------------")

boys = ['dae', 'kae', 'lae']
for namess in boys:
    print(namess)
print("----------------------------------------")

for x in range(3):
    for y in range(3):
        print(f'({x},{y})')
print("----------------------------------------")

numm = [5,2,5,2,2]      #print F
for x in numm:
    output = ''
    for y in range(x):
        output += 'x'
    print(output)
print("----------------------------------------")

matrix = [
    [0, 1, 2],
    [3, 4, 5],
    [9, 8, 7]
]
print(matrix)
print(matrix[2][2])
for x in matrix:
    for y in x:
        print(y)
print(50 in matrix)
print("----------------------------------------")

nums = [1,2,4,2,1,6,7,2,1]
unique = []
for x in nums:
    if x not in unique:
        unique.append(x)
print(unique)
print("----------------------------------------")




