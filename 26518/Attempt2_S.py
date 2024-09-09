from math import sqrt

def main(b: int, c: int, a_1: int, a_2: int) -> float:
    return (b + sqrt(b * b + 4 * c)) / 2

b, c, a_1, a_2 = map(int, input().split())
print(f"{main(b, c, a_1, a_2):.9f}")