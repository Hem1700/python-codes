str = input("Enter a string:")
remove_character = input("Enter the character to be removed:")
lst = []
for i in str:
    lst.append(i)
print(lst)
for i in lst:
    if remove_character in lst:
        lst.remove(remove_character)
        newstr = ''.join(lst)
        print(newstr)
