from math import floor

def main(string: str):
    max_palindrome_length = len(string)
    rest_string_length = 0

    for index in range(len(string)):
        if is_palindrome(string[index:]):
            max_palindrome_length = len(string[index:])
            rest_string_length = len(string[:index])
            break

    return max_palindrome_length + rest_string_length * 2

def is_palindrome(string: str) -> bool:
    for index in range(floor(len(string) / 2)):
        if string[index] != string[len(string) - 1 - index]:
            return False

    return True

string = input()
print(main(string))