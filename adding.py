str = input("Enter a string :")
lst = str.split(' ')
print(lst)
new_lst = []
for  i in lst:
    new_lst.append(i+'ing')
new_str = ' '.join(new_lst)
print(new_str)
