from template import Template
import time


class Day06(Template):
    def __init__(self):
        self.day = 6
        super().__init__(self.day)

        self.add_test_case(
            "part1",
            """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""",
            41,
        )

        self.add_test_case(
            "part2",
            """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""",
            6,
        )

    def parse_data(self, raw_data):
        return raw_data.strip().split("\n")

    def part1(self):
        def parse_map(input_map):
            grid = []
            guard_pos = None
            dir_map = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
            direction = None

            for row_idx, row in enumerate(input_map):
                grid_row = []
                for col_idx, cell in enumerate(row):
                    if cell in dir_map:
                        guard_pos = (row_idx, col_idx)
                        direction = dir_map[cell]
                        grid_row.append(".")
                    else:
                        grid_row.append(cell)
                grid.append(grid_row)

            return grid, guard_pos, direction

        def turn_right(direction):
            if direction == (-1, 0):
                return (0, 1)
            elif direction == (0, 1):
                return (1, 0)
            elif direction == (1, 0):
                return (0, -1)
            elif direction == (0, -1):
                return (-1, 0)

        def simulate_path(grid, guard_pos, direction):
            rows, cols = len(grid), len(grid[0])
            visited_positions = set()
            current_pos = guard_pos

            while 0 <= current_pos[0] < rows and 0 <= current_pos[1] < cols:

                visited_positions.add(current_pos)
                next_pos = (
                    current_pos[0] + direction[0],
                    current_pos[1] + direction[1],
                )

                if (
                    next_pos[0] < 0
                    or next_pos[0] >= rows
                    or next_pos[1] < 0
                    or next_pos[1] >= cols
                ):
                    break

                if grid[next_pos[0]][next_pos[1]] == "#":
                    direction = turn_right(direction)
                else:
                    current_pos = next_pos

            return visited_positions

        grid, guard_pos, direction = parse_map(self.get_data())
        visited_positions = simulate_path(grid, guard_pos, direction)
        return len(visited_positions)

    def part2(self):
        grid = self.get_data()
        start = next(
            (y, x)
            for y, row in enumerate(grid)
            for x, char in enumerate(row)
            if char == "^"
        )
        height = len(grid)
        width = len(grid[0])

        def patrol(ob_y=-1, ob_x=-1):
            seen = set()
            y, x = start
            dy, dx = -1, 0
            while True:
                if not (0 <= y < height and 0 <= x < width):
                    return False, len(seen)
                if grid[y][x] == "#" or (y == ob_y and x == ob_x):
                    y -= dy
                    x -= dx
                    dy, dx = dx, -dy
                elif (y, x, dy, dx) in seen:
                    return True, len(seen)
                else:
                    seen.add((y, x, dy, dx))
                    y += dy
                    x += dx

        obs = 0

        for row in range(height):
            for col in range(width):
                if grid[row][col] == ".":
                    is_looping, _ = patrol(row, col)
                    if is_looping:
                        obs += 1

        return obs


print(Day06())
