def get_game_number(game_str: str) -> int:
    return int(game_str.split()[-1])


def get_known_cubes_amount(draws_str: str) -> dict[str, int]:
    cubes_in_bag = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    draws = draws_str.split('; ')

    for draw in draws:
        cubes = draw.split(', ')

        for single_color_cubes in cubes:
            amount_str, color = single_color_cubes.split()

            amount = int(amount_str)

            if cubes_in_bag[color] < amount:
                cubes_in_bag[color] = amount

    return cubes_in_bag


def is_game_possible(known_cubes_in_bag: dict[str, int]) -> bool:
    max_cubes_in_bag = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    for color, max_amount in max_cubes_in_bag.items():
        if known_cubes_in_bag[color] > max_amount:
            return False

    return True


def get_single_game_result(line: str) -> int:
    game_str, draws_str = line.split(': ')

    game_number = get_game_number(game_str)

    known_cubes_amount = get_known_cubes_amount(draws_str)

    if is_game_possible(known_cubes_amount):
        return game_number

    return 0


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
