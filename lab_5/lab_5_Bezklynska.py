#task 1
hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
# Step 2:
user_number = int(input("Enter the number: "))
hat_list[2] = user_number
# Step 2:
del hat_list[-1]
# Step 3:
print("List's length: ", len(hat_list))
print(hat_list)

#task 2
arr = list(map(int, input("Введіть елементи списку через пробіл: ").split()))
print(arr)
n = len(arr)
for i in range(n - 1):
    swapped = False
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
    if not swapped:
        break

print("Відсортований список:", arr)

#task 3
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print(my_list)
unique_arr = []

for num in my_list:
    if num not in unique_arr:
        unique_arr.append(num)

print("The list with unique elements only:")
print(unique_arr)

#task 4
chessboard = [["_" for _ in range(8)] for _ in range(8)]

chessboard[0][0] = "R"
chessboard[0][7] = "R"
chessboard[7][0] = "R"
chessboard[7][7] = "R"

for row in chessboard:
    print(" ".join(row))