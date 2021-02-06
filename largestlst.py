lst = []
num = int(input("Enter the size of the list:"))
print('Enter the elements of list:')
for n in range(num):
    numbers = int(input())
    lst.append(numbers)

def largest(lst):
    max_value = 0
    for i in lst:
        if i>max_value:
            max_value = i
    return max_value

def smallest(lst):
    for i in lst:
        min_value = i
        if i<min_value:
            min_value = i
        return min_value

print("Largest number" , largest(lst))
print("Smallest number" , smallest(lst))
