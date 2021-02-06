lst = []
n  = int(input("Enter the size of the list"))
print("Enter the elements")
for i in range(n):
    numbers = int(input())
    lst.append(numbers)
dict = {}
for i in lst:
    if i not in dict:
        dict[i] = 0
    dict[i]+=1
print(dict)


def occ(lst , x):
    return lst.count(x)
x  = int(input("Enter the number to be checked"))

print(occ(lst , x))
#print('{} occured {} times'.format(x , occ(lst ,x)))
