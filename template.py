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
        if not file_location:
            self.__data = get_input_data(day)
        else:
            f = open(file_location, "r")
            data = f.read()
            f.close()
            self.__data = data

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
