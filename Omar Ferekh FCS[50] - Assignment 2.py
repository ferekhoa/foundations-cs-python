# Exercise 1:
number = eval(input("Please enter a number: "))
digits = len(str(number))
print(f"In the number " ,number ," there is " ,digits, "digits")


# Exercise 2:
number = eval(input("Please enter a number: "))
i = j = 0
for i in range(number):
    for j in range(i+1):
        print("*", end="")
    print()


# Exercise 3:
list1 = [54,76,2,4,98,100]
number1 = int(input("Please enter the first number: "))
number2 = int(input("Please enter the second number: "))
for value in list1:
    if number1 < value < number2:
        print(value)


# Exercise 4:
Names = ["Maria","Hala","Ghady","Ehsan","Joe","Zoe"]
while True:
    letter = input("Please enter your letter or e to exit: ")
    if letter == "e":
        break
    for name in Names:
        if letter in name.lower():
            print(name)
        else:
            print("There is no names that contain the letter", letter)
            break





