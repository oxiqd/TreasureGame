import streamlit as st

from .config import BOARD_SIZE, MAX_MOVES
from .game import get_cell_label, get_rank, make_move, start_new_game
from .messages import RULES_HTML, SUBTITLE_HTML, TITLE_HTML


def render_header():
    st.markdown(TITLE_HTML, unsafe_allow_html=True)
    st.markdown(SUBTITLE_HTML, unsafe_allow_html=True)


def render_rules():
    st.markdown(RULES_HTML, unsafe_allow_html=True)


def render_status():
    message_col, moves_col = st.columns([2, 1])

    with message_col:
        st.markdown(
            f'<p class="hint-text">{st.session_state.message}</p>',
            unsafe_allow_html=True,
        )

    with moves_col:
        st.metric("Moves", f"{st.session_state.moves} / {MAX_MOVES}")

    progress = st.session_state.moves / MAX_MOVES
    st.progress(progress)


def render_game_board():
    for row in range(BOARD_SIZE):
        columns = st.columns(BOARD_SIZE)

        for col in range(BOARD_SIZE):
            label = get_cell_label(row, col)

            if columns[col].button(
                label,
                key=f"cell-{row}-{col}",
                use_container_width=True,
                disabled=st.session_state.found or st.session_state.game_over,
            ):
                make_move(row, col)
                st.rerun()


def render_result():
    if st.session_state.found:
        st.success(f"You won! Rank: {get_rank()}.")

    elif st.session_state.game_over:
        st.error("Game over. The hidden artifact was not found.")


def render_footer():
    restart_col, info_col = st.columns([1, 2])

    with restart_col:
        if st.button("New game", use_container_width=True):
            start_new_game()
            st.rerun()

    with info_col:
        checked_cells = len(st.session_state.visited_cells)

        st.markdown(
            f'<p class="small-muted">Checked cells: {checked_cells} / {BOARD_SIZE * BOARD_SIZE}</p>',
            unsafe_allow_html=True,
        )