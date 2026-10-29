class Aipa:
    def __init__(self,name,age,trade,marks):
        self.name=name
        self.age=age
        self.trade=trade
        self.marks=marks
        


    
std1=Aipa("ritika",18,"aipa",75)
std2=Aipa("pinki",20,"aipa",80)


print(std1.name)
print(std2.age)
print(std1.marks)
print(std2.name)
print(std1.age)





class Student:
    def __init__(self,name,age,trade,marks):
        self.name=name
        self.age=age
        self.trade=trade
        self.marks=marks
        
    def display_details(self):
        print("name:",self.name)
        print("age:",self.age)
        print("trade:",self.trade)
        print("marks:",self.marks)


    def check_result(self):
        if self.marks>=40:
            print("pass")
        else:
            print("fail")


    def percentage(self,total_marks):
        return(self.marks/total_marks)*100        

student1=Student("priya",20,"aipa",56)
student2=Student("riya",20,"aipa",36)
student3=Student("priyanshi",20,"aipa",76)
student4=Student("priyanka",20,"aipa",96)
student5=Student("supriya",20,"aipa",39)

student4.display_details()
student4.check_result()


student5.display_details()
student5.check_result()

student3.display_details()
student3.check_result()
print(student3.percentage(100),"%")



class Vehicle:
    def __init__(self,color,name,brand,speed):
        self.color=color
        self.name=name
        self.brand=brand
        self.speed=speed

    def display_details(self):
        print("color:",self.color)
        print("name:",self.name)
        print("brand:",self.brand)
        print("speed:",self.speed)

    def check_speed(self):
        if self.speed>100:
            print("high speed")
        elif self.speed>=60:
            print("normal speed")
        else:
            print("low speed") 

car1=Vehicle("black","Jaguar","Tata motars",90)
car2=Vehicle("white","BMW","BMW Motorrad",120)

car1.display_details()
car1.check_speed()
car2.display_details()
car2.check_speed()


class Student:
    def __init__(self):
        self.name="ritika"
        self._trade ="aipa"
        self.__marks=90
std=Student()
print(std.name)
print (std._trade)
print(std.__marks
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print("deposit successfully")
        else:
            print("invalid amount")
    def withdraw(self,amount):
        if amount<=0:
            print("invalid amount")
        elif amount<=self.__balance:
            self.__balance-=amount
            print("withdraw successfully")
        else:
            print("insufficient balance")

    def check_balance(self):
        print("correct balance:",self.__balance)
user = BankAccount("Ritika",1000) 
print(user.name)
user.deposit(500)
user.withdraw(200)
print(user.check_balance())






        
            
        
    
        



        



    