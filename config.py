class SudokuConfig:
    @staticmethod
    def get_configs():
        # Define configurations for different Sudoku versions
        configs = {
            "4x4": {
                "grid_size": 4,
                "sub_grid_size": 2,
                "num_puzzles": 100,
                "base_output_path": "./sudoku_data/4x4/jsonl",  # JSONL files path
                "converted_output_path": "./sudoku_data/4x4/converted",  # Converted formats path
                "difficulty_levels": {
                    "beginner": 10,  # Percent missing for beginner level
                    "easy": 25,
                    "hard": 40,
                },
                "enforce_unique_options": {
                    "unique": True,  # Enforce unique solutions
                    "non_unique": False,  # Allow multiple solutions
                },
                "default_options": {
                    "difficulty": "easy",  # Default difficulty
                    "enforce_unique": "unique",  # Default enforce unique setting
                    "placeholder": "0",  # Default placeholder
                },
                "rules": """
                4x4 Sudoku Rules:
                - The grid is 4x4 in size.
                - Each row, column, and 2x2 sub-grid must contain the numbers 1 to 4 exactly once.
                - Some cells are pre-filled, and the player must fill in the rest.
                """
            },
            "6x6": {
                "grid_size": 6,
                "sub_grid_size": 2,
                "num_puzzles": 100,
                "base_output_path": "./sudoku_data/6x6/jsonl",
                "converted_output_path": "./sudoku_data/6x6/converted",
                "difficulty_levels": {
                    "beginner": 20,
                    "easy": 33,
                    "medium": 45,
                    "hard": 55,
                },
                "enforce_unique_options": {
                    "unique": True,
                    "non_unique": False,
                },
                "default_options": {
                    "difficulty": "medium",  # Default difficulty
                    "enforce_unique": "unique",  # Default enforce unique setting
                    "placeholder": ".",  # Default placeholder
                },
                "rules": """
                6x6 Sudoku Rules:
                - The grid is 6x6 in size.
                - Each row, column, and 2x3 sub-grid must contain the numbers 1 to 6 exactly once.
                - Some cells are pre-filled, and the player must fill in the rest.
                """
            },
            "9x9": {
                "grid_size": 9,
                "sub_grid_size": 3,
                "num_puzzles": 100,
                "base_output_path": "./sudoku_data/9x9/jsonl",
                "converted_output_path": "./sudoku_data/9x9/converted",
                "difficulty_levels": {
                    "beginner": 30,
                    "easy": 40,
                    "medium": 50,
                    "hard": 60,
                    "expert": 70,
                },
                "enforce_unique_options": {
                    "unique": True,
                    "non_unique": False,
                },
                "default_options": {
                    "difficulty": "hard",  # Default difficulty
                    "enforce_unique": "non_unique",  # Default enforce unique setting
                    "placeholder": "?",  # Default placeholder
                },
                "rules": """
                9x9 Sudoku Rules:
                - The grid is 9x9 in size.
                - Each row, column, and 3x3 sub-grid must contain the numbers 1 to 9 exactly once.
                - Some cells are pre-filled, and the player must fill in the rest.
                """
            },
        }
        return configs

    @staticmethod
    def get_placeholder_options():
        # Define all available placeholder options for missing numbers
        return {
            "0": "0 (Machine-readable formats)",
            ".": ". (Human-readable text-based grids)",
            "_": "_ (Visual emphasis in puzzles)",
            "*": "* (Visually striking representations)",
            "?": "? (Expressing uncertainty/unknowns)",
        }

    @staticmethod
    def get_conversion_formats():
        # Define the 11 Sudoku puzzle formats for conversion
        formats = {
            1: "Inline String Format",
            2: "Row-by-Row List Format",
            3: "Key-Value Row Mapping",
            4: "Grid with Separators",
            5: "CSV Format",
            6: "Coordinate List Format",
            7: "Box-Oriented Format",
            8: "Sparse Coordinate Format",
            9: "Markdown Table Format",
            10: "Alphanumeric Keyed Format",
            11: "XML Format",
        }
        return formats

    @staticmethod
    def validate_config(config):
        # Validate individual configuration entries
        if config["grid_size"] % config["sub_grid_size"] != 0:
            raise ValueError(
                f"Invalid configuration: grid_size {config['grid_size']} "
                f"must be divisible by sub_grid_size {config['sub_grid_size']}."
            )
        if config["grid_size"] <= 0 or config["sub_grid_size"] <= 0:
            raise ValueError(
                f"Invalid configuration: grid_size and sub_grid_size must be positive integers."
            )

    @staticmethod
    def validate_all_configs(configs):
        # Validate all configurations
        for version, config in configs.items():
            try:
                SudokuConfig.validate_config(config)
            except ValueError as e:
                raise ValueError(f"Error in {version} configuration: {e}")

    @staticmethod
    def instructions():
        # Display instructions for using the Sudoku generator
        return """
        Sudoku Generator Instructions:
        ----------------------------------
        1. Choose a version: 4x4, 6x6, or 9x9.
        2. Choose a difficulty level:
           - Beginner: Few missing numbers
           - Easy: Moderate missing numbers
           - Medium: Balanced difficulty
           - Hard: Many missing numbers
           - Expert: Most numbers missing (9x9 only)
        3. Choose a placeholder for missing numbers:
           - Example: 0, ., _, *, or ?
        4. Decide whether puzzles must have unique solutions.
        5. Choose a format for saving puzzles. Options include:
           - Inline String Format
           - Row-by-Row List Format
           - Key-Value Row Mapping
           - Grid with Separators
           - CSV Format
           - Coordinate List Format
           - Box-Oriented Format
           - Sparse Coordinate Format
           - Markdown Table Format
           - Alphanumeric Keyed Format
           - XML Format
        6. Generated puzzles will be saved in appropriate files.
        """