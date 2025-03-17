# Sudoku4LLM: A Dataset Generator for Training and Evaluating Reasoning LLMs

## 🚀 Motivation

As **reasoning capabilities** in Large Language Models (LLMs) continue to advance, the need for high-quality, structured datasets has become increasingly critical. While most datasets focus on linguistic tasks, reasoning over **structured or semi-structured data** remains an underexplored frontier in LLM research. **Sudoku4LLM** addresses this gap by providing a systematic, scalable, and flexible Sudoku dataset generator tailored for **training, fine-tuning, and evaluating reasoning LLMs**.

Sudoku is particularly well-suited for this purpose because it combines **logical reasoning** and **structured data representation** in a way that is both challenging and easy to verify. With Sudoku puzzles, we can simulate tasks that require multi-step reasoning, curriculum learning, and structured data serialization, all of which are essential for advancing reasoning capabilities in LLMs.

By leveraging Sudoku puzzles, **Sudoku4LLM** enables researchers and practitioners to explore and optimize reasoning-focused LLMs in a way that natural language datasets often cannot. The project is designed to support experiments in **structured data reasoning**, **Chain of Thought (CoT) prompting**, and **tabular data serialization**.

---

## 🎯 Why Use Sudoku for Reasoning LLMs?

Sudoku puzzles are more than just a game—they are a **rich reasoning benchmark** with unique properties that make them ideal for training and evaluating LLMs:

### 1. **Multi-Dimensional Difficulty Levels**
   - Sudoku puzzles offer multiple axes of difficulty:
     - **Grid Size:** Supports 4×4, 6×6, and 9×9 puzzles, each requiring progressively more reasoning steps.
     - **Percent of Missing Numbers:** Difficulty increases as more cells are left unfilled.
     - **Solution Uniqueness:** Puzzles can be configured with unique or multiple solutions.
   - This flexibility allows for fine-grained control over task complexity.

### 2. **Controlled Curriculum Learning**
   - The structured difficulty levels make Sudoku an excellent candidate for **curriculum learning**, where training progresses from simple to complex tasks.
   - Researchers can control the **length of the Chain of Thought (CoT)** required by the model, enabling targeted reasoning experiments.

### 3. **Ease of Verification**
   - Sudoku has a **well-defined solution space**, making it easy to evaluate model outputs:
     - Fully correct solutions can be verified against the ground truth.
     - Partial correctness can be assessed by counting valid rows, columns, or sub-grids.
   - This makes Sudoku puzzles ideal for reinforcement learning with rule-based rewards.

### 4. **Structured Data Format**
   - Unlike text-based tasks, Sudoku puzzles are inherently **structured**:
     - Grids can be serialized in multiple ways (e.g., cell-level, row-level, or grid-level).
     - This allows researchers to explore the **optimal input format for structured data** in LLMs.
   - Sudoku4LLM supports 11 different serialization formats, making it a versatile tool for studying structured data representation.

### 5. **Resistance to Memorization**
   - With **infinite variability** in puzzle generation, Sudoku puzzles are highly resistant to memorization, ensuring that models are genuinely reasoning rather than recalling.

### 6. **Systematic Generation**
   - Puzzles are generated using **logic-based templates**, ensuring consistency and reliability.

---

## 📚 Research Opportunities

Sudoku4LLM provides a unique opportunity to advance research in the following areas:

### 1. **Optimal Representation of Structured Data**
   - Explore different serialization methods for structured or semi-structured data.
   - Evaluate how cell-level, row-level, column-level, or grid-level representations impact LLM reasoning performance.

### 2. **Reasoning Over Tabular Data**
   - Study how LLMs handle tabular or grid-like data, which is common in real-world applications (e.g., spreadsheets, databases).
   - Develop best practices for adapting LLMs to structured data reasoning tasks.

### 3. **Chain of Thought (CoT) Optimization**
   - Use Sudoku puzzles to train and evaluate CoT prompting strategies.
   - Experiment with curriculum learning techniques to improve reasoning depth.

### 4. **Benchmarking Reasoning LLMs**
   - Use Sudoku puzzles as a benchmark for comparing reasoning capabilities across different LLM architectures and training strategies.

---

## 🔑 Features

