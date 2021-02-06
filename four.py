#6th problem

lst1 = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
new_lst1 = [value*2 for value in lst1]
print(new_lst1)

#7th problem
lst2 = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]
new_lst2 = [name for surname , name in lst2]
print(new_lst2)


#8th Problem
l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']

x = filter(lambda x,y:x>3 and y>3 , zip(l1,l2))
print(x)
