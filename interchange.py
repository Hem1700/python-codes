lst = []
num  = int(input("Enter the size of the list:"))
print("Enter the numbers in list:")
for i in range(num):
    numbers  = int(input())
    lst.append(numbers)

def interchange(lst):
    temp = []
    size = len(lst)
    temp = lst[0]
    lst[0] = lst[size - 1]
    lst[size - 1] = temp
    return lst

print("Previous list" , lst)    
print("List after interchange:", interchange(lst))
