from part1 import get_known_cubes_amount


def calculate_set_of_cubes_power(cubes_in_bag: dict[str, int]) -> int:
    power = 1

    for amount in cubes_in_bag.values():
        power *= amount

    return power


def get_single_game_result(line: str) -> int:
    draws_str = line.split(': ')[-1]

    known_cubes_amount = get_known_cubes_amount(draws_str)

    return calculate_set_of_cubes_power(known_cubes_amount)


def solution(text_lines: list[str]) -> int:
    result = 0

    for line in text_lines:
        result += get_single_game_result(line)

    return result


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    result = solution(lines)

    print(result)
