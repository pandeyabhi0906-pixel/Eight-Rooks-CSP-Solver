
# Eight Rooks CSP Solver

An Artificial Intelligence project that solves the Eight Rooks problem using Constraint Satisfaction Problems (CSP) and the Backtracking algorithm.

## Project Overview

The objective is to place eight rooks on an 8x8 chessboard such that no two rooks attack each other.

## AI Techniques Used

- Constraint Satisfaction Problem (CSP)
- Recursive Backtracking
- Constraint Checking
- State Space Search

## CSP Formulation

- Variables: 8 rows of the chessboard
- Domain: Columns 0 to 7
- Constraints: No two rooks can occupy the same column
- Goal: Place all 8 rooks without conflicts

## Features

- Finds all 40,320 valid solutions
- Interactive chessboard
- Random solution generation
- Step-by-step solution visualization
- Reset functionality
- Algorithm performance statistics

## Technologies Used

- Python
- Streamlit
- Git and GitHub

## Algorithm Statistics

| Metric | Result |
|---|---:|
| Total solutions | 40,320 |
| Constraint checks | 554,248 |
| Placements | 109,600 |
| Backtracks | 109,600 |

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Project Structure

```text
Eight-Rooks-CSP-Solver/
├── app.py
├── solver.py
├── requirements.txt
├── README.md
├── screenshots/
└── report/
```

## Conclusion

This project demonstrates how Artificial Intelligence techniques, particularly CSP and Backtracking, can be used to solve constraint-based problems.
