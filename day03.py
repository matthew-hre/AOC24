from template import Template
import re

class Day03(Template):
    def __init__(self):
        self.day = 3
        super().__init__(self.day)

        self.add_test_case(
            "part1",
            """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))""",
            161,
        )

        self.add_test_case(
            "part2",
            """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))""",
            48,
        )

    def parse_data(self, raw_data):
       return raw_data 

    def part1(self):

        pattern = r"mul\((\d+),(\d+)\)"
        matches = re.findall(pattern, self.get_data())
        data = [[int(num1), int(num2)] for num1, num2 in matches]

        ans = 0
        for x in data:
            ans += x[0] * x[1]

        return ans

    def part2(self):
        pattern_mul = r"mul\((\d+),(\d+)\)"
        pattern_dont = r"don't\(\)"
        pattern_do = r"do\(\)"

        combined_pattern = rf"{pattern_mul}|{pattern_dont}|{pattern_do}"

        ordered_matches = re.finditer(combined_pattern, self.get_data())
        result_with_order = []

        for match in ordered_matches:
            if match.group(1): 
                result_with_order.append(["mul", int(match.group(1)), int(match.group(2))])
            elif "don't()" in match.group(0):
                result_with_order.append("don't()")
            elif "do()" in match.group(0):
                result_with_order.append("do()")

        ans = 0
        enabled = True
        for x in result_with_order:
            if x == "don't()":
                enabled = False
            elif x == "do()":
                enabled = True

            if not enabled:
                continue

            if type(x) == list:
                ans += x[1] * x[2]

        return ans


print(Day03())
