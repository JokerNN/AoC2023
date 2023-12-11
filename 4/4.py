import re
from typing import Dict, Set
from utils.input import get_input_lines

s = 0
input_lines = get_input_lines('./4.txt')
for line in input_lines:
    card_id, numbers_str = line.split(':')
    winning_numbers_str, my_numbers_str = numbers_str.split('|')
    winning_numbers = set(int(s) for s in winning_numbers_str.strip().split())
    my_numbers = set(int(s) for s in my_numbers_str.strip().split())
    intersection = my_numbers & winning_numbers
    if len(intersection) > 0:
        s += 2 ** (len(intersection) - 1)

print(f"Answer 1: {s}")


card_re = re.compile(r'Card\s+(\d+)')
cards: Dict[int, Dict[str, Set[int] | int]] = {}
for line in input_lines:
    card_id_str, numbers_str = line.split(':')
    card_id = int(card_re.match(card_id_str)[1])
    winning_numbers_str, my_numbers_str = numbers_str.split('|')
    winning_numbers = set(int(s) for s in winning_numbers_str.strip().split())
    my_numbers = set(int(s) for s in my_numbers_str.strip().split())
    cards[card_id] = {
        'my_numbers': my_numbers,
        'winning_numbers': winning_numbers,
        'count': 1
    }


for card_id in range(1, len(cards) + 1):
    winning_numbers = cards[card_id]['winning_numbers']
    my_numbers = cards[card_id]['my_numbers']
    current_card_count = cards[card_id]['count']
    wins = winning_numbers & my_numbers
    for idx in range(card_id + 1, card_id + len(wins) + 1):
        cards[idx]['count'] += current_card_count


res = sum(card['count'] for card in cards.values())


print(f'Answer 2: {res}')