
from pprint import pprint
import sys
# sys.path.append('/Users/ataktaev/Documents/AoC2023')
pprint(sys.path)


from utils.input import get_input_lines
import re

lines = get_input_lines('input.txt')

s = 0
for line in lines:
    res = re.sub(r'[a-zA-Z]*', '', line, 0)
    # print(res)
    try:
        s += int(res[0] + res[-1])
    except IndexError:
        pass

print(f"Answer 1: {s}")


m = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four':4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


s = 0
for line in lines:
    occurences = []
    for text, figure in m.items():
        occurences.extend([(m.start(), text) for m in re.finditer(text, line)])
        occurences.extend([(m.start(), str(figure)) for m in re.finditer(str(figure), line)])

    occurences = [o for o in occurences if o[0] != -1]
    occurences.sort(key=lambda o: o[0])
    first_digit = occurences[0][1]
    last_digit = occurences[-1][1]
    if first_digit in m:
        first_digit = str(m[first_digit])
    if last_digit in m:
        last_digit = str(m[last_digit])

    s += int(first_digit + last_digit)

print(f'Answer 2: {s}')