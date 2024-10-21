#task 1
pi = 3.141592653589793
e = 2.718281828459045

x = float(input("Введіть значення x:\n"))
mu = float(input("Введіть значення середнього (mu):\n"))
sigma = float(input("Введіть значення стандартного відхилення (sigma):\n"))

k = 1 / (sigma * ((2 * pi) ** 0.5))
exponent = e ** (-((x - mu) ** 2) / (2 * sigma ** 2))
result = k * exponent
print(f"Функція Гауса для x = {x}, mu = {mu}, sigma = {sigma}:\n{result}")

#task 2
john = 3
mary = 5
adam = 6

print(f"John = {john}", f"Mary = {mary}", f"Adam = {adam}", sep=(", "))

totalApples = john + mary + adam
print(totalApples)

print(f"Загальна кількість яблук: {totalApples}")

#task 3
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

#task 4
x = 3
x = float(x)
y = 3 * x ** 3 - 2 * x **2 + 3 ** x - 1
print("y =", y)

#task 5
# this program computes the number of seconds in a given number of hours
hours = 2 # number of hours
seconds = 3600 # number of seconds in 1 hour
hours_to_seconds = hours * seconds

print(f"Hours: {hours}\nSeconds in given hours: {hours_to_seconds}")
print("Goodbye!")

#task 6
a = float(input("Enter the first number 'a': "))
b = float(input("Enter the first number 'b': "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

print("\nThat's all, folks!")

#task 7
x = float(input("Enter value for x: "))

y = 1 / (x + 1 / (x + 1 / (x + 1 / x)))

print("y =", y)

#task 8
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

hour_to_mins = hour * 60 + mins
total_mins = hour_to_mins + dura
finish_hour = round(total_mins / 60) % 24
finish_mins = total_mins % 60

print(f"{finish_hour}:{finish_mins}")