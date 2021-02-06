lst = []
n = int(input("Enter the size of the list:"))
print("Enter the elements:")
for i in range(n):
    numbers = int(input())
    lst.append(numbers)
pos_lst = []
neg_lst = []
for i in lst:
    if (i<0):
        neg_lst.append(i)

    else:
        pos_lst.append(i)

print( 'Negative list is:',neg_lst)
print("Positive list is" , pos_lst)
