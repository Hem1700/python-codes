str = input("Enter a string: ")
str1= str.lower()
dict = {}

for i in str1:
    if i not in dict:
        dict[i] = 0
    dict[i]+=1
print(dict)
keys = list(dict.keys())
max_value = keys[0]
for k in dict.keys():
    if dict[i]>dict[max_value]:
        max_value = i

print(max_value)