### 🎲 **Highly Configurable Puzzle Generation**
- Supports **4×4**, **6×6**, and **9×9** Sudoku grids.
- Configurable difficulty:
  - Vary the **percentage of missing numbers** (e.g., beginner, easy, medium, hard, expert).
  - Toggle between **unique solutions** or **multiple solutions**.
- Customizable placeholders for missing numbers (e.g., `0`, `.`, `*`, `?`).

### 💡 **Flexible Serialization Formats**
- Convert puzzles into 11 different formats, including:
    - **Inline String Format**  
    - **Row-by-Row JSON**  
    - **Key-Value Row Mapping**  
    - **Grid with Separators**  
    - **CSV Format**  
    - **Coordinate List Format**  
    - **Box-Oriented Format**  
    - **Sparse Coordinate Format**  
    - **Markdown Table Format**  
    - **Alphanumeric Keyed Format**  
    - **XML Format**  
- To view visual examples of each format, see the dedicated file: [**Sudoku4LLM/FORMAT_EXAMPLES.md**](./FORMAT_EXAMPLES.md)

- Experiment with these structured representations to find the optimal input format for reasoning LLMs, tailored to your research needs.

### 🔍 **Systematic and Scalable**
- Generate an unlimited number of puzzles with systematic templates for consistency.
- Scalable for training large models or generating benchmarks.

### 🧩 **Ease of Use**
- Modular design with user-friendly scripts for generating puzzles and converting formats.
- Configurable settings via `config.py` for easy customization.

---

## 🛠️ How to Use

### 1. **Generate Sudoku Puzzles**

Run the `sudoku_generator.py` script to create a batch of Sudoku puzzles:

```bash
python sudoku_generator.py
```

Follow the interactive prompts to:
- Select grid size (4×4, 6×6, or 9×9).
- Choose difficulty level, solution enforcement, and placeholder.
- Save puzzles in JSONL format for training or evaluation.

```plaintext
$ python3 Sudoku4LLM/sudoku_generator.py

Select Sudoku grid size:
1. 4x4
2. 6x6
3. 9x9
Enter your choice (1, 2, or 3): 2
You've selected '6x6' Sudoku.

Select difficulty level:
- beginner: 20% missing numbers
- easy: 33% missing numbers
- medium: 45% missing numbers
- hard: 55% missing numbers
Press Enter to use the default difficulty: medium
Enter your choice (e.g., beginner, easy, hard): medium
You've selected 'medium' difficulty.

Enforce unique solutions:
- unique: Enforce unique solution
- non_unique: Allow multiple solutions
Press Enter to use the default option: unique
Enter your choice (e.g., unique, non_unique): non_unique
You've selected 'non_unique' for solution enforcement.

Select placeholder for unknown numbers:
- 0: 0 (Machine-readable formats)
- .: . (Human-readable text-based grids)
- _: _ (Visual emphasis in puzzles)
- *: * (Visually striking representations)
- ?: ? (Expressing uncertainty/unknowns)
Press Enter to use the default placeholder: .
Enter your choice (e.g., 0, ., _, *, ?): 0
You've selected '0' as the placeholder for unknown numbers.

Generating puzzle 1/100...
Generating puzzle 2/100...
...
Generating puzzle 100/100...
Puzzles saved to ./sudoku_data/6x6/jsonl/grid-6_diff-45_placeholder-0_enforce-non_unique.jsonl in JSON Lines format.
```

### 2. **Convert Puzzles into Desired Formats**

Use the `format_convertor.py` script to convert puzzles into one of 11 supported formats:

```bash
python format_convertor.py
```

Provide:
- The path to the input JSONL file.
- The desired output format (e.g., CSV, XML, Markdown).
- The directory where the converted files should be saved.

### 3. **Customize Configurations**

Modify `config.py` to adjust default settings, including:
- Difficulty levels and number of puzzles.
- Output paths for generated and converted puzzles.
- Default placeholders and solution uniqueness.

---

## 🤝 Acknowledgements

We would like to thank the following contributors, projects, and resources that inspired or supported this work:

- [Add acknowledgements here.]

---

## 📜 Citation

If you use **Sudoku4LLM** in your research, please cite us:

```bibtex
@misc{Sudoku4LLM,
  author = {Your Name},
  title = {Sudoku4LLM: A Dataset Generator for Training and Evaluating Reasoning LLMs},
  year = {2025},
  url = {https://github.com/your-repo/Sudoku4LLM},
  note = {Version 1.0}
}
```