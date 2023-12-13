from utils.input import get_input_lines
from typing import Dict, List, Tuple


def parse_map(node_descriptions):
    """ Parse the node descriptions into a map of nodes and their left/right neighbors. """
    map_nodes = {}
    for description in node_descriptions:
        node, neighbors = description.split(" = ")
        left, right = neighbors.strip("()").split(", ")
        map_nodes[node] = (left, right)
    return map_nodes

def navigate_network(instructions: List[str], map_nodes: Dict[str, Tuple[str,str]], start_node = 'AAA', end_node = 'ZZZ') -> int:
    cur_node = start_node
    s = 0
    while True:
        if cur_node == end_node:
            return s
        ins = instructions[s % len(instructions)]
        if ins == 'L':
            cur_node = map_nodes[cur_node][0]
        elif ins == 'R':
            cur_node = map_nodes[cur_node][1]

        s += 1


def navigate_network_debug(instructions: List[str], map_nodes: Dict[str, Tuple[str,str]], start_node = 'AAA', end_node = 'ZZZ') -> int:
    cur_node = start_node
    s = 0
    while True:
        if cur_node.endswith('Z'):
            return s
        ins = instructions[s % len(instructions)]
        if ins == 'L':
            cur_node = map_nodes[cur_node][0]
        elif ins == 'R':
            cur_node = map_nodes[cur_node][1]

        s += 1





def solve(filename):
    inp = get_input_lines(filename)
    instructions = inp[0]
    # Parse the map
    map_nodes = parse_map(inp[2:])

    return navigate_network(instructions, map_nodes)

print("Answer 1 tst: ", solve('./8_tst.txt'))
print("Answer 1: ", solve('./8.txt'))

def navigate_network2(instructions: List[str], map_nodes: Dict[str, Tuple[str,str]]) -> int:
    cur_nodes = []
    for node in map_nodes.keys():
        if node.endswith('A'):
            cur_nodes.append(node)

    s = 0
    while True:
        if all(node.endswith('Z') for node in cur_nodes):
            return s
        ins = instructions[s % len(instructions)]
        for idx, node in enumerate(cur_nodes):
            if ins == 'L':
                cur_nodes[idx] = map_nodes[node][0]
            elif ins == 'R':
                cur_nodes[idx] = map_nodes[node][1]
        
        s += 1
    


def solve2(filename):
    inp = get_input_lines(filename)
    instructions = inp[0]
    # Parse the map
    map_nodes = parse_map(inp[2:])

    print(navigate_network_debug(instructions, map_nodes, 'DRA'))
    print(navigate_network_debug(instructions, map_nodes, 'AAA'))
    print(navigate_network_debug(instructions, map_nodes, "CMA"))
    print(navigate_network_debug(instructions, map_nodes, "MNA"))
    print(navigate_network_debug(instructions, map_nodes, "NJA"))
    print(navigate_network_debug(instructions, map_nodes, "RVA"))

    # return navigate_network2(instructions, map_nodes)


# print("Answer 2 tst: ", solve2('./8_tst2.txt'))
print("Answer 2: ", solve2('./8.txt'))
# LCM of 
# 20777
# 18673
# 13939
# 17621
# 19199
# 12361
# 17972669116327