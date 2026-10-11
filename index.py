#Task1
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
if number1 > number2:
    print(f"{number1} is greater than {number2}")
elif number1 < number2:
    print(f"{number2} is greater than {number1}")
else:
    print(f"{number1} is equal to {number2}")

#Task2
a = int(input("Enter a number: "))
if a== 0:
    print("The number is zero.")
elif a > 0:
    print("The number is positive.")
else:
    print("The number is negative.")

#Task3
a = int(input("Enter a number: "))
if a % 2 == 0:
    print(f"{a} is an even number.")
else:
    print(f"{a} is an odd number.")

#Task4
score = int(input('Enter your exam score: '))
if score < 0 or score > 100:
    print("invalid score")
elif score >= 91:
    print("Grade: A")
elif score >= 81:
    print("Grade: B")
elif score >= 71:
    print("Grade: C")
elif score >= 61:
    print("Grade: D")
elif score >= 51:
    print("Grade: E")
else:
    print("Grade: F")


#Task5
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if a > b and a > c:
    print(f"{a} is the greatest number.")
elif b > a and b > c:
    print(f"{b} is the greatest number.")
elif c > a and c > b:
    print(f"{c} is the greatest number.")
else:
    print("All numbers are equal.")


#Task6
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /, % ,** , //): ")
if operation == "+":
    print(f"{a} + {b} = {a + b}")
elif operation == "-":
    print(f"{a} - {b} = {a - b}")
elif operation == "*":
    print(f"{a} * {b} = {a * b}")
elif operation == "/":
    if b != 0:
        print(f"{a} / {b} = {a / b}")
    else:
        print("Error: Division by zero is not allowed.")
elif operation == "%":
    if b != 0:
        print(f"{a} % {b} = {a % b}")
    else:
        print("Error: Division by zero is not allowed.")
elif operation == "**":
    print(f"{a} ** {b} = {a ** b}")
elif operation == "//":
    if b != 0:
        print(f"{a} // {b} = {a // b}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter a valid operation (+, -, *, /, %, **, //).")

#Task7
age = int(input("Enter your age:"))
if age < 0:
    print("Invalid age.")
elif age <= 12:
    print("Child")
elif age <= 17:
    print("Teenager")
elif age <= 64:
    print("Adult")
else:
    print("Senior")


#Task8
a = int(input("Enter total purchase amount: "))
discount = 0
if a <= 100:
    discount = 0
elif a > 100 and a < 300:
    discount = 10
elif a > 299 and a < 500:
    discount = 15 
else:
    discount = 20
b = a - a * discount / 100
print(f"Original price is {a}, Discount is {discount}% , Final price is {b}")


#Task9
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))
if a <= b and a <= c:
    if b <= c:
        print(a, b, c)
    else:
        print(a, c, b)
elif b <= a and b <= c:
    if a <= c:
        print(b, a, c)
    else:
        print(b, c, a)
else:
    if a <= b:
        print(c, a, b)
    else:
        print(c, b, a)


#Task10
balance = 1000
amount = int(input("Enter withdrawal amount: "))
if amount <= 0:
    print("Invalid amount")
elif amount > balance:
    print("Insufficient balance")
else:
    balance = balance - amount
    print(f"Remaining balance: {balance} AZN")


#Task11
usage = int(input("Monthly usage in kWh: "))
if usage < 0:
    print("Invalid input")
else:
    if usage <= 100:
        rate = 0.08
    elif usage <= 300:
        rate = 0.12
    else:
        rate = 0.15
    bill = usage * rate
    print("Usage:", usage, "kWh")
    print("Applied rate:", rate, "AZN per kWh")
    print("Total bill:", bill, "AZN")


#Task12
startingfee = 2
distance = int(input("Enter the distance: "))
if distance < 0:
    print("Invalid distance")
elif distance <= 5:
    fee = 0.70
elif distance <= 15:
    fee = 0.60
else:
    fee = 0.50
total_fare = startingfee + fee
print("Starting fee:", startingfee, "AZN")
print("Distance fee:", fee, "AZN")
print("Total amount:", total_fare, "AZN")


#Task13
age = int(input("Enter your age: "))
salary = int(input("Enter your monthly salary: "))
amount = int(input("Enter credit amount: "))
if age < 18:
    print("Loan application rejected because you are a minor")
elif salary < 500:
    print("Loan application rejected because your salary is below the minimum requirement.")
elif salary * 10 < amount:
    print("Loan application rejected because the credit amount exceeds the allowed limit.")
else:
    print("Loan application approved.")

#Task14
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if a + b > c:
    if a + c > b:
        if b + c > a:
                if a == b == c:
                    print("Equilateral")
                elif a == b or a == c or b == c:
                    print("Isosceles")
                else:
                    print("Scalene")
        else:
            print("Triangle cannot be created.")
    else:
        print("Triangle cannot be created.")
else:
    print("Triangle cannot be created.")


#Task15
age = int(input("Enter your age: "))
exam = int(input("Enter exam score: "))
school = int(input("Enter school score: "))
if age < 16:
    print("Application rejected.")
elif exam < 0 or exam > 700:
    print("Invalid exam score.")
elif school < 0 or school > 100:
    print("Invalid school score.")
elif exam >= 600:
    print("Scholarship")
elif exam >= 450:
    print("Accepted")
elif exam >= 300:
    if school >= 80:
        print("Accepted")
    else:
        print("Rejected")
else:
    print("Rejected. Exam score is below 300")
