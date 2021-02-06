str = input("Enter a string:")
dict = {}

for i in str:
    if i not in dict:
        dict[i] = 0
    dict[i]+=1
print(dict)

keys = list(dict.keys())
print(keys)
for i in keys:
    print(dict[i])


for i in keys:
    if dict[i]>1:
        del dict[i]
print(dict)
new_str = ' '.join(dict)
print(new_str)
