# Sudoku4LLM/format_convertor.py

import json
import os
from config import SudokuConfig  # Importing the config.py module for format options


class SudokuFormatConverter:
    def __init__(self, input_jsonl, output_path):
        self.input_jsonl = input_jsonl
        self.output_path = output_path

    def load_puzzles(self):
        """Load puzzles from the JSONL file."""
        puzzles = []
        try:
            with open(self.input_jsonl, "r") as file:
                for line in file:
                    puzzle_data = json.loads(line)
                    puzzles.append(puzzle_data)
        except FileNotFoundError:
            print(f"Error: Input file '{self.input_jsonl}' not found.")
            exit(1)
        except json.JSONDecodeError:
            print(f"Error: File '{self.input_jsonl}' is not in valid JSONL format.")
            exit(1)
        return puzzles

    def save_to_jsonl(self, converted_puzzles, format_name):
        """Save the converted puzzles to a JSONL file."""
        try:
            os.makedirs(self.output_path, exist_ok=True)
            output_file = os.path.join(self.output_path, f"converted_{format_name}.jsonl")
            with open(output_file, "w") as file:
                for puzzle in converted_puzzles:
                    json.dump(puzzle, file)
                    file.write("\n")
            print(f"Converted puzzles saved in JSONL format to: {output_file}")
        except PermissionError:
            print(f"Error: Unable to write to directory '{self.output_path}'. Check your permissions.")
            exit(1)
        except Exception as e:
            print(f"Error: An unexpected error occurred while saving the file: {e}")
            exit(1)

    def convert_to_inline_string(self, puzzle):
        """Convert puzzle to Inline String Format."""
        return "".join(str(cell) for row in puzzle for cell in row)

    def convert_to_row_by_row(self, puzzle):
        """Convert puzzle to Row-by-Row List Format."""
        return json.dumps(puzzle, indent=2)

    def convert_to_key_value_row(self, puzzle):
        """Convert puzzle to Key-Value Row Mapping."""
        return json.dumps({f"row_{i + 1}": row for i, row in enumerate(puzzle)}, indent=2)

    def convert_to_grid_with_separators(self, puzzle, separator=True):
        """Convert puzzle to Grid with Separators or Box-Oriented Format."""
        rows = []
        grid_size = len(puzzle)
        sub_grid_size = int(grid_size ** 0.5)  # Dynamically calculate sub-grid size
        for i, row in enumerate(puzzle):
            row_parts = []
            for j in range(0, grid_size, sub_grid_size):
                row_parts.append(" ".join(map(str, row[j:j + sub_grid_size])))
            rows.append(" | ".join(row_parts))
            if separator and (i + 1) % sub_grid_size == 0 and i + 1 != grid_size:
                rows.append(" | ".join("-" * len(part) for part in row_parts))
        return "\n".join(rows)

    def convert_to_csv(self, puzzle):
        """Convert puzzle to CSV Format."""
        return "\n".join(",".join(map(str, row)) for row in puzzle)

    def convert_to_coordinate_list(self, puzzle, sparse=False):
        """Convert puzzle to Coordinate List or Sparse Coordinate Format."""
        if sparse:
            return ", ".join(f"({i + 1},{j + 1})={cell}"
                             for i, row in enumerate(puzzle)
                             for j, cell in enumerate(row) if cell != 0)
        else:
            return str([(i + 1, j + 1, cell)
                        for i, row in enumerate(puzzle)
                        for j, cell in enumerate(row) if cell != 0])

    def convert_to_markdown_table(self, puzzle):
        """Convert puzzle to Markdown Table Format."""
        grid_size = len(puzzle)
        rows = ["|   | " + " | ".join(map(str, range(1, grid_size + 1))) + " |"]
        rows.append("|---|" + "---|" * grid_size)
        for i, row in enumerate(puzzle):
            rows.append(f"| {chr(65 + i)} | " + " | ".join(map(str, row)) + " |")
        return "\n".join(rows)

    def convert_to_alphanumeric_keyed(self, puzzle):
        """Convert puzzle to Alphanumeric Keyed Format."""
        return json.dumps({f"{chr(65 + i)}{j + 1}": cell
                           for i, row in enumerate(puzzle)
                           for j, cell in enumerate(row) if cell != 0}, indent=2)

    def convert_to_xml(self, puzzle):
        """Convert puzzle to XML Format."""
        rows = ["<sudoku>"]
        for i, row in enumerate(puzzle):
            rows.append(f'  <row index="{i + 1}">' + ",".join(map(str, row)) + "</row>")
        rows.append("</sudoku>")
        return "\n".join(rows)

    def convert(self, format_choice):
        """Convert puzzles to the selected format, include game_rule and directly use config."""
        puzzles = self.load_puzzles()
        converted_puzzles = []

        # Mapping format_choice to corresponding conversion methods
        format_methods = {
            1: ("Inline String Format", self.convert_to_inline_string),
            2: ("Row-by-Row List Format", self.convert_to_row_by_row),
            3: ("Key-Value Row Mapping", self.convert_to_key_value_row),
            4: ("Grid with Separators", lambda puzzle: self.convert_to_grid_with_separators(puzzle, separator=True)),
            5: ("CSV Format", self.convert_to_csv),
            6: ("Coordinate List Format", lambda puzzle: self.convert_to_coordinate_list(puzzle, sparse=False)),
            7: ("Box-Oriented Format", lambda puzzle: self.convert_to_grid_with_separators(puzzle, separator=False)),
            8: ("Sparse Coordinate Format", lambda puzzle: self.convert_to_coordinate_list(puzzle, sparse=True)),
            9: ("Markdown Table Format", self.convert_to_markdown_table),
            10: ("Alphanumeric Keyed Format", self.convert_to_alphanumeric_keyed),
            11: ("XML Format", self.convert_to_xml)
        }

        if format_choice not in format_methods:
            print(f"Error: Invalid format choice '{format_choice}'. Please choose a number between 1 and 11.")
            exit(1)

        # Get the format description and function
        description, format_function = format_methods[format_choice]

        # Apply the selected format method to each puzzle
        for puzzle_data in puzzles:
            puzzle = puzzle_data["puzzle"]
            config = puzzle_data["config"]  # Directly use the "config" from the original data

            # Add game rule based on grid size
            grid_size = config["grid_size"]
            game_rule = SudokuConfig.get_configs().get(f"{grid_size}x{grid_size}", {}).get("rules", "Unknown rules").strip()

            # Build the converted puzzle data
            converted_puzzles.append({
                "original_puzzle": puzzle,  # Include the original puzzle
                "converted_puzzle": format_function(puzzle),  # Converted puzzle
                "format": description,  # Metadata: format name
                "game_rule": game_rule,  # Game rule
                "config": config  # Directly include the original config
            })

        # Save all converted puzzles in JSONL format
        self.save_to_jsonl(converted_puzzles, description.replace(" ", "_").lower())


if __name__ == "__main__":
    # Prompt user for input file
    input_jsonl = input("Enter the path to the Sudoku JSONL file you want to convert: ").strip()
    if not os.path.isfile(input_jsonl):
        print(f"Error: File '{input_jsonl}' does not exist.")
        exit(1)

    # Prompt user for output directory
    output_path = input("Enter the directory where converted files should be saved: ").strip()
    if not os.path.isdir(output_path):
        print(f"Error: Directory '{output_path}' does not exist.")
        exit(1)

    # Display available formats
    format_options = SudokuConfig.get_conversion_formats()
    print("\nChoose a format to convert Sudoku puzzles into:")
    for number, description in format_options.items():
        print(f"{number}: {description}")

    try:
        format_choice = int(input("Enter the format number (1-11): ").strip())
    except ValueError:
        print("Error: Please enter a valid number between 1 and 11.")
        exit(1)

    # Initialize the converter with the user-provided file and directory
    converter = SudokuFormatConverter(input_jsonl, output_path)
    converter.convert(format_choice)