#  Constructor
# class Calculate():
#     def __init__(self,a,b):
#      self.a=a
#      self.b=b
#      c=a+b
#      print("Total is: ",c)
# obj = Calculate(7,6)

# class Calculate():
#     def __init__(self):
#         print("I am Constructor")

# obj = Calculate()

# Calculator by Ooops
# class Calculator():
#     def __init__(self, a, b):
#      self.a = a
#      self.b = b
#     def add(self):
#         return self.a+self.b
#     def mul(self):
#         return self.a*self.b
#     def div(self):
#         if self.b == 0:
#             return "Error: Division by zero"
#         return self.a/self.b
#     def sub(self):
#         return self.a-self.b

# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# obj=Calculator(a,b)
# choice=1
# while choice!=0:
#     print("0. Exit")
#     print("1. Add")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     choice=int(input("Enter choice: "))
#     if choice==1:
#         print("Result: ",obj.add())
#     elif choice==2:
#         print("Result: ",obj.sub())
#     elif choice==3:
#         print("Result: ",obj.mul())
#     elif choice==4:
#         print("Result: ",round(obj.div(),4))
#     elif choice==0:
#         print("Exiting!")
#     else:
#         print("Invalid choice!!")