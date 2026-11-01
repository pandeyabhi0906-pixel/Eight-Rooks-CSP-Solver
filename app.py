
import streamlit as st
import random
from solver import run_solver, generate_trace


# --------------------------------
# PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="Eight Rooks CSP Solver",
    page_icon="♜",
    layout="wide"
)


# --------------------------------
# CUSTOM CSS
# --------------------------------

st.markdown("""
<style>
.stApp {
    background-color: #111827;
}

.rook-board {
    display: grid;
    grid-template-columns: repeat(8, 1fr);
    width: min(100%, 480px);
    aspect-ratio: 1;
    margin: 15px auto;
    border: 4px solid #64748b;
}

.square {
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: clamp(20px, 5vw, 42px);
}

.light {
    background-color: #e5d5bd;
    color: #111827;
}

.dark {
    background-color: #64748b;
    color: white;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------
# LOAD AI SOLVER
# --------------------------------

@st.cache_data
def load_solutions():
    return run_solver()


solutions, stats, execution_time = load_solutions()


# --------------------------------
# SESSION STATE
# --------------------------------

if "current_solution" not in st.session_state:
    st.session_state.current_solution = None

if "trace" not in st.session_state:
    st.session_state.trace = []

if "trace_step" not in st.session_state:
    st.session_state.trace_step = 0


# --------------------------------
# CHESSBOARD DISPLAY FUNCTION
# --------------------------------

def display_board(board):

    html = '<div class="rook-board">'

    for row in range(8):
        for col in range(8):

            color = (
                "light" if (row + col) % 2 == 0
                else "dark"
            )

            symbol = "♜" if board[row] == col else ""

            html += (
                f'<div class="square {color}">'
                f'{symbol}</div>'
            )

    html += '</div>'

    st.markdown(html, unsafe_allow_html=True)


# --------------------------------
# GENERATE VISUALIZATION
# --------------------------------

def select_solution(index):

    st.session_state.current_solution = index

    selected = solutions[index]

    st.session_state.trace = generate_trace(selected)

    st.session_state.trace_step = 0


# --------------------------------
# MAIN HEADING
# --------------------------------

st.title("♜ Eight Rooks CSP Solver")

st.markdown(
    "An Artificial Intelligence project using "
    "Constraint Satisfaction Problems and Backtracking."
)

st.divider()


# --------------------------------
# MAIN DASHBOARD
# --------------------------------

left, right = st.columns([1.5, 1])


with left:

    st.subheader("Chessboard")

    b1, b2, b3 = st.columns(3)

    # SOLVE BUTTON
    with b1:

        if st.button("Solve", use_container_width=True):
            select_solution(0)

    # RANDOM SOLUTION BUTTON
    with b2:

        if st.button("Random Solution", use_container_width=True):

            index = random.randrange(len(solutions))

            select_solution(index)

    # RESET BUTTON
    with b3:

        if st.button("Reset", use_container_width=True):

            st.session_state.current_solution = None
            st.session_state.trace = []
            st.session_state.trace_step = 0

    # DISPLAY BOARD

    if st.session_state.current_solution is None:

        board = [-1] * 8

        st.info("Click Solve or Random Solution to begin.")

    else:

        board = solutions[
            st.session_state.current_solution
        ]

        st.success("Valid solution generated successfully!")

    display_board(board)


with right:

    st.subheader("Algorithm Information")

    st.metric(
        "Total Valid Solutions",
        f"{len(solutions):,}"
    )

    st.metric(
        "Constraint Checks",
        f"{stats['checks']:,}"
    )

    st.metric(
        "Rook Placements",
        f"{stats['placements']:,}"
    )

    st.metric(
        "Backtracking Operations",
        f"{stats['backtracks']:,}"
    )

    st.metric(
        "Execution Time",
        f"{execution_time:.6f} sec"
    )

    st.divider()

    st.subheader("CSP Configuration")

    st.write("**Variables:** 8 rows")

    st.write("**Domain:** Columns 0–7")

    st.write("**Constraints:** No two rooks in the same column")

    st.write("**Algorithm:** Recursive Backtracking")

    st.write("**Objective:** Place 8 non-attacking rooks")


# --------------------------------
# STEP-BY-STEP VISUALIZATION
# --------------------------------

st.divider()

st.header("AI Algorithm Visualization")

st.write(
    "Observe how the selected solution is constructed "
    "by placing one rook at a time."
)


if st.session_state.trace:

    trace = st.session_state.trace

    # PREVIOUS AND NEXT BUTTONS

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:

        if st.button("Previous Step", use_container_width=True):

            st.session_state.trace_step = max(
                0,
                st.session_state.trace_step - 1
            )

    with col3:

        if st.button("Next Step", use_container_width=True):

            st.session_state.trace_step = min(
                len(trace) - 1,
                st.session_state.trace_step + 1
            )

    # STEP SLIDER

    step = st.slider(
        "Move through the solution",
        min_value=0,
        max_value=len(trace) - 1,
        value=st.session_state.trace_step
    )

    st.session_state.trace_step = step

    current = trace[step]

    # DISPLAY MESSAGE

    st.subheader("Current Algorithm Step")

    st.write(current["message"])

    if current["type"] == "success":

        st.success("All 8 rooks placed successfully!")

    elif current["type"] == "place":

        st.info("Rook placed successfully.")

    # DISPLAY VISUALIZATION BOARD

    display_board(current["board"])

    st.caption(
        f"Step {step + 1} of {len(trace)}"
    )

else:

    st.info(
        "Generate a solution to see its step-by-step visualization."
    )


# --------------------------------
# PROJECT INFORMATION
# --------------------------------

st.divider()

st.header("About the Project")

st.write("""
The Eight Rooks CSP Solver is an Artificial Intelligence
application that solves the Eight Rooks problem using
Constraint Satisfaction Problems and recursive Backtracking.

The objective is to place eight rooks on an 8x8 chessboard
such that no two rooks attack each other.
""")

st.markdown("""
**Developed using:**
- Python
- Constraint Satisfaction Problems (CSP)
- Backtracking Algorithm
- Streamlit
""")

st.caption("Eight Rooks CSP Solver | AI Project")

#streamlit run app.py