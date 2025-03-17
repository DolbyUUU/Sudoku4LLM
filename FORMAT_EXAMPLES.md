## 💡 **Flexible Serialization Formats**

Sudoku4LLM supports 11 different serialization formats, allowing researchers to experiment with various structured data representations for reasoning LLMs. These formats provide a diverse set of options to explore the optimal input structure for tasks involving tabular or grid-like data.

Below are the supported formats with examples:

---

### 1. **Inline String Format**
A compact, single-line representation of the puzzle, where rows are concatenated into a single string.

**Example:**
```
530070000600195000098000060800060003400803001700020006060000280000419005000080079
```

---

### 2. **Row-by-Row List Format**
A JSON list of rows, where each row is an array.

**Example:**
```json
[
  [5, 3, 0, 0, 7, 0, 0, 0, 0],
  [6, 0, 0, 1, 9, 5, 0, 0, 0],
  [0, 9, 8, 0, 0, 0, 0, 6, 0],
  [8, 0, 0, 0, 6, 0, 0, 0, 3],
  [4, 0, 0, 8, 0, 3, 0, 0, 1],
  [7, 0, 0, 0, 2, 0, 0, 0, 6],
  [0, 6, 0, 0, 0, 0, 2, 8, 0],
  [0, 0, 0, 4, 1, 9, 0, 0, 5],
  [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
```

---

### 3. **Key-Value Row Mapping**
A JSON object where each key represents a row, and the value is the array for that row.

**Example:**
```json
{
  "row_1": [5, 3, 0, 0, 7, 0, 0, 0, 0],
  "row_2": [6, 0, 0, 1, 9, 5, 0, 0, 0],
  "row_3": [0, 9, 8, 0, 0, 0, 0, 6, 0],
  "row_4": [8, 0, 0, 0, 6, 0, 0, 0, 3],
  "row_5": [4, 0, 0, 8, 0, 3, 0, 0, 1],
  "row_6": [7, 0, 0, 0, 2, 0, 0, 0, 6],
  "row_7": [0, 6, 0, 0, 0, 0, 2, 8, 0],
  "row_8": [0, 0, 0, 4, 1, 9, 0, 0, 5],
  "row_9": [0, 0, 0, 0, 8, 0, 0, 7, 9]
}
```

---

### 4. **Grid with Separators**
A human-readable format that uses separators (`|` and `-`) to emphasize sub-grids.

**Example:**
```
5 3 0 | 0 7 0 | 0 0 0
6 0 0 | 1 9 5 | 0 0 0
0 9 8 | 0 0 0 | 0 6 0
------+-------+------
8 0 0 | 0 6 0 | 0 0 3
4 0 0 | 8 0 3 | 0 0 1
7 0 0 | 0 2 0 | 0 0 6
------+-------+------
0 6 0 | 0 0 0 | 2 8 0
0 0 0 | 4 1 9 | 0 0 5
0 0 0 | 0 8 0 | 0 7 9
```

---

### 5. **CSV Format**
A standard CSV representation of the puzzle.

**Example:**
```
5,3,0,0,7,0,0,0,0
6,0,0,1,9,5,0,0,0
0,9,8,0,0,0,0,6,0
8,0,0,0,6,0,0,0,3
4,0,0,8,0,3,0,0,1
7,0,0,0,2,0,0,0,6
0,6,0,0,0,0,2,8,0
0,0,0,4,1,9,0,0,5
0,0,0,0,8,0,0,7,9
```

---

### 6. **Coordinate List Format**
A list of `(row, column, value)` tuples for non-empty cells.

**Example:**
```
[
  (1,1,5), (1,2,3), (1,5,7),
  (2,1,6), (2,4,1), (2,5,9), (2,6,5),
  (3,2,9), (3,3,8), (3,8,6),
  (4,1,8), (4,5,6), (4,9,3),
  (5,1,4), (5,4,8), (5,6,3), (5,9,1),
  (6,1,7), (6,5,2), (6,9,6),
  (7,2,6), (7,7,2), (7,8,8),
  (8,4,4), (8,5,1), (8,6,9), (8,9,5),
  (9,5,8), (9,8,7), (9,9,9)
]
```

---

### 7. **Box-Oriented Format**
A grid representation emphasizing sub-grids, without row separators.

**Example:**
```
5 3 0 | 6 0 0 | 0 9 8
0 7 0 | 1 9 5 | 0 0 0
0 0 0 | 0 0 0 | 0 6 0
------+-------+------
8 0 0 | 4 0 0 | 7 0 0
0 6 0 | 8 0 3 | 0 2 0
0 0 3 | 0 0 1 | 0 0 6
------+-------+------
0 6 0 | 0 0 0 | 0 0 0
0 0 0 | 4 1 9 | 0 8 0
2 8 0 | 0 0 5 | 0 7 9
```

---

### 8. **Sparse Coordinate Format**
A sparse representation using key-value pairs for non-empty cells.

**Example:**
```
(1,1)=5, (1,2)=3, (1,5)=7, (2,1)=6, (2,4)=1, (2,5)=9, 
(2,6)=5, (3,2)=9, (3,3)=8, (3,8)=6, (4,1)=8, (4,5)=6, 
(4,9)=3, (5,1)=4, (5,4)=8, (5,6)=3, (5,9)=1, (6,1)=7, 
(6,5)=2, (6,9)=6, (7,2)=6, (7,7)=2, (7,8)=8, (8,4)=4, 
(8,5)=1, (8,6)=9, (8,9)=5, (9,5)=8, (9,8)=7, (9,9)=9
```

---

### 9. **Markdown Table Format**
A Markdown table representation for easy visualization in Markdown files.

**Example:**
```
|   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| A | 5 | 3 | 0 | 0 | 7 | 0 | 0 | 0 | 0 |
| B | 6 | 0 | 0 | 1 | 9 | 5 | 0 | 0 | 0 |
| C | 0 | 9 | 8 | 0 | 0 | 0 | 0 | 6 | 0 |
| D | 8 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 3 |
| E | 4 | 0 | 0 | 8 | 0 | 3 | 0 | 0 | 1 |
| F | 7 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 6 |
| G | 0 | 6 | 0 | 0 | 0 | 0 | 2 | 8 | 0 |
| H | 0 | 0 | 0 | 4 | 1 | 9 | 0 | 0 | 5 |
| I | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 7 | 9 |
```

---

### 10. **Alphanumeric Keyed Format**
A JSON object using alphanumeric keys to identify each cell.

**Example:**
```json
{
  "A1": 5, "A2": 3, "A5": 7,
  "B1": 6, "B4": 1, "B5": 9, "B6": 5,
  "C2": 9, "C3": 8, "C8": 6,
  "D1": 8, "D5": 6, "D9": 3,
  "E1": 4, "E4": 8, "E6": 3, "E9": 1,
  "F1": 7, "F5": 2, "F9": 6,
  "G2": 6, "G7": 2, "G8": 8,
  "H4": 4, "H5": 1, "H6": 9, "H9": 5,
  "I5": 8, "I8": 7, "I9": 9
}
```

---

### 11. **XML Format**
An XML representation of the puzzle, with each row as an XML element.

**Example:**
```xml
<sudoku>
  <row index="1">5,3,0,0,7,0,0,0,0</row>
  <row index="2">6,0,0,1,9,5,0,0,0</row>
  <row index="3">0,9,8,0,0,0,0,6,0</row>
  <row index="4">8,0,0,0,6,0,0,0,3</row>
  <row index="5">4,0,0,8,0,3,0,0,1</row>
  <row index="6">7,0,0,0,2,0,0,0,6</row>
  <row index="7">0,6,0,0,0,0,2,8,0</row>
  <row index="8">0,0,0,4,1,9,0,0,5</row>
  <row index="9">0,0,0,0,8,0,0,7,9</row>
</sudoku>
