lst = []
n = int(input("Enter the size of the list: "))
print("Enter the numbers!:")
for i in range(n):
    numbers = int(input())
    lst.append(numbers)

lst.sort()
print("Second largest element is:", lst[-2]) 
