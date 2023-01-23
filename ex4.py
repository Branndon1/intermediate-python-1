sum = 0
for i in range(5):
    while True:
        try:
            num = int(input("Enter an int: "))
            break
        except ValueError:
            print("Invalid input. Please enter an int.")
    sum += num
print("The sum of the integers is:", sum)