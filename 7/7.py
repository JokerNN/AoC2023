from collections import Counter
from utils.input import get_input_lines
from typing import List
from pprint import pprint

class Hand:
    def __init__(self, cards: List[str], bid: int):
        self.cards: List[str] = cards
        self.cards_value: List[int]
        self.type: int = 0
        self.bid: int = bid

    def __str__(self):
        return f"Hand(cards={self.cards}, bid={self.bid}, type={self.type})"
    
    def __repr__(self):
        return self.__str__()

def evaluate_hand(hand: Hand) -> None:
    """ Evaluate the hand and return its type and ranks of the cards """
    ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    cards = [ranks[card] for card in hand.cards]
    counts = Counter(cards)
    
    # Determine the type of hand
    if 5 in counts.values():
        hand_type = 1  # Five of a kind
    elif 4 in counts.values():
        hand_type = 2  # Four of a kind
    elif 3 in counts.values() and 2 in counts.values():
        hand_type = 3  # Full house
    elif 3 in counts.values():
        hand_type = 4  # Three of a kind
    elif list(counts.values()).count(2) == 2:
        hand_type = 5  # Two pair
    elif 2 in counts.values():
        hand_type = 6  # One pair
    else:
        hand_type = 7  # High card

    # Sort cards by frequency and then by rank
    hand.cards_value = cards
    hand.type = hand_type

def evaluate_hand2(hand: Hand) -> None:
    """ Evaluate the hand and return its type and ranks of the cards """
    ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 1, 'Q': 12, 'K': 13, 'A': 14}
    cards = [ranks[card] for card in hand.cards]
    counts = Counter(cards)
    
    if counts[1] == 5:
        pass
    else:
        most_common_card = counts.most_common(1)[0][0]
        if most_common_card == 1:
            most_common_card = counts.most_common(2)[1][0]
        counts[most_common_card] += counts[1]
        counts[1] = 0
    # Determine the type of hand
    if 5 in counts.values():
        hand_type = 1  # Five of a kind
    elif 4 in counts.values():
        hand_type = 2  # Four of a kind
    elif 3 in counts.values() and 2 in counts.values():
        hand_type = 3  # Full house
    elif 3 in counts.values():
        hand_type = 4  # Three of a kind
    elif list(counts.values()).count(2) == 2:
        hand_type = 5  # Two pair
    elif 2 in counts.values():
        hand_type = 6  # One pair
    else:
        hand_type = 7  # High card

    # Sort cards by frequency and then by rank
    hand.cards_value = cards
    hand.type = hand_type


def calculate_winnings(hands):
    for hand in hands:
        evaluate_hand(hand)

    hands.sort(key= lambda hand: (-hand.type, hand.cards_value))
    # pprint(hands)
    res = 0
    rank = 1
    for hand in hands:
        res += hand.bid * rank
        rank += 1

    return res


def calculate_winnings2(hands):
    for hand in hands:
        evaluate_hand2(hand)

    hands.sort(key= lambda hand: (-hand.type, hand.cards_value))
    # pprint(hands)
    res = 0
    rank = 1
    for hand in hands:
        res += hand.bid * rank
        rank += 1

    return res



def solve(filename):
    hands = []
    for line in get_input_lines(filename):
        _h = line.split()
        hand = Hand(_h[0], int(_h[1]))

        hands.append(hand)
    
    return calculate_winnings(hands)


print("Answer 1 test: ", solve('7_tst.txt'))
print("Answer 1: ", solve('7.txt'))

def solve2(filename):
    hands = []
    for line in get_input_lines(filename):
        _h = line.split()
        hand = Hand(_h[0], int(_h[1]))

        hands.append(hand)
    
    return calculate_winnings2(hands)

print("Answer 2 test: ", solve2('7_tst.txt'))
print("Answer 2: ", solve2('7.txt'))

