try:
    number1 = int(input("Enter the number to divide: "))
    num2 = int(input("Enter the second number: "))

    print(number1 / num2)

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("You cannot divide by zero.")