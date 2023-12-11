from utils.input import get_input_lines

def sum_part_numbers(schematic):
    def is_valid(x, y, rows, cols):
        return 0 <= x < rows and 0 <= y < cols

    def has_adjacent_symbol(x, y, grid):
        directions = [(dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if not (dx == 0 and dy == 0)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, len(grid), len(grid[0])) and grid[nx][ny] != '.' and grid[nx][ny] not in digit_set:
                return True
        return False

    symbols = set("*#$+/=-@&")
    digit_set = set("0123456789")
    total_sum = 0

    # Iterate over each cell in the grid
    for i, row in enumerate(schematic):
        j = 0
        while j < len(row):
            char = row[j]
            # Check if the current cell is a digit
            if char.isdigit():
                number_str = char
                k = j + 1
                # Check for multi-digit numbers
                while k < len(row) and row[k].isdigit():
                    number_str += row[k]
                    k += 1
                
                # Check if any part of the number is adjacent to a symbol
                number_adjacent_to_symbol = any(
                    has_adjacent_symbol(i, jj, schematic) for jj in range(j, k)
                )

                if number_adjacent_to_symbol:
                    total_sum += int(number_str)

                j = k  # Skip past the current number
            else:
                j += 1

    return total_sum


schematics = get_input_lines('./3.txt')
# Test again with the provided example
print(f"Answer 1: {sum_part_numbers(schematics)}")
