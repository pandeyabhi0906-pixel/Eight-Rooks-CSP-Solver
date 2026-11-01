
import time
SIZE = 8

# Check whether placing a rook is safe
def is_safe(board, row, col):

    for previous_row in range(row):
        if board[previous_row] == col:
            return False

    return True


# Find all possible solutions using backtracking
def solve_all(board, row, solutions, stats):

    # Base case: all 8 rooks placed
    if row == SIZE:
        solutions.append(board.copy())
        return

    # Try every column
    for col in range(SIZE):

        stats["checks"] += 1

        if is_safe(board, row, col):

            # Place rook
            board[row] = col
            stats["placements"] += 1

            # Solve next row
            solve_all(board, row + 1, solutions, stats)

            # Backtrack
            board[row] = -1
            stats["backtracks"] += 1


# Main solver function
def run_solver():

    board = [-1] * SIZE
    solutions = []

    stats = {
        "checks": 0,
        "placements": 0,
        "backtracks": 0
    }

    start_time = time.perf_counter()

    solve_all(board, 0, solutions, stats)

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    return solutions, stats, execution_time


# Display results when running this file directly
if __name__ == "__main__":

    solutions, stats, execution_time = run_solver()

    print("\nEIGHT ROOKS CSP SOLVER")
    print("----------------------")

    print("\nTotal Solutions:", len(solutions))

    print("\nFirst Valid Solution:\n")

    if solutions:
        board = solutions[0]

        for row in range(SIZE):
            for col in range(SIZE):

                if board[row] == col:
                    print(" R ", end="")
                else:
                    print(" . ", end="")

            print()

    print("\nAlgorithm Statistics:")
    print("Constraint Checks:", stats["checks"])
    print("Placements:", stats["placements"])
    print("Backtracks:", stats["backtracks"])
    print("Execution Time:", round(execution_time, 6), "seconds")


def generate_trace(target_solution):

    events = []
    board = [-1] * SIZE

    for row in range(SIZE):

        col = target_solution[row]

        # Record rook placement
        board[row] = col

        events.append({
            "board": board.copy(),
            "message": f"Placed rook at Row {row+1}, Column {col+1}",
            "type": "place"
        })

    events.append({
        "board": board.copy(),
        "message": "Random solution completed! All constraints satisfied.",
        "type": "success"
    })

    return events

