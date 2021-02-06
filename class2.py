class fruits:
    def __init__(self, name,price):
        self.name = name
        self.price = price



L = [fruits('Mangoes',10) , fruits('Apple' , 20) , fruits('Watermelon' , 30)]

for i in sorted(L , key= lambda x:x.price):
    print(i.name)
    print(i.price)
