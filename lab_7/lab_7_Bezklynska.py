#task 1
num = (9, 12, 1, 5, 35, 19, 46, 13, 21)
print(num)
n = int(input("Введіть число: "))

result = [numbers for numbers in num if numbers < n]
print("Числа з кортежу, менші за", n, ":", result)

#task 2
words = ("one", "two", "three", "four")
print(words)
result = ", ".join(words)
print(result)

#task 3
library = {
    "The Fault in Our Stars": ("John Michael Green", 2012, 313),
    "Me Before You": ("Jojo Moyes", 2012, 369), 
    "The Notebook": ("Nicholas Sparks", 1996, 214), 
    "Twilight": ("Stephenie Meyer", 2005, 498)
}

book_name = input("Enter the name of the book: ")
print(book_name)

if book_name in library:
    author, year, pages = library[book_name]
    print(f"Author: {author}")
    print(f"Year: {year}")
    print(f"Pages: {pages}")
else:
    print("Sorry, this book is not available in the library.")

#task 4
students = {
    "Rose": ("Emily", 20, "Literature"),
    "Storm": ("Lilith", 22, "Astronomy"),
    "Dream": ("Lileya", 19, "Art History"),
    "Moon": ("Astra", 21, "Philosophy"),
    "Nova": ("Selena", 23, "Physics")
}

surname = input("Enter the student's surname: ")

if surname in students:
    name, age, faculty = students[surname]
    print(f"Name: {name}\nAge: {age}\nFaculty: {faculty}")
else:
    print("No student found with that nickname!")

#task 5
phonebook = {
    "Ivan": ("098-123-45-67", "096-987-65-43"),
    "Olena": ("063-555-66-77",),
    "Mykola": ("098-222-33-44", "096-333-44-55")
}

def add_phone_number(contact_name, new_number):
    if contact_name in phonebook:
        phonebook[contact_name] = phonebook[contact_name] + (new_number,)
    else:
        phonebook[contact_name] = (new_number,)

add_phone_number("Kateryna", "063-444-55-66")

for contact, numbers in phonebook.items():
    print(f"{contact}: {', '.join(numbers)}")