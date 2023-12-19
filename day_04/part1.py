def get_numbers_out_of_numbers_str(numbers_str: str) -> list[int]:
    return [int(num) for num in numbers_str.split()]


def count_winning_numbers_we_have(
        winning_nums: list[int],
        our_nums: list[int]
        ) -> int:
    our_winning_numbers = [num for num in our_nums if num in winning_nums]

    return len(our_winning_numbers)


def calculate_value(winning_numbers_count: int) -> int:
    return int(2 ** (winning_numbers_count - 1))


def get_card_value(line: str) -> int:
    numbers = line.split(': ')[1]

    winning_numbers_str, our_numbers_str = numbers.split(' | ')

    winning_numbers = get_numbers_out_of_numbers_str(winning_numbers_str)
    our_numbers = get_numbers_out_of_numbers_str(our_numbers_str)

    our_winning_numbers_count = \
        count_winning_numbers_we_have(winning_numbers, our_numbers)

    return calculate_value(our_winning_numbers_count)


def solution(text_lines: list[str]) -> int:
    result = 0

    for line in text_lines:
        result += get_card_value(line)

    return result


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    result = solution(lines)

    print(result)
