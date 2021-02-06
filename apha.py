str  = input("Enter a string: ")
str1 = str.lower()
dict = {}
for i in str1:
    if i not in dict:
        dict[i] = 0
    dict[i]+=1

print(dict)
keys = list(dict.keys())
for i in sorted(keys):
    print(i,dict[i])
