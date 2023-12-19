from part1 import get_our_winning_numbers_count


def add_cards_won(
        cards_count: list[int],
        cards_to_add: int,
        won_card_index: int
        ) -> None:
    number_of_copies = cards_count[won_card_index]

    for i in range(1, cards_to_add+1):
        if won_card_index + i > len(cards_count):
            break

        cards_count[won_card_index + i] += number_of_copies


def solution(text_lines: list[str]) -> int:
    cards_count = [1 for _ in range(len(text_lines))]

    for card_index, line in enumerate(text_lines):
        our_winning_numbers_count = get_our_winning_numbers_count(line)

        add_cards_won(cards_count, our_winning_numbers_count, card_index)

    return sum(cards_count)


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    result = solution(lines)

    print(result)
