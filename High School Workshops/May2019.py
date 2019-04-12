# A line with a hashtag is a "comment"; it's greyed-out and does nothing.
# We'll use them to leave you notes and instructions below!


# 1) OUTPUT: first, we want the computer to show us some text

print("Hello, World!")

# 2) VARIABLES: we can use variables like sticky notes to hold data for us

message = "My favorite color is green"
print(message)

# TODO: talk about different types, e.g. int and str

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
else:
  print("Sorry, wrong answer.")

# 6) CALCULATOR: time to combine everything you've learned to make a simple calculator!

# TODO