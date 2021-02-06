lst = []
num  = int(input("Enter the size of the list:"))
print("Enter the elements:")
for i in range(num):
    numbers = int(input())
    lst.append(numbers)


def check(lst):
    n = int(input("Enter the number to check :"))
    if n in lst:
            return "Number is there!"
    else:
            return "It isnt there"
print(check(lst))
