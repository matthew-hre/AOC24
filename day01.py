from template import Template
from collections import Counter

class Day01(Template):


    def __init__(self):
        self.day = 1
        super().__init__(self.day)

        data = self.get_data().strip().split("\n")
        data = [x.split("   ") for x in data]
        data = list(zip(*data[::-1]))
        self.set_data(data)


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
