lst = []
n = int(input("Enter the size of the list: "))
print("Enter the elements:")
for i in range(n):
    numbers = int(input())
    lst.append(numbers)
x = int(input("Enter the number to be removed"))
for  i in lst:
    if x in lst:
        lst.remove(x)
    else:
       print("Number doesnt exist")
print(lst)
