#exercitiu 1
"""
matrix = [
    [1, 2, 3],
    [5,2,6], 
    [7, 8, 9]
]

count=0

for row in matrix:
    increasing = True
    for i in range(len(row)-1):
        if row[i]>row[i+1]:
            increasing=False
            break
    if increasing:
        count+=1


print("Numar de randuri crescatoare: ", count)

"""
#exercitiu 2

matrix = [
    [1, 2, 3],
    [5,2,6], 
    [7, 8, 9]
]

