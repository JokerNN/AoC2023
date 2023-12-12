def calculate_ways_to_win(time, record_distance):
    ways_to_win = 0
    for hold_time in range(time):
        speed = hold_time
        remaining_time = time - hold_time
        distance = speed * remaining_time
        if distance > record_distance:
            ways_to_win += 1
    return ways_to_win

# Test the function with the provided example
races_tst = [(7, 9), (15, 40), (30, 200)]
# Time:        50     74     86     85
# Distance:   242   1017   1691   1252
races = [(50, 242), (74, 1017), (86, 1691), (85, 1252)]


ways_to_win_per_race = [calculate_ways_to_win(time, record) for time, record in races]
total_ways_to_win = 1
for ways in ways_to_win_per_race:
    total_ways_to_win *= ways

# print(total_ways_to_win, ways_to_win_per_race)
print(f"Answer 1: {total_ways_to_win}")

race = (50748685, 242101716911252)

ways_to_win = calculate_ways_to_win(race[0], race[1])

print(f"Answer 2: {ways_to_win}")