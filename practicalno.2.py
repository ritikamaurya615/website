# def greet(name):
#     print("Welcome", name)

# greet("Ritika")

#Taskno.2 Addition Function

# def add(a, b):
#     return a + b

# print("Sum =", add(10, 20))

#Task no.3 Even and Odd

# def check(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# print(check(7))



#Task no.4 factorial 

# def factorial(n):
#     if n < 0:
#         return "Invalid input"

#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     return fact

# print("Factorial =", factorial(6))


#Task no.5 largest three number


# def largest(a, b, c):
#     return max(a, b, c)

# print("Largest =", largest(10, 25, 15))


#Task no.6 grade calculator

# def grade(marks):
#     if marks < 0 or marks > 100:
#         return "Invalid Marks"
#     elif marks >= 90:
#         return "A"
#     elif marks >= 75:
#         return "B"
#     elif marks >= 60:
#         return "C"
#     elif marks >= 40:
#         return "D"
#     else:
#         return "Fail"

# print("Grade =", grade(85))


#task no.7 list

# def total(lst):
#     return sum(lst)

# def average(lst):
#     return sum(lst) / len(lst)

# def minimum(lst):
#     return min(lst)

# def maximum(lst):
#     return max(lst)

# numbers = [10, 20, 30, 40, 50]

# print("Total =", total(numbers))
# print("Average =", average(numbers))
# print("Minimum =", minimum(numbers))
# print("Maximum =", maximum(numbers))



#Task no.8

balance = 1000

def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
    else:
        print("Invalid amount")

def withdraw(amount):
    global balance
    if 0 < amount <= balance:
        balance -= amount
    else:
        print("Invalid amount or insufficient balance")

def show_balance():
    print("Balance =", balance)

while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        deposit(float(input("Enter amount: ")))
    elif choice == 2:
        withdraw(float(input("Enter amount: ")))
    elif choice == 3:
        show_balance()
    elif choice == 4:
        break
    else:
        print("Invalid choice")