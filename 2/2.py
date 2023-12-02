import re
from utils.input import get_input_lines

lines = get_input_lines('./2.txt')
game_re = re.compile(r'Game (?P<id>\d+)')
throw_re = re.compile(r'(?P<count>\d+) (?P<color>\w+)')

limits = {
    'red': 12,
    'green': 13,
    'blue': 14
}

s = 0

for line in lines:
    game, throws_str = line.split(':')
    game_id = int(game_re.match(game)['id'])
    throws = throws_str.split(';')
    possible = True
    for throw in throws:
        results = throw_re.findall(throw)
        for res in results:
            color = res[1]
            count = int(res[0])
            if count > limits[color]:
                possible = False
                break
    if possible:
        s += game_id

print(f"Answer 1: {s}")

s = 0
for line in lines:
    game, throws_str = line.split(':')
    game_id = int(game_re.match(game)['id'])
    throws = throws_str.split(';')
    possible = True
    maxs = {
        'red': float('-inf'),
        'green': float('-inf'),
        'blue': float('-inf')
    }
    for throw in throws:
        results = throw_re.findall(throw)
        for res in results:
            color = res[1]
            count = int(res[0])
            maxs[color] = max(maxs[color], count)
    s += maxs['red'] * maxs['green'] * maxs['blue']

print(f"Answer 2: {s}")
