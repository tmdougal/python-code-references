def input_number():
    while True:
        try:
            x = input("Enter a number or press Enter to quit: ")
            if x == "":
                x = float(0.0)
                return x
            else:
                x = float(x)
                return x
        except ValueError:
            print("ERROR: Please enter a real number or press Enter to quit.")

num1 = input_number()
num2 = input_number()
num3 = input_number()
num4 = input_number()

sum = num1 + num2 + num3 + num4
average = sum / 4

print("The sum is", + sum)
print("The average is", + average)
