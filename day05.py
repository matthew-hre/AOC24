from template import Template
from collections import defaultdict, deque


class Day05(Template):
    def __init__(self):
        self.day = 5
        super().__init__(self.day)

        self.add_test_case(
            "part1",
            """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""",
            143,
        )

        self.add_test_case(
            "part2",
            """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""",
            123,
        )

    def parse_data(self, raw_data):
        data = raw_data.strip().split("\n\n")
        rules = [[int(y) for y in x.split("|")] for x in data[0].split("\n")]
        updates = [[int(y) for y in x.split(",")] for x in data[1].split("\n")]

        return [rules, updates]

    def part1(self):
        rules, updates = self.get_data()
        middle_pages = []
        for update in updates:
            if self.correct_order(update, rules) == update:
                middle_pages.append(update[len(update) // 2])

        return sum(middle_pages)

    def part2(self):
        rules, updates = self.get_data()
        incorrect_updates = []
        for update in updates:
            if not self.correct_order(update, rules) == update:
                incorrect_updates.append(self.correct_order(update, rules))

        middle_pages_incorrect = [
            update[len(update) // 2] for update in incorrect_updates
        ]
        return sum(middle_pages_incorrect)

    def correct_order(self, update, rules):
        graph = defaultdict(list)
        in_degree = defaultdict(int)

        for x, y in rules:
            if x in update and y in update:
                graph[x].append(y)
                in_degree[y] += 1

        queue = deque([page for page in update if in_degree[page] == 0])
        sorted_order = []

        while queue:
            page = queue.popleft()
            sorted_order.append(page)
            for neighbor in graph[page]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return sorted_order


print(Day05())
