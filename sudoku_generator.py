import random
import copy
import json
import os
from config import SudokuConfig  # Import the configuration


class SudokuGenerator:
    def __init__(self, grid_size, sub_grid_size, placeholder, enforce_unique):
        # Initialize an empty grid of the specified size
        self.grid_size = grid_size
        self.sub_grid_size = sub_grid_size
        self.placeholder = placeholder
        self.enforce_unique = enforce_unique
        self.grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

        # Validate placeholder
        if self.placeholder in range(1, self.grid_size + 1):
            raise ValueError(f"Placeholder '{self.placeholder}' cannot be a valid grid number.")

    def is_safe(self, row, col, num):
        # Check if the number can be placed in the given row, column, and sub-grid
        for x in range(self.grid_size):
            if self.grid[row][x] == num or self.grid[x][col] == num:
                return False
        start_row, start_col = (
            self.sub_grid_size * (row // self.sub_grid_size),
            self.sub_grid_size * (col // self.sub_grid_size),
        )
        for i in range(self.sub_grid_size):
            for j in range(self.sub_grid_size):
                if self.grid[start_row + i][start_col + j] == num:
                    return False
        return True

    def find_empty_cell(self):
        # Helper method to find the next empty cell
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                if self.grid[row][col] == 0:
                    return row, col
        return None

    def fill_grid(self):
        # Fill the grid using backtracking
        empty_cell = self.find_empty_cell()
        if not empty_cell:
            return True  # Base case: the grid is filled
        row, col = empty_cell

        nums = list(range(1, self.grid_size + 1))
        random.shuffle(nums)
        for num in nums:
            if self.is_safe(row, col, num):
                self.grid[row][col] = num
                if self.fill_grid():
                    return True
                self.grid[row][col] = 0
        return False

    def remove_numbers(self, percent_missing):
        # Calculate the number of cells to remove based on the percentage of missing numbers
        total_cells = self.grid_size * self.grid_size
        cells_to_remove = int(total_cells * percent_missing / 100)

        while cells_to_remove > 0:
            row, col = random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)
            if self.grid[row][col] != 0:
                backup = self.grid[row][col]
                self.grid[row][col] = self.placeholder

                # If enforcing unique solutions, check for uniqueness
                if self.enforce_unique and not self.has_unique_solution(self.grid):
                    self.grid[row][col] = backup
                else:
                    cells_to_remove -= 1

    def has_unique_solution(self, grid):
        """
        Check if the given Sudoku grid has a unique solution.
        """
        solutions = 0

        def solve():
            nonlocal solutions
            empty_cell = self.find_empty_cell()
            if not empty_cell:
                solutions += 1
                return
            row, col = empty_cell
            for num in range(1, self.grid_size + 1):
                if self.is_safe(row, col, num):
                    grid[row][col] = num
                    solve()
                    grid[row][col] = 0
                    if solutions > 1:  # Stop early if more than one solution is found
                        return

        solve()
        return solutions == 1
    
    def generate_puzzle(self, percent_missing):
        # Generate a complete grid and then remove numbers to create a puzzle
        self.grid = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.fill_grid()
        self.remove_numbers(percent_missing)
        return self.grid  # Return the puzzle


def save_puzzles_to_jsonl(puzzles, path, filename):
    # Ensure the directory exists
    os.makedirs(path, exist_ok=True)
    file_path = os.path.join(path, filename)

    with open(file_path, "w") as file:
        for puzzle in puzzles:
            json.dump({"puzzle": puzzle}, file)
            file.write("\n")
    print(f"Puzzles saved to {file_path} in JSON Lines format.")


def get_user_settings(config):
    """
    Collect user-selected settings (difficulty, enforce uniqueness, placeholder) once.
    """
    # Select difficulty
    default_difficulty = config["default_options"]["difficulty"]
    print("\nSelect difficulty level:\n")
    for difficulty, percent_missing in config["difficulty_levels"].items():
        print(f"- {difficulty}: {percent_missing}% missing numbers")
    print(f"\nPress Enter to use the default difficulty: {default_difficulty}\n")

    while True:
        choice = input("Enter your choice (e.g., beginner, easy, hard): ").strip().lower()
        if not choice:  # Use default if no input is provided
            print(f"\nUsing default difficulty: {default_difficulty}\n")
            percent_missing = config["difficulty_levels"][default_difficulty]
            break
        elif choice in config["difficulty_levels"]:
            print(f"\nYou've selected '{choice}' difficulty.\n")
            percent_missing = config["difficulty_levels"][choice]
            break
        else:
            print("\nInvalid choice. Please select a valid difficulty level.\n")

    # Select enforce uniqueness
    default_enforce = config["default_options"]["enforce_unique"]
    print("\nEnforce unique solutions:\n")
    for option, enforce in config["enforce_unique_options"].items():
        print(f"- {option}: {'Enforce unique solution' if enforce else 'Allow multiple solutions'}")
    print(f"\nPress Enter to use the default option: {default_enforce}\n")

    while True:
        choice = input("Enter your choice (e.g., unique, non_unique): ").strip().lower()
        if not choice:
            print(f"\nUsing default option: {default_enforce}\n")
            enforce_unique = config["enforce_unique_options"][default_enforce]
            break
        elif choice in config["enforce_unique_options"]:
            print(f"\nYou've selected '{choice}' for solution enforcement.\n")
            enforce_unique = config["enforce_unique_options"][choice]
            break
        else:
            print("\nInvalid choice. Please select 'unique' or 'non_unique'.\n")

    # Select placeholder
    default_placeholder = config["default_options"]["placeholder"]
    print("\nSelect placeholder for unknown numbers:\n")
    for key, description in SudokuConfig.get_placeholder_options().items():
        print(f"- {key}: {description}")
    print(f"\nPress Enter to use the default placeholder: {default_placeholder}\n")

    while True:
        choice = input("Enter your choice (e.g., 0, ., _, *, ?): ").strip()
        if not choice:
            print(f"\nUsing default placeholder: {default_placeholder}\n")
            placeholder = default_placeholder
            break
        elif choice in SudokuConfig.get_placeholder_options():
            print(f"\nYou've selected '{choice}' as the placeholder for unknown numbers.\n")
            placeholder = choice
            break
        else:
            print("\nInvalid choice. Please select a valid placeholder.\n")

    return percent_missing, enforce_unique, placeholder


def select_grid_size(configs):
    """
    Allow the user to select a grid size (4x4, 6x6, 9x9).
    """
    print("\nSelect Sudoku grid size:\n")
    grid_options = list(configs.keys())
    for i, option in enumerate(grid_options, start=1):
        print(f"{i}. {option}")
    print()

    while True:
        try:
            choice = int(input("Enter your choice (1, 2, or 3): ").strip())
            if 1 <= choice <= len(grid_options):
                selected_version = grid_options[choice - 1]
                print(f"\nYou've selected '{selected_version}' Sudoku.\n")
                return configs[selected_version]
            else:
                print("\nInvalid choice. Please select a valid option.\n")
        except ValueError:
            print("\nInvalid input. Please enter a number corresponding to your choice.\n")


def generate_sudoku_puzzles(num_puzzles, config, settings, output_file):
    """
    Generate a batch of Sudoku puzzles using predefined settings.
    """
    percent_missing, enforce_unique, placeholder = settings
    generator = SudokuGenerator(
        config["grid_size"], config["sub_grid_size"], placeholder, enforce_unique
    )

    puzzles = []
    for i in range(num_puzzles):
        print(f"Generating puzzle {i + 1}/{num_puzzles}...")
        puzzle = generator.generate_puzzle(percent_missing)
        puzzles.append(puzzle)

    save_puzzles_to_jsonl(puzzles, config["base_output_path"], output_file)


if __name__ == "__main__":
    # Load configurations
    configs = SudokuConfig.get_configs()

    # Let the user select the grid size
    selected_config = select_grid_size(configs)

    # Collect user settings
    settings = get_user_settings(selected_config)
    num_puzzles = selected_config["num_puzzles"]

    # Create a detailed output filename
    difficulty, enforce_unique, placeholder = settings
    enforce_label = "unique" if enforce_unique else "non_unique"
    output_file = (
        f"grid-{selected_config['grid_size']}_diff-{difficulty}_placeholder-{placeholder}_enforce-{enforce_label}.jsonl"
    )

    # Generate puzzles
    generate_sudoku_puzzles(num_puzzles, selected_config, settings, output_file)