str = input("Enter a sentence:")
lst = str.split(" ")
print(lst)
dict = {}
for i in lst:
    if i not in dict:
        dict[i] = 0
    dict[i]+=1

print(dict)
x1 = input("Enter the word to be removed:")

del dict[x1]
print(dict)
