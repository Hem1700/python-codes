#First Problem

str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]

for i in str_list:
    print(len(i))

#Second Problem
original_str = "The quick brown rhino jumped over the extremely lazy fox."
count = 0
for i in original_str:
    count+=1

print(count)

#Third Problem
addition_str = "2+5+10+20"
add = 0
lst = addition_str.split('+')
print(lst)
for i in lst:
    i2 = int(i)
    add = add+i2
print(add)

#Fourth Problem
week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"

lst1 = week_temps_f.split(',')
print(lst1)
sum = 0
count_1 = 0
for i in lst1:
    i2 = float(i)
    sum+=i2
    count_1+=1

avg = sum/count_1
print(avg)

#Fifth Problem
print('***********************************************************************')
nums = [4, 2, 23.4, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]
count_2 = 0
for i in nums:
    print(i)
    if i==9:
        count_2+=1
print('***************************')
print(count_2)

#Sixth Problem
lst = ["hi", "goodbye", "python", "106", "506", 91, ['all', 'Paul', 'Jackie', "UMSI", 1, "Stephen", 4.5], 109, "chair", "pizza", "wolverine", 2017, 3.92, 1817, "account", "readings", "papers", 12, "facebook", "twitter", 193.2, "snapchat", "leaders and the best", "social", "1986", 9, 29, "holiday", ["women", "olympics", "gold", "rio", 21, "2016", "men"], "26trombones"]

end = lst[-1]
print(end)

#Seventh Problem

sent = "The bicentennial for our university was in 2017"
lst3 = sent.split(' ')
print(lst3)

#Eight Problem
rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
lst4 = []
new_lst = rainfall_mi.split(',')
print(new_lst)
for i in new_lst:
    print(i)
    i2 = float(i)
    if i2>3:
        lst4.append(i2)
print(lst4)


#Nineth Problem
sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."

lst5 = sentence.split(' ')
print(lst5)
lst6 = []
for i in lst5:
    print(i)
    if ('a' in i or 'e' in i):
        lst6.append(i)
print('**********************************')
print(lst6)

#Tenth Problem

y = 22
z = 30
if z>y:
    y+=5

x = y*z
print(x)

#Eleventh Problem
wrd_lst = ["Hello", "activecode", "Java", "C#", "Python", "HTML and CSS", "Javascript", "Swift", "php"]
count_3 = 0
for i in wrd_lst:
    if len(i)<6:
        count_3+=1
print(count_3)

#Twelth Problem
original_str = "The quick brown rhino jumped over the extremely lazy fox"
new_lst1 = []
lst7 = original_str.split(' ')
print(lst7)
for i in lst7:
    x = len(i)
    new_lst1.append(x)
print(new_lst1)

#13th Problem
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"

lst8 = org.split(' ')
print(lst8)
for i in lst8:
    if i in stopwords:
        lst8.remove(i)
new_str = ' '.join(lst8)
print(new_str)

#14th Problem

scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
new_lst2 = []
lst9 = scores.split(' ')
print(lst9)
for i in lst9:
    i2 = int(i)
    if (i2>=90):
        new_lst2.append(i)
print(new_lst2)

#15 Problem
print('#######################################################################################')

str = '{a} {b} , This is Hem'.format(a = 'Hi' , b = 'Riya')
print(str)

#16th Problem

swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4, 'Phelps':23}

swimmers['Phelps']+=5
print(swimmers)

#17th Problem
travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}
count_4 = 0
for k,v in travel.items():
    count_4+=v
print(count_4)

#18th Problem
placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."

dict = {}
for i in placement:
    if i not in dict:
        dict[i] =0
    dict[i]+=1
print(dict)
keys = list(dict.keys())
min_value = keys[0]
for i in keys:
    if dict[i]<dict[min_value]:
        min_value = i
print(min_value)

#19th Problem
product = "iphone and android phones"

dict1 = {}
for i in product:
    if i not in dict1:
        dict1[i] = 0
    dict1[i]+=1
print(dict1)

keys1 = list(dict1.keys())
max_value = keys1[0]
for i in keys1:
    if dict1[i]>dict1[max_value]:
        max_value = i

print(max_value)


#20th Problem
