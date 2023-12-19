from part1 import create_grid


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


def is_gear(adjacent_numbers: list[int]) -> bool:
    return len(adjacent_numbers) == 2


def get_gear_ratio(three_rows: list[list[str]], column_number: int) -> int:
    adjacent_numbers = []

    columns = range(column_number - 1, column_number + 2)

    for row_number, row in enumerate(three_rows):

        for column_number in columns:

            if three_rows[row_number][column_number].isdigit():
                number = get_and_remove_full_number(row, column_number)
                adjacent_numbers.append(number)

    if is_gear(adjacent_numbers):
        return adjacent_numbers[0] * adjacent_numbers[1]

    return 0


def solution(text_lines: list[str]) -> int:
    result = 0

    grid = create_grid(text_lines)

    for row_number, row in enumerate(grid):

        for column_number, char in enumerate(row):

            if char == '*':
                result += get_gear_ratio(
                    grid[row_number-1:row_number+2],
                    column_number)

    return result


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    result = solution(lines)

    print(result)
