#Second Problem
lst_tups = [('Articuno', 'Moltres', 'Zaptos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'), ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", "Tauros", 'Dragonite'), ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Unown', 'Teddiursa', 'Phanpy'), ('Loudred', 'Volbeat', 'Wailord', 'Seviper', 'Sealeo')]

t_check = []
for i in lst_tups:
    t_check.append(i[2])

print(t_check)

#3rd Problem

tups = [('a', 'b', 'c'), (8, 7, 6, 5), ('blue', 'green', 'yellow', 'orange', 'red'), (5.6, 9.99, 2.5, 8.2), ('squirrel', 'chipmunk')]

seconds = []
for i in tups:
    seconds.append(i[1])

print(seconds)

#4th Problem
v1,v2,v3,v4 = 1,2,3,4
print(v1,v2,v3,v4)

#5th Problem
water , fire , electric , grass = 'Squirtle' , 'Charmandar' , 'Pikachu' , 'Bulbasaur'
print(water , fire , electric , grass)

#6th Problem

pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}
p_names = []
p_number = []

for k,v in pokemon.items():
    p_names.append(k)
    p_number.append(v)
print(p_names)
print(p_number)


#7th Problem
def circle(r):
    pi = 3.14
    circumference  = 2*pi*r
    area = pi*r*r
    return (circumference , area)

print(circle(4))


#8th Problem
def sum(x ,y):
    return x+y
z = (5,4)
y = (6,7)
print(sum(*z))
print(sum(*y))


#9th Problem
gold = {'USA':31, 'Great Britain':19, 'China':19, 'Germany':13, 'Russia':12, 'Japan':10, 'France':8, 'Italy':8}
num_medals = []
for k,v in gold.items():
    num_medals.append(v)
print(num_medals)


#10th Problem

def subtract_three(x):
    return x-3

print(subtract_three(8))

#11th Problem
def change(y):
    return y+7

print(change(4))

#12th Problem
def decision(string):
    if len(string)>17:
        return 'This is a long string'
    else:
        return 'THis is short string'
print(decision('THIS IS HEMM'))

#13 Problem
def multiply(string , mult_int = 10):
    return string*mult_int

print(multiply('Helloo'))


#14 Problem
x = ['Riya' , 'Hem']
y = ['Parekh' , 'Parekh']
lst = zip(x,y)
mapped = set(lst)
print(mapped)


#15th Problem
##    return len(x)

#n = int(input('Enter the number of names you want to enter' ))
#lst = []
#for i in range(n) :
##    lst.append(name)

#x = map(fun , lst)

#print(list(x))


#1st Problem

lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

def fun(lst):
    for i in lst:
        if 'w' in i:
            return True
filter_testing = filter(lambda x: 'w' in x  , lst_check)

for i in filter_testing:
    print(i)

#2nd Problem

n = int(input('Enter the length of list'))
lst5 = []
print('Enter the numbers ')
for i in range(n):
    numbers = int(input())
    lst5.append(numbers)
print(lst5)
def eve(lst):
    if lst%2 ==0:
        return True
    else:
        return False
new_lst5 = filter(eve , lst5)

for i in new_lst5:
    print(i)


#3rd Problem

things = [4,5,6]

new_lst6 = [i*2 for i in things]

print(new_lst6)


#4th Problem
n1 = int(input('Enter the length of the list'))
lst7 = []
print('Enter the numbers in the list')
for  i in range(n1):
    numbers = int(input())
    lst7.append(numbers)

new_lst7 = [value*2 for value in lst7]
print(new_lst7)


#5th Problem
students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]

passed = [names for names , grade in students if grade>=70]
print(passed)
