lst = []
n = int(input("Enter the size of the list:"))
print("Enter the numbers")
for i in range(n):
    numbers  = int(input())
    lst.append(numbers)

l2 = sorted(lst , reverse = True)
print(l2)
