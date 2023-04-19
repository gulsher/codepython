try:
    value = 10/0
    number = int(input("Enter the number: "))
    print(number)
except ValueError:
    print("Invalid input")
except ZeroDivisionError as e:
    print("divide by zero", e)