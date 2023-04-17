inputs = input().split(" ")
first_input = int(inputs[0])
second_input = int(inputs[1])

true_num = 0
for num in range(first_input, second_input + 1):
    square_num = 1
    while True:
        square_num += 1
        if num < square_num**2:
            break
        if num % square_num**2 == 0:
            true_num += 1
            break
print(second_input - first_input - true_num + 1)