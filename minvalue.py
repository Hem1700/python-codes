str = input("Enter a string:")
dict = {}
for i in str:
    if i not in dict:
        dict[i] = 0
    dict[i] = dict[i]+1

print(dict)
lst1 = []
keys = list(dict.keys())
min_value = keys[0]
for i in dict:
    if dict[i]<=dict[min_value]:
        min_value = i
        lst1.append(i)
print(min_value)
print(lst1)
