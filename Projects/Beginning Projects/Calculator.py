#Here we are going to do some pratice with the code from lesson1.basics.py
#Print, First section: Calculations 2nd section: guessing game, and 3rd section: To-do list
print("----------------------")
print("Calculator")
#Definee add, subtract, multiply, divide fuctions 
#Keeping it simple and having two variables
def add(a, b):
    return a + b 
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    else: return a / b 

#define options for simple calcuation 
def calculator():
    print("Select option:")
    print ("1. Add")
    print ("2. Subtract")
    print ("3. Multiply")
    print ("4. Divide")

    choice = input("Choose an operation (1/2/3/4): ")
    num1=float(input("Enter first number: "))
        #float allows for decimal numbers
    num2=float(input("Enter second number: "))

#When to use If vs elif
#"If" is used if a specified condition is true
#"elif" is used if the previous condition is false and the new condition is true
    if choice == "1":
        print("Results:", add(num1, num2))
    elif choice == "2":
         print("Results:", subtract(num1, num2))
    elif choice == "3":
         print("Results:", multiply(num1, num2))
    elif choice == "4":
        print("Results:", divide(num1, num2))
    else:
        print("Invalid input")
#Made a mistake here; 
#Before: print("Results:"), divide(num1, num2) -> "Results:"
#After: print("Results:", divide(num1, num2)) -> "Results: [value]"
calculator()
print("----------------------")