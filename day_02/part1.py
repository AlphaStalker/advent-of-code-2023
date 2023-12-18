MAX_CUBES_IN_BAG = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def get_cubes(line: str):  # TODO: Rename
    game_str, cubes_str = line.split(': ')

    game_number = int(game_str.split()[-1])

    draws = cubes_str.split('; ')

    CUBES_WE_KNOW = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    for draw in draws:
        colors = draw.split(', ')
        for color in colors:
            count, key = color.split()
            if CUBES_WE_KNOW[key] < int(count):
                CUBES_WE_KNOW[key] = int(count)

    for key, value in MAX_CUBES_IN_BAG.items():
        if CUBES_WE_KNOW[key] > value:
            return 0

    return game_number


def solution(text_lines: list[str]) -> int:
    result = 0

    for line in text_lines:
        result += get_cubes(line)

    return result


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    result = solution(lines)

    print(result)
