class numb:
    def __init__(self , x, y):
        self.x=x
        self.y=y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def __str__(self):
        return 'x is {} and y is {}'.format(self.x,self.y)

obj = numb(7,6)
print(obj.getX())
print(type(obj.getX()))
print('----------------------------')
print(obj.getY())
print(type(obj.getY()))
print('------------------------------')
print(obj.__str__())
print(type(obj.__str__()))
print('-----------------------------')
print(type(obj))
print(obj)
