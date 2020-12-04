# Quiz Game
# Author: Roydan Chu
# Date: December 4 2020

# Create a tally
total = 0

# Greet the user
greet = input("Hi, are you ready for a quiz?").lower()
if greet == "yes":
    print("Great")
else:
    print("Ok, I'll quiz you anyway")

# Ask first question
first_question = int(input("What is 2*2?: "))
if first_question == 4:
    total += 1
    print(f"Nice, your score is {total}/5")
else:
    print(f"Wrong, your score is {total}/5")

# Ask second question
print("Which is the largest island?")
second_question = input("A: Greenland, B: Hawaii, C: Australia: ").lower()
if second_question == "a":
    total += 1
    print(f"Nice, your score is {total}/5")
else:
    print(f"Wrong, your score is {total}/5")

# Ask third question
third_question = input("What is the capital of Greece?: ").lower()
if third_question == "athens":
    total += 1
    print(f"Nice, your score is {total}/5")
else:
    print(f"Wrong, your score is {total}/5")

# Ask fourth question
print("What is 3^7?")
fourth_question = input("A: 2871, B: 2718, C: 2187: ").lower()
if fourth_question == "c":
    total += 1
    print(f"Nice, your score is {total}/5")
else:
    print(f"Wrong, your score is {total}/5")

# Ask fifth question
print("Which team are the 2020 NBA champs?")
fifth_question = input("A: Warriors, B: Lakers, C: Celtics: ").lower()
if fifth_question == "b":
    total += 1
    print(f"Nice, your final score is {total}/5")
else:
    print(f"Wrong, your final score is {total}/5")

# Closing line
if total == 5:
    print("Aced!")
elif total == 0:
    print("You got it next time")
else:
    print("Well done!")