num1 = int(input("give one number: "))
num2 = int(input("give another number: "))
operation = input("choose operator: add, sub, mul, div ")

if operation == "add":
    print(f"Addition of 2 numbers is {num1+num2}")
elif operation == "sub":
    print(f"Subtraction of 2 numbers is {num1-num2}")
elif operation == "mul":
    print(f"Multipication of 2 numbers is {num1*num2}")
elif operation == "div":
    print(f"Division of 2 numbers is {num1/num2}")
else:
    print("give correct input")