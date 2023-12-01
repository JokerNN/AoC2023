import os
import sys
from typing import List


def get_input_blob(filename: str) -> str:
    with open(os.path.join(sys.path[0], filename), encoding='utf-8') as file:
        return file.read().strip()

def get_input_lines(filename: str) -> List[str]:
    with open(os.path.join(sys.path[0], filename), encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]

def get_raw(filename: str) -> str:
    with open(os.path.join(sys.path[0], filename), encoding='utf-8') as file:
        return file.read()
