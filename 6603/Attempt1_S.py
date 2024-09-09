from typing import List, Tuple

MAX_LENGTH = 6

def main(test_cases: List[Tuple[int, List[int]]]):

    def print_test_case(test_case: Tuple[int, List[int]]):
        print_recursive([], -1, test_case)

    def print_recursive(sequence: List[int], index: int, test_case: Tuple[int, List[int]]):
        if len(sequence) == MAX_LENGTH:
            print(*sequence)
            return

        next_index = index + 1
        if next_index == len(test_case[1]):
            return

        print_recursive(sequence + [test_case[1][next_index]], next_index, test_case)
        print_recursive(sequence, next_index, test_case)

    for index in range(len(test_cases)):
        print_test_case(test_cases[index])
        if index != len(test_cases): print("")


def process_input() -> List[Tuple[int, List[int]]]:
    test_cases = []
    while True:
        line = input().strip()
        if line == "0": break

        numbers = list(map(int, line.split()))
        k = numbers[0]
        sequence = numbers[1:]

        test_cases.append((k, sequence))

    return test_cases

test_cases = process_input()
main(test_cases)