def sub(source, target) -> int:
    if target == source: return 0
    else: return 1


def levenshtein_distance(source: str, target: str) -> int:
    rows = len(source)
    cols = len(target)

    table = [[0] * (cols + 1) for _ in range(rows + 1)]

    for col in range(cols + 1):
        table[0][col] = col
    for row in range(rows + 1):
        table[row][0] = row

    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            table[row][col] = min(
                table[row - 1][col] + 1,
                table[row][col - 1] + 1,
                table[row - 1][col - 1] + sub(source= source[row - 1], target= target[col - 1])
            )

    return table[rows][cols]


# Unit test
if __name__ == '__main__':
    print(levenshtein_distance(source="yu", target="you"))
    print(levenshtein_distance(source="kitten", target="sitting"))
    print(levenshtein_distance(source="hi", target="hello"))
    print(levenshtein_distance(source="hola", target="hello"))
