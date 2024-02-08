#1
class String:
    def getString(self):
         self.input_string = input()
         
    def printString(self):
         print(self.input_string.upper())
         
#2
class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    
    def area(self):
        return self.length ** 2
    
shape_instance = Shape()
square_instance = Square(7)

print(shape_instance.area())
print(square_instance.area())

#3
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
     super().__init__()
     self.length = length
     self.width = width
     
    def area(self):
         return self.length * self.width
    
shape_instance = Shape()
rectangle_instance = Rectangle(6,8)

print (shape_instance.area())
print (rectangle_instance.area())
    
#4
class Point: 
    def getCoordinates(self, x1, y1): 
        self.x1 = x1 
        self.y1 = y1 
 
    def showCoordinates(self): 
        print(f'Coordinates: {self.x1}, {self.y1} ') 
 
    def moveCoordinates(self, x2, y2): 
        self.x2 = x2 
        self.y2 = y2 
 
    def distBetweenCoordinates(self): 
        print(((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2) ** 0.5) 
 
point = Point() 
point.getCoordinates(1, 2) 
point.moveCoordinates(5, 6) 
point.distBetweenCoordinates()

#5
class BankAccount: 
    def __init__(self, owner, balance=0): 
        self.owner = owner 
        self.balance = balance 
         
    def deposit(self, amount): 
        if amount > 0: 
            self.balance += amount 
            print(f"Deposited ${amount}. New balance: ${self.balance}") 
        else: 
            print("Invalid deposit amount. Please deposit a positive amount.") 
      
    def withdraw(self, amount): 
        if 0 < amount <= self.balance: 
            self.balance -= amount 
            print(f"Withdrew ${amount}. New balance: ${self.balance}") 
        else: 
            print("Invalid withdrawal amount or insufficient funds.")        
       
account = BankAccount("Naze", 1000)  
 
account.deposit(500)         
account.withdraw(200)         
account.withdraw(1000)     
account.deposit(-50)

#6
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True