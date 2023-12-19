def add_border(text_lines: list[str]) -> list[str]:
    new_lines = []

    for line in text_lines:
        new_lines.append(f'.{line.strip()}.')

    top_bottom_border = '.' * len(new_lines[0])

    new_lines.insert(0, top_bottom_border)
    new_lines.append(top_bottom_border)

    return new_lines


def create_grid(text_lines: list[str]) -> list[list[str]]:
    text_lines = add_border(text_lines)

    return [list(line) for line in text_lines]


def is_symbol(char: str) -> bool:
    return not char.isdigit() and not char == '.'


def solution(text_lines: list[str]) -> int:
    result = 0

    grid = create_grid(text_lines)

    for row_number, row in enumerate(grid):

        for column_number, char in enumerate(row):

            if is_symbol(char):
                pass

    return result


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    result = solution(lines)

    print(result)
