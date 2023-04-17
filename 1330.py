inputs = input().split(" ")
first_input = int(inputs[0])
second_input = int(inputs[1])

print(((first_input > second_input) and '>') or ((first_input < second_input) and '<') or ((first_input == second_input) and '=='))
