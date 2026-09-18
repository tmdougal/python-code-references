userInputtedNumbers = []
count = 0
total = 0

def input_number():
    while True:
        try:
            x = input("Enter a number or press Enter to quit: ")
            if x == "":
                return x
            else:
                x = float(x)
                return x
        except ValueError:
            print("ERROR: Please enter a real number or press Enter to quit.")

while True:
    userInput = input_number()
    if userInput == '':
        break
    else:
        userInputtedNumbers.append(userInput)
        count += 1

for num in userInputtedNumbers:
    total += num

if count == 0:
    print("No numbers entered.")
    input("Press enter to exit.")
    exit
else:
    average = total / count
    print("The sum is", + total)
    print("The average is", + average)

