def main(b: int, c: int, a_1: int, a_2: int) -> float:
    while True:
        a_3 = b * a_1 + c * a_2

        if a_3 / a_2 == a_2 / a_1:
            return round(a_3 / a_2, 9)

        a_1, a_2, a_3 = a_2, a_3, 0


b, c, a_1, a_2 = map(int, input().split())
print(main(b, c, a_1, a_2))