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
    'four': 4,
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
        occurences.extend([(m.start(), str(figure))
                          for m in re.finditer(str(figure), line)])

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



def sum_calibration_values_with_overlap(input_data):
    word_to_digit = {
        "one": "1", 
        "two": "2", 
        "three": "3", 
        "four": "4", 
        "five": "5",
        "six": "6", 
        "seven": "7", 
        "eight": "8", 
        "nine": "9"
    }

    total_sum = 0

    for line in input_data:
        digits_found = []

        # Search for all number words and digits in the line
        for word, digit in word_to_digit.items():
            for match in re.finditer(word, line):
                digits_found.append((match.start(), digit))
        # Also search for numerical digits
        for match in re.finditer(r'\d', line):
            digits_found.append((match.start(), match.group()))
        # Sort the found digits by their position in the line
        digits_found.sort(key=lambda x: x[0])
        # Identify the first and last number word/digit found
        if digits_found:
            first_digit = digits_found[0][1]
            last_digit = digits_found[-1][1]
            total_sum += int(first_digit + last_digit)

    return total_sum


# Calculate the sum for Part Two
input_part_two = lines
result_part_two = sum_calibration_values_with_overlap(input_part_two)

print("The sum of all calibration values for Part Two is:", result_part_two)