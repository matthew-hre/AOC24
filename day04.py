from template import Template

class Day04(Template):
    def __init__(self):
        self.day = 4
        super().__init__(self.day)

        self.add_test_case(
            "part1",
            """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""",
            18,
        )

        self.add_test_case(
            "part2",
            """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""",
            9,
        )


    def parse_data(self, raw_data):
        data = raw_data.strip().split("\n")
        return [list(x) for x in data]


    def part1(self):
        grid = self.get_data()

        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0

        occurrs = 0

        target = ["X", "M", "A", "S"]
        reverse_target = ["S", "A", "M", "X"]

        for r in range(rows):
            for c in range(cols - 3):
                segment = grid[r][c:c+4]
                if segment == target or segment == reverse_target:
                    occurrs += 1
        for r in range(rows - 3):
            for c in range(cols):
                segment = [grid[r+i][c] for i in range(4)]
                if segment == target or segment == reverse_target:
                    occurrs += 1
        for r in range(rows - 3):
            for c in range(cols - 3):
                segment = [grid[r+i][c+i] for i in range(4)]
                if segment == target or segment == reverse_target:
                    occurrs += 1

        for r in range(rows - 3):
            for c in range(3, cols):
                segment = [grid[r+i][c-i] for i in range(4)]
                if segment == target or segment == reverse_target:
                    occurrs += 1

        return occurrs


    def part2(self):
            grid = self.get_data()

            rows = len(grid)
            cols = len(grid[0]) if rows > 0 else 0

            occurrs = 0

            x_patterns = [
                {'tl': 'M', 'tr': 'M', 'bl': 'S', 'br': 'S'},
                {'tl': 'M', 'tr': 'S', 'bl': 'M', 'br': 'S'},
                {'tl': 'S', 'tr': 'M', 'bl': 'S', 'br': 'M'},
                {'tl': 'S', 'tr': 'S', 'bl': 'M', 'br': 'M'},
            ]
            for r in range(1, rows - 1):
                for c in range(1, cols - 1):
                    for pattern in x_patterns:
                        if (grid[r][c] == "A" and
                            grid[r-1][c-1] == pattern['tl'] and
                            grid[r-1][c+1] == pattern['tr'] and
                            grid[r+1][c-1] == pattern['bl'] and
                            grid[r+1][c+1] == pattern['br']):
                            occurrs += 1

            return occurrs

print(Day04())
