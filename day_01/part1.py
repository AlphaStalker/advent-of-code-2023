def get_number_out_of_line(line: str) -> int:
    result = 0

    for char in line:
        if char.isdigit():
            result += 10 * int(char)
            break

    for char in line[::-1]:
        if char.isdigit():
            result += int(char)
            break

    return result


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
