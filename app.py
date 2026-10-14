import streamlit as st

from detective_cat.game import start_new_game
from detective_cat.styles import load_styles
from detective_cat.ui import (
    render_footer,
    render_game_board,
    render_header,
    render_result,
    render_rules,
    render_status,
)

st.set_page_config(
    page_title="Detective Cat",
    page_icon="🐾",
    layout="centered",
)


load_styles()


if "artifact_position" not in st.session_state:
    start_new_game()


render_header()
render_rules()
render_status()

st.divider()

render_game_board()

st.divider()

render_result()
render_footer()