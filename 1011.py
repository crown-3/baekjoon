test_case_count = int(input())
test_input = []

while test_case_count:
    inputs = input().split(" ")
    test_input.append([int(inputs[0]), int(inputs[1])])
    test_case_count -= 1

for test_case in test_input:
    length = test_case[1] - test_case[0]
    count = 0
    while length > 0:
        count += 1
        length -= (count + 1) // 2
    print(count)