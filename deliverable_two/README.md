Here is your **complete, clean, GitHub-ready README.md** combining both projects in one place:

---

```markdown
# 🐍 Python Mini Projects: AI Game + Data Visualization

This repository contains two Python projects built for learning and practice:

1. 🎮 A **Tic-Tac-Toe game with AI (Minimax algorithm)**
2. 📊 A **Matplotlib data visualization project using sales data**

Both projects demonstrate core skills in:
- Python programming
- Algorithms (Minimax AI)
- Data analysis
- Data visualization

---

# 📁 Project Structure

```

.
├── tic_tac_toe.py
├── matplotlib_sales_analysis.py
├── company_sales_data.csv
├── outputs/
│   ├── exercise1_total_profit.png
│   └── exercise2_subplots.png
└── README.md

````

---

# 🎮 Project 1: Tic-Tac-Toe AI Game

## Description

A command-line Tic-Tac-Toe game where:
- The player plays as **X**
- The AI plays as **O**
- The AI uses the **Minimax algorithm** to always choose the optimal move

The game runs in a continuous loop until the user chooses to exit.

---

## Features

- Human vs AI gameplay
- AI uses Minimax algorithm (optimal play)
- Input validation for moves (1–9)
- Win and tie detection
- Replay system (infinite play loop)
- Clean command-line interface

---

## How to Run

```bash
python tic_tac_toe.py
````

---

## Game Instructions

* Choose a position by entering numbers **1–9**
* After each game:

  * Enter `y` to play again
  * Enter any other key to quit

---

# 📊 Project 2: Matplotlib Sales Data Visualization

## Description

This project analyzes and visualizes company sales data using:
Matplotlib and Pandas

It reads a CSV file and generates:

1. A line plot of total profit per month
2. Subplots comparing bathing soap and facewash sales

---

## Dataset Used

* `company_sales_data.csv`

Key columns:

* `month_number`
* `total_profit`
* `bathingsoap`
* `facewash`

---

## Visualizations

### 📈 Exercise 1: Total Profit Over Time

* Line plot
* Monthly trend analysis
* Grid + markers for clarity

### 📊 Exercise 2: Product Sales Comparison

* Subplot 1: Bathing soap sales
* Subplot 2: Facewash sales
* Side-by-side comparison across months

---

## How to Run

```bash
python matplotlib_sales_analysis.py
```

---

# 🧠 Skills Demonstrated

## Programming

* Functions
* Loops
* Conditionals
* Input validation

## AI / Algorithms

* Minimax algorithm
* Game tree decision making

## Data Analysis

* Working with CSV files
* Data extraction using Pandas

## Data Visualization

* Line plots
* Subplots
* Custom styling (labels, titles, grids)
* Layout management using `tight_layout()`

---

# 🚀 Future Improvements

### Tic-Tac-Toe

* Add GUI version (Tkinter or Streamlit)
* Add difficulty levels (Easy / Medium / Hard)
* Add score tracking system

### Data Visualization

* Add more product comparisons
* Build interactive dashboard
* Use real-time datasets

---

# 👤 Author

This project was built as part of a Python learning journey focusing on:

* AI fundamentals
* Data analysis
* Visualization
* Practical problem solving

```
- or :contentReference[oaicite:4]{index=4}
```
