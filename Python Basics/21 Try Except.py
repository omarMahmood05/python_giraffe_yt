try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Zero Can Not Be Divided")
