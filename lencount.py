str = input("Enter a sentence:")
n = int(input("Enter the length:"))
new_lst = []
lst = str.split()
for i in lst:
    if len(i)>n:
        new_lst.append(i)

print(new_lst)
