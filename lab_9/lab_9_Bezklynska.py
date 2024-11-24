#example 1
# Написати метод аналогічний split()
def mysplit(string):
    if not string or string.isspace():
        return []

    words = []
    word = ""
    for char in string:
        if char != ' ':
            word += char
        elif word:
            words.append(word)
            word = ""

    if word:
        words.append(word)

    return words

#example 2
number_dict = {
    '1': ('  #', '  #', '  #', '  #', '  #'),
    '2': ('###', '  #', '###', '#  ', '###'),
    '3': ('###', '  #', '###', '  #', '###'),
    '4': ('# #', '# #', '###', '  #', '  #'),
    '5': ('###', '#  ', '###', '  #', '###'),
    '6': ('###', '#  ', '###', '# #', '###'),
    '7': ('###', '  #', '  #', '  #', '  #'),
    '8': ('###', '# #', '###', '# #', '###'),
    '9': ('###', '# #', '###', '  #', '###'),
    '0': ('###', '# #', '# #', '# #', '###')
}

def display_number(num_str):
    for level in range(5):
        for symbol in num_str:
            print(number_dict[symbol][level], end=' ')
        print()

def main():
    while True:
        number_input = input("Введіть ціле число: ").strip()
        if number_input.isdigit():
            display_number(number_input)
            break
        else:
            print("Будь ласка, введіть дійсне ціле невід'ємне число.")

main()

#example 3
# Caesar cipher.
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)

#example 4
# Caesar cipher - decrypting a message.
cipher = input('Enter your cryptogram: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)

#task 1
while True:
    try:
        shift = int(input("Enter shift value(1-25): "))
        if 1 <= shift <= 25:
            break
        else:
            print("Shift value must be between 1-25.")
    except ValueError:
        print("Invalid input. Please enter an integer 1-25.")

print("Shift: ", shift)
text = input("Enter your message: ")
print(text)
cipher = ''

for char in text:
    if char.isalpha():
        start = ord('A') if char.isupper() else ord('a')
        code = start + (ord(char) - start + shift) % 26
        cipher += chr(code)
    else:
        cipher += char

print("Ciphered text:", cipher)