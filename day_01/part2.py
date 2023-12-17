import re


STR_DIGIT_TO_INT = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def get_digit_out_of_str(s: str) -> int:
    try:
        return int(s)
    except:
        return STR_DIGIT_TO_INT[s]


def get_first_digit(line: str) -> int:
    pattern = r'|'.join(STR_DIGIT_TO_INT.keys()) + r'|\d'

    digit_str = re.search(pattern, line)[0]

    return get_digit_out_of_str(digit_str)


def get_last_digit(line: str) -> int:
    reversed_keys = [digit_str[::-1] for digit_str in STR_DIGIT_TO_INT.keys()]
    pattern = r'|'.join(reversed_keys) + r'|\d'

    reversed_digit_str = re.search(pattern, line[::-1])[0]
    digit_str = reversed_digit_str[::-1]

    return get_digit_out_of_str(digit_str)


def get_number_out_of_line(line: str) -> int:
    return 10 * get_first_digit(line) + get_last_digit(line)


def solution(text_lines: list[str]) -> int:
    result = 0

    for line in text_lines:
        result += get_number_out_of_line(line)

    return result


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    result = solution(lines)

    print(result)
