str = input("Enter a string:")
dict= {}
lst = sorted(str)
for i in lst:
    if i not in dict:
        dict[i] = 0
    dict[i]+=1
print(dict)
