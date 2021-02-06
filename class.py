#class Person:
#    def __init__(self , age , name):
#        self.age = age
#        self.name = name
#    def getDetails(self):
#        print('THe name and age is ' , self.name , self.age)

#obj = Person(20 , 'Riya')
#obj.getDetails()


class Maths:
    def __init__(self , num1 , num2):
        self.num1 = num1
        self.num2 = num2
    def getSum(self):
        print('Addition is' , self.num1+self.num2)
    def getDifference(self):
        print('Subtraction is ' , self.num1-self.num2)
    def getDivision(self):
        print('Division is ' , self.num1/self.num2)
    def getMultiplication(self):
        print('Multiplication is ', self.num1*self.num2)

sum = Maths(20,5)
sum.getSum()
sum.getDivision()
sum.getDifference()
sum.getMultiplication()
