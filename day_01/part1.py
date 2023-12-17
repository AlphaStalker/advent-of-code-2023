def solution(text_lines: list[str]) -> int:
    result = 0

    for line in text_lines:

        for char in line:
            if char.isdigit():
                result += 10 * int(char)
                break
        
        for char in line[::-1]:
            if char.isdigit():
                result += int(char)
                break

    return result


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    result = solution(lines)

    print(result)
