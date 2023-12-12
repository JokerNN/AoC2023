from utils.input import get_input_blob
import re


input = get_input_blob('5.txt')
seeds_str = re.match(r'seeds: (.+\n)', input)
seeds = [int(n) for n in seeds_str.group(1).split(' ')]

seed_to_soil_str = re.search(r'seed-to-soil map:\n([\n\d\s]+)\n\n', input, re.MULTILINE)
seed_to_soil_map = [tuple(map(int, line.split())) for line in seed_to_soil_str.group(1).splitlines()]

soil_to_fertilizer_str = re.search(r'soil-to-fertilizer map:\n([\n\d\s]+)\n\n', input, re.MULTILINE)
soil_to_fertilizer_map = [tuple(map(int, line.split())) for line in soil_to_fertilizer_str.group(1).splitlines()]

fertilizer_to_water_str = re.search(r'fertilizer-to-water map:\n([\n\d\s]+)\n\n', input, re.MULTILINE)
fertilizer_to_water_map = [tuple(map(int, line.split())) for line in fertilizer_to_water_str.group(1).splitlines()]

water_to_light_str = re.search(r'water-to-light map:\n([\n\d\s]+)\n\n', input, re.MULTILINE)
water_to_light_map = [tuple(map(int, line.split())) for line in water_to_light_str.group(1).splitlines()]

light_to_temperature_str = re.search(r'light-to-temperature map:\n([\n\d\s]+)\n\n', input, re.MULTILINE)
light_to_temperature_map = [tuple(map(int, line.split())) for line in light_to_temperature_str.group(1).splitlines()]

temperature_to_humidity_str = re.search(r'temperature-to-humidity map:\n([\n\d\s]+)\n\n', input, re.MULTILINE)
temperature_to_humidity_map = [tuple(map(int, line.split())) for line in temperature_to_humidity_str.group(1).splitlines()]

humidity_to_location_str = re.search(r'humidity-to-location map:\n([\n\d\s]+)\n', input, re.MULTILINE)
humidity_to_location_map = [tuple(map(int, line.split())) for line in humidity_to_location_str.group(1).splitlines()]

maps_order = [seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map]


def map_value(value, mapping):
    for dest_start, src_start, length in mapping:
        if src_start <= value < src_start + length:
            return dest_start + (value - src_start)
    return value


def process_maps2(seed, maps):
    for mapping in maps:
        seed = map_value(seed, mapping)
    return seed

def traceback_validation(value, seeds, maps):
    for m in reversed(maps):
        for dest_start, src_start, l in m:
            if value >= dest_start and value < dest_start + l:
                value = value + (src_start - dest_start)
                break
    
    for idx in range(0, len(seeds), 2):
        r_start = seeds[idx]
        l = seeds[idx + 1]
        if value >= r_start and value <= r_start + l:
            return True
        
    return False
    

def solve_part_1(seeds):
    ms = float('inf')
    for sid in seeds:
        val = process_maps2(sid, maps_order)
        ms = min(ms, val)
    return ms


def solve_part_2(seeds, maps):
    answer = float('inf')

    for idx in range(0, len(seeds), 2):
        seed_start = seeds[idx]
        inc = seeds[idx + 1]
        res = process_maps2(seed_start, maps_order)
        answer = min(answer, res)
    print(f'Seeds answer: {answer}')

    for idx in range(len(maps)):
        for dest_start, src_start, length in maps[idx]:
            res = process_maps2(src_start, maps[idx:])
            if traceback_validation(src_start, seeds, maps[:idx]):
                answer = min(answer, res)

    return answer
    

print(f"Answer 1: {solve_part_1(seeds)}")

# Parse the seed ranges from the modified input string
res = solve_part_2(seeds, maps_order)

# Calculate the lowest location number for these seeds
# lowest_location_number = solve(seeds, seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map)
print(f"Answer 2: {res}")
