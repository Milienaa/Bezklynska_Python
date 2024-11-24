#task 1
def is_hidden_word(word, text):
    index = 0
    for char in word:
        index = text.find(char, index)
        if index == -1:
            return "No"
        index += 1
    return "Yes"

word_input = input("Enter the word to check: ").strip()
text_input = input("Enter the text to search in: ").strip()

result = is_hidden_word(word_input, text_input)
print(result)

#task 2
def calculate_life_number(date):
    digits = ''.join(filter(str.isdigit, date))
    digit_sum = sum(int(d) for d in digits)

    while digit_sum > 9:
        digit_sum = sum(int(d) for d in str(digit_sum))

    return digit_sum


while True:
    try:
        date = input("Введіть дату народження у форматі РРРРММДД, РРРРДДММ або ММДДРРРР: ")

        cleaned_date = ''.join(filter(str.isdigit, date))

        if len(cleaned_date) < 8:
            raise ValueError("Дата має бути не менше 8 цифр!")

        print(f"Ви ввели дату: {cleaned_date}")
        life_number = calculate_life_number(cleaned_date)
        print("Цифра життя для дати {}: {}".format(cleaned_date, life_number))
        break
    except ValueError as ve:
        print(f"Помилка: {ve} Спробуйте ще!")
    except Exception as e:
        print(f"Невідома помилка: {e} Спробуйте ще!")

#task 3
def get_number(message, lower_limit, upper_limit):
    while True:
        try:
            num = int(input(message))
            if num < lower_limit or num > upper_limit:
                print(f"Error: the value is not within permitted range ({lower_limit}..{upper_limit}).")
            else:
                return num
        except ValueError:
            print("Error: wrong input!")

message = input("Enter the message for the prompt: ")
lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))

result = get_number(message, lower_limit, upper_limit)
print(f"Entered: {result}")