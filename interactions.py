import streamlit as st
import random

def add_interactive_elements(current_page, total_pages):
    # Navigation buttons with page tracking
    col1, col2 = st.columns(2)
    
    with col1:
        if current_page > 0:
            if st.button("Previous"):
                st.session_state.page = max(0, st.session_state.page - 1)
                st.experimental_rerun()
    
    with col2:
        if current_page < total_pages - 1:
            if st.button("Next"):
                st.session_state.page = min(total_pages - 1, st.session_state.page + 1)
                st.experimental_rerun()
    
    # Optional: Add a fun random quote generator
    if st.button("Get a Random Birthday Quote"):
        birthday_quotes = [
            "Age is merely the number of years the world has been enjoying you!",
            "Birthdays are nature's way of telling us to eat more cake.",
            "Celebrate yourself today and every day!",
            "Another year of awesomeness begins now!"
        ]
        st.success(random.choice(birthday_quotes))