import importlib
import sys

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

def run_day_tests(day: int):
    """Dynamically imports a day's module and runs its tests."""
    try:
        # Import the module dynamically
        module_name = f"day{day:02d}"
        day_module = importlib.import_module(module_name)

        # Initialize the day class
        day_class = getattr(day_module, f"Day{day:02d}")
        day_instance = day_class()

        for part in ["part1", "part2"]:
            print(f"{bcolors.BOLD}Part {part[-1].upper()}: {bcolors.ENDC}")
            try:
                test_cases = day_instance.test_cases.get(part, [])
                for idx, (input_data, expected_output) in enumerate(test_cases, start=1):
                    day_instance.set_data(day_instance.parse_data(input_data))
                    result = getattr(day_instance, part)()
                    assert result == expected_output, (
                        f"Test {idx} failed: Expected {expected_output}, got {result}."
                    )
                    print(f"    {bcolors.OKGREEN}✅ Test {idx} Passed!{bcolors.ENDC}")
                print(f"    {bcolors.OKGREEN}✅ Final Output: Didn't Crash!{bcolors.ENDC}")
            except AssertionError as e:
                print(f"    {bcolors.FAIL}❌ {e}{bcolors.ENDC}")
    except ModuleNotFoundError:
        print(f"{bcolors.WARNING}Day {day:02d} module not found. Skipping...{bcolors.ENDC}")
    except AttributeError:
        print(f"{bcolors.WARNING}Day {day:02d} class not defined. Skipping...{bcolors.ENDC}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # If a specific day is provided, run tests for that day only
        try:
            day = int(sys.argv[1])
            run_day_tests(day)
        except ValueError:
            print(f"{bcolors.FAIL}Please provide a valid day number (e.g., `python test_runner.py 1`).{bcolors.ENDC}")
    else:
        # Run tests for all days (assumes up to 25 days of Advent of Code)
        for day in range(1, 26):
            run_day_tests(day)

