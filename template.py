import requests
from functools import cache
from typing import Any
from timeit import default_timer as timer

import constants
cookie = constants.COOKIE
api_client_id = constants.API_CLIENT_ID
api_secret = constants.API_SECRET

session = requests.Session()

# ensures the site gives us the correct data, and not just a lame "you're not logged in" reponse
requests.utils.add_dict_to_cookiejar(session.cookies, {"session": cookie})


@cache
def get_input_data(day: int) -> str:
    """Takes a day and returns the input data for that day

    Args:
        day (int): The day to get the input data for

    Returns:
        str: The unparsed input data
    """
    url = f"https://adventofcode.com/2024/day/{day}/input"
    return session.get(url).text


class Template:
    def __init__(self, day: int, file_location: str = None):
        """Initializes the template class"""
        self.day = day
        self.link = f"https://adventofcode.com/2024/day/{day}"
        self.test_cases = {"part1": [], "part2": []}
        if not file_location:
            raw_data = get_input_data(day)
        else:
            with open(file_location, "r") as f:
                raw_data = f.read()
        self.set_data(self.parse_data(raw_data))


    def add_test_case(self, part: str, input_data: str, expected_output: int):
        """Adds a unit test for a specific part."""
        if part not in self.test_cases:
            raise ValueError(f"Unknown part '{part}'. Use 'part1' or 'part2'.")
        self.test_cases[part].append((input_data, expected_output))


    def run_tests(self) -> None:
        """Runs all test cases for part1 and part2."""
        for part in ["part1", "part2"]:
            self.run_part_tests(part)

    def run_part_tests(self, part: str) -> None:
        """Runs test cases for a specific part."""
        if part not in self.test_cases:
            raise ValueError(f"Unknown part '{part}'. Use 'part1' or 'part2'.")
        for idx, (input_data, expected_output) in enumerate(self.test_cases[part]):
            # Parse the test input using the day's parse_data method
            parsed_data = self.parse_data(input_data)
            self.set_data(parsed_data)

            result = getattr(self, part)()  # Calls part1 or part2 dynamically
            assert result == expected_output, (
                f"Test {idx + 1} for {part} failed: "
                f"Expected {expected_output}, got {result}."
            )
        print(f"All tests for {part} passed!")


    def parse_data(self, raw_data):
        """Default data parser. Override this in each day's class if needed."""
        return raw_data.strip()


    def get_data(self) -> Any:
        """Gets the data for the day
        WARNING: The data may be any type, as it can be modified by the set_data method

        Returns:
            Any: The data for the day
        """
        return self.__data

    def set_data(self, data: Any) -> None:
        """Sets the data as the given data
        WARNING: The data may be any type

        Args:
            data (Any): The data to set the data to
        """
        self.__data = data

    def part1(self) -> int:
        """Returns the numerical answer for part 1"""
        pass

    def part2(self) -> int:
        """Returns the numerical answer for part 2"""
        pass

    def __str__(self) -> str:
        """Returns the string representation of the day"""
        return f"\n\n{bcolors.BOLD}  -=-=- {bcolors.OKGREEN}ADVENT {bcolors.FAIL}OF {bcolors.OKGREEN}CODE {bcolors.FAIL}DAY {bcolors.OKGREEN}{self.day}{bcolors.ENDC}{bcolors.BOLD} -=-=-{bcolors.ENDC}\n{bcolors.UNDERLINE}{bcolors.OKCYAN}{self.link}{bcolors.ENDC}\n\n{self.get_part1_timing()}\n{self.get_part2_timing()}\n"

    def get_part1_timing(self) -> str:
        """Returns the time taken to run part 1"""
        start = timer()
        result = self.part1()
        end = timer()
        return f"{bcolors.BOLD}Part One:{bcolors.ENDC} {bcolors.OKGREEN}{result}{bcolors.ENDC} ({bcolors.OKCYAN}{end - start:.7f}{bcolors.ENDC} seconds)"

    def get_part2_timing(self) -> str:
        """Returns the time taken to run part 2"""
        start = timer()
        result = self.part2()
        end = timer()
        return f"{bcolors.BOLD}Part Two:{bcolors.ENDC} {bcolors.OKGREEN}{result}{bcolors.ENDC} ({bcolors.OKCYAN}{end - start:.7f}{bcolors.ENDC} seconds)"

    def get_total_timing(self) -> float:
        """Returns the time taken to run both parts"""
        return self.get_part1_timing() + self.get_part2_timing()


# from https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
