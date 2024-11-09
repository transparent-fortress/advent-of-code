class AOC:
    def __init__(self, filepath):
        self.filepath = filepath
    
    def load_input(self):
        print(self.filepath)
        with open(self.filepath, 'r') as inputfile:
            self.input_lines = inputfile.readlines()
            self.input_data = inputfile.read()

    def solve_part1(self):
        self.load_input()
        print(self.input_lines)

aoc = AOC('/workspaces/advent-of-code/advent-of-code-2023/day-1-input.txt')

aoc.solve_part1()

