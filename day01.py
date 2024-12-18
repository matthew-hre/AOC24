from template import Template
from collections import Counter

class Day01(Template):


    def __init__(self):
        self.day = 1
        super().__init__(self.day)

        self.add_test_case(
            "part1",
            """3   4
4   3
2   5
1   3
3   9
3   3""",
            11,
        )

        self.add_test_case(
            "part2",
            """3   4
4   3
2   5
1   3
3   9
3   3""",
            31,
        )


    def parse_data(self, raw_data):
        data = raw_data.strip().split("\n")
        data = [x.split("   ") for x in data]
        return list(zip(*data[::-1]))


    def part1(self):
        data = self.get_data()

        left = sorted(data[0])
        right = sorted(data[1])

        total = 0

        for idx, _ in enumerate(left):
            total += abs(int(left[idx]) - int(right[idx]))

        return total

    def part2(self):
        data = self.get_data()
        left = data[0]
        right = Counter(data[1])

        score = 0

        for idx, val in enumerate(left):
            score += int(val) * right[val]

        return score

print(Day01())
