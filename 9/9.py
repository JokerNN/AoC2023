from utils.input import get_input_lines

def calculate_differences(sequence):
    """Calculate differences between consecutive elements of a sequence."""
    return [sequence[i+1] - sequence[i] for i in range(len(sequence) - 1)]


def extrapolate_next_value(history):
    """Extrapolate the next value in the history with the correct approach."""
    sequences = [history]
    while not all(d == 0 for d in sequences[-1]):
        sequences.append(calculate_differences(sequences[-1]))
    
    # Extrapolate from the bottom sequence upwards
    for i in range(len(sequences) - 2, -1, -1):
        sequences[i].append(sequences[i][-1] + sequences[i + 1][-1])
    
    return sequences[0][-1]

def sum_extrapolated_values(histories):
    """Sum the extrapolated next values of each history with the corrected approach."""
    return sum(extrapolate_next_value(history) for history in histories)


def solve(filename):
    lines = get_input_lines(filename)
    histories = [
        [int(n) for n in line.split()] for line in lines
    ]
    return sum_extrapolated_values(histories)

print("Answer 1 tst: ", solve('./9_tst.txt'))
print("Answer 1: ", solve('./9.txt'))


def extrapolate_previous_value(history):
    """Extrapolate the previous value in the history."""
    sequences = [history]
    while not all(d == 0 for d in sequences[-1]):
        sequences.append(calculate_differences(sequences[-1]))
    
    # Extrapolate from the bottom sequence upwards, adding a new zero at the beginning
    for i in range(len(sequences) - 2, -1, -1):
        sequences[i].insert(0, sequences[i][0] - sequences[i + 1][0])
    
    return sequences[0][0]

def sum_extrapolated_previous_values(histories):
    """Sum the extrapolated previous values of each history."""
    return sum(extrapolate_previous_value(history) for history in histories)



def solve2(filename):
    lines = get_input_lines(filename)
    histories = [
        [int(n) for n in line.split()] for line in lines
    ]
    return sum_extrapolated_previous_values(histories)

print("Answer 2 tst: ", solve2('./9_tst.txt'))
print("Answer 2: ", solve2('./9.txt'))
# Test with the provided example
