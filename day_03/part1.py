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


def get_and_remove_full_number(row: list[str], column_number: int) -> int:
    char_on_left = row[column_number - 1]

    while char_on_left.isdigit():
        column_number -= 1
        char_on_left = row[column_number - 1]

    number_str = ''
    char = row[column_number]

    while char.isdigit():
        number_str += char
        row[column_number] = '.'
        column_number += 1
        char = row[column_number]

    return int(number_str)


def find_sum_and_remove_adjacent_numbers(
        three_rows: list[list[str]],
        column_number: int
        ) -> int:
    result = 0

    columns = range(column_number - 1, column_number + 2)

    for row_number, row in enumerate(three_rows):

        for column_number in columns:

            if three_rows[row_number][column_number].isdigit():
                result += get_and_remove_full_number(row, column_number)

    return result


def solution(text_lines: list[str]) -> int:
    result = 0

    grid = create_grid(text_lines)

    for row_number, row in enumerate(grid):

        for column_number, char in enumerate(row):

            if is_symbol(char):
                result += find_sum_and_remove_adjacent_numbers(
                    grid[row_number-1:row_number+2],
                    column_number)

    return result


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    result = solution(lines)

    print(result)
