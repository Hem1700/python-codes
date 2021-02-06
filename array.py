lst = []
num = int(input("Enter the size of the list: "))
print("Enter list elements: ")
for n in range(num):
  numbers = int(input())
  lst.append(numbers)

def Sum(lst):
    sum  = 0
    for i in lst:
        sum  = sum+i
    return sum

print('Sum' , Sum(lst))
#print("Sum:", sum(lst))
