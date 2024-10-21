#task 1
n = int(input("Введіть значення n: "))
print(n >= 100)

n = int(input("Введіть значення n: "))
print(n >= 100)

n = int(input("Введіть значення n: "))
print(n >= 100)

#task 2
a = int(input("Введіть значення a: "))
b = int(input("Введіть значення b: "))

if a > b:
    print(f"Значення {a} > {b}")
else:
    print(f"Значення {a} < {b}")

#task 3
string = input("Введіть рядок: ")
print(string)

if string == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif string == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print(f"Spathiphyllum! Not {string}!")

#task 4
income = float(input("Enter the annual income: "))
print("Your income: ", income)

if income <= 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + (income - 85528) * 0.32

tax = round(tax, 0)

if tax <= 0:
    tax = 0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")

#task 5
year = int(input("Enter a year: "))
print("Year:", year)

if year < 1582:
    print("Not within the Gregorian calendar period!")
elif year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Common year")

#task 6
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

while True:
    guess = int(input("Enter your guess (int number): "))
    print("Guess: ", guess)
    
    if guess == secret_number:
        print(
        """
        +-----------------------------+
        | Молодець, магле!             |
        | Тепер ти вільний!            |
        +-----------------------------+
        """)
        break
    else:
        print(
        """
        +-----------------------------+
        | Ха-ха!        Ви застрягли  |
        |       у моїй петлі!         |
        +-----------------------------+
        """)

#task 7
import time

for i in range(1, 6):
    print(i, "Mississippi")
    time.sleep(1)

print("Ready or not, here I come!")

#task 8
while True:
    word = input("Введи слово: ")
    print("Word: ", word)
    if word == "chupacabra":
        print("You've successfully left the loop.")
        break

#task 9
user_word = input("Please enter a word: ")
user_word = user_word.upper()
print("User word: ", user_word)

for letter in user_word:
    if letter in "AEIOU":
        continue
    print(letter)

#task 10
user_word = input("Please enter a word: ")
user_word = user_word.upper()
word_without_vowels = ""
print("User word: ", user_word)

for letter in user_word:
    if letter in "AEIOU":
        continue
    word_without_vowels += letter

print(word_without_vowels)

#task 11
total_block = int(input("Enter the number of blocks: "))
print("Total blocks: ", total_block)
height = 0
in_progress = 0

while in_progress + (height + 1) <= total_block:
    height += 1
    in_progress += height

print("The height of the pyramid is: ", height)

#task 12
c0 = int(input("Введіть натуральне число: "))
steps = 0

while c0 != 1:
    print(c0)
    if c0 % 2 == 0:
        c0 = c0 // 2 
    else:
        c0 = 3 * c0 + 1 
    steps += 1

print(c0)
print("Кількість кроків:", steps)