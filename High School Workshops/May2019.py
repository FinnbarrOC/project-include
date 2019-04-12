# A line with a hashtag is a "comment"; it's greyed-out and does nothing.
# We'll use them to leave you notes and instructions below!


# 1) OUTPUT: first, we want the computer to show us some text

print("Hello, World!")

# 2) VARIABLES: we can use variables like sticky notes to hold data for us

message = "My favorite color is green"  # str
print(message)
number = 42   # int
print("My favorite number is " + str(number)) # Converting types

# 3) INPUT: now let's type a message to the computer, save it, and print it back out

name = input("Type your name, then press Enter: ")
print(name)   # Start by simply printing name
print("My friend " + name + " is learning to code!")  # Then insert name into a message

# 4) MATH: try some simple addition/subtraction, then see how fast your computer really is!

print(2 + 3)
print(12 * 12)
print(33432 / 596)
print(25**25)   # The double-star stands for exponentation

# 5) IF/ELSE: this is how your computer makes simple decisions based on "True" or "False"

number = int(input("What number do you choose? "))
if (number < 0):
  print(str(number) + " is a negative number")
else:
  print(str(number) + " is a positive number")

answer = input("Say my name, and I disappear. What am I? ")
if (answer == "silence"):
  print("You solved my riddle!")
elif (answer == "Silence"):     # "elif" short for "else if"
  print("You solved my riddle!")
else:
  print("Sorry, wrong answer.")

# 6) CALCULATOR: time to combine everything you've learned to make a simple calculator!

number1 = int(input("What is the first number? "))
number2 = int(input("What is the second number? "))
operation = input("Would you like to add or subtract? ")

if (operation == "add"):
  print(number1 + number2)
else:
  print(number1 - number2)

# 7) WHILE LOOPS: this is how we can make some lines of code run multiple times, or forever

while(True):
  number1 = int(input("What is the first number? "))
  number2 = int(input("What is the second number? "))
  operation = input("Would you like to add, subtract, or quit? ")

  if (operation == "quit"):
    print("Goodbye")
    break
  elif (operation == "add"):
    print(number1 + number2)
  else:
    print(number1 - number2)

# 8) FOR LOOPS: this is another way to run code multiple times; this should get interesting
  # (you can learn about factorials here: https://en.wikipedia.org/wiki/Factorial)

number = int(input("What number should we find the factorial of? "))
total = 1
for x in range(1, number + 1):  # Check for off-by-one errors here
  total = total * x

print("The factorial of " + str(number) + " =")
print(total)