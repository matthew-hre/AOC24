from template import Template
from collections import Counter

class Day02(Template):
    def __init__(self):
        self.day = 2
        super().__init__(self.day)

        self.add_test_case(
            "part1",
            """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""",
            2,
        )
        

        self.add_test_case(
            "part2",
            """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""",
            4,
        )


    def parse_data(self, raw_data):
        data = [[int(y) for y in x.split(" ")] for x in raw_data.strip().split("\n")]
        return data

    def part1(self):
        data = self.get_data()

        safe = 0

        sign = lambda x: (1, -1)[x<0]

        for row in data:
            ascdec = 0

            for idx, _ in enumerate(row):
                if (idx == len(row) - 1):
                    safe += 1
                    break

                diff = row[idx] - row[idx + 1]

                if abs(diff) == 0 or abs(diff) > 3 or (ascdec != 0 and sign(diff) != ascdec): 
                    break
                elif idx == 0:
                    ascdec = sign(row[idx] - row[idx+1])

        return safe


    def part2(self):
        data = self.get_data()

        perms = lambda input_list: [input_list] + [input_list[:i] + input_list[i+1:] for i in range(len(input_list))]

        def is_safe(row):
            ascdec = 0
            sign = lambda x: (1, -1)[x < 0]


            for idx in range(len(row) - 1):
                diff = row[idx] - row[idx + 1]
                if abs(diff) == 0 or abs(diff) > 3 or (ascdec != 0 and sign(diff) != ascdec):
                    return False
                if idx == 0:
                    ascdec = sign(diff)
            return True

        safe = 0

        for row in data:
            for permuted_row in perms(row):
                if is_safe(permuted_row):
                    safe += 1
                    break

        return safe

        
print(Day02())
