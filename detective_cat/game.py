import random

import streamlit as st

from .config import BOARD_SIZE, MAX_MOVES
from .messages import ALREADY_CHECKED_MESSAGE, GAME_OVER_MESSAGE, START_MESSAGE


def start_new_game():
    st.session_state.artifact_position = (
        random.randint(0, BOARD_SIZE - 1),
        random.randint(0, BOARD_SIZE - 1),
    )

    st.session_state.visited_cells = set()
    st.session_state.moves = 0
    st.session_state.found = False
    st.session_state.game_over = False
    st.session_state.message = START_MESSAGE
    st.session_state.last_cell = None


def get_distance(row, col):
    artifact_row, artifact_col = st.session_state.artifact_position

    return abs(row - artifact_row) + abs(col - artifact_col)


def get_hint(distance):
    if distance == 0:
        return "💎 Artifact found!"

    if distance == 1:
        return "🔥 Hot! The artifact is very close."

    if distance <= 2:
        return "🌤 Warm. You are near the artifact."

    return "❄️ Cold. Try another area."


def get_rank():
    if st.session_state.moves <= 4:
        return "Legendary detective"

    if st.session_state.moves <= 7:
        return "Sharp investigator"

    if st.session_state.moves <= 10:
        return "Careful searcher"

    return "Lucky cat"


def make_move(row, col):
    if st.session_state.found or st.session_state.game_over:
        return

    clicked_cell = (row, col)

    if clicked_cell in st.session_state.visited_cells:
        st.session_state.message = ALREADY_CHECKED_MESSAGE
        return

    st.session_state.visited_cells.add(clicked_cell)
    st.session_state.last_cell = clicked_cell
    st.session_state.moves += 1

    distance = get_distance(row, col)

    st.session_state.message = get_hint(distance)

    if distance == 0:
        st.session_state.found = True
        return

    if st.session_state.moves >= MAX_MOVES:
        st.session_state.game_over = True
        st.session_state.message = GAME_OVER_MESSAGE


def get_cell_label(row, col):
    current_cell = (row, col)

    is_artifact_cell = current_cell == st.session_state.artifact_position
    is_visited = current_cell in st.session_state.visited_cells
    is_last_cell = current_cell == st.session_state.last_cell

    if st.session_state.found and is_artifact_cell:
        return "💎"

    if st.session_state.game_over and is_artifact_cell:
        return "👻"

    if is_last_cell:
        return "🐈"

    if is_visited:
        return "🐾"

    return "⬜"