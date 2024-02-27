import streamlit as st
from datetime import datetime
import json
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="2024 | Samar",
    layout="centered",  # Center everything on the page
    initial_sidebar_state="collapsed",  # Lock the sidebar by default
)

def calculate_percentage(start_date, end_date):
    total_days = (end_date - start_date).days + 1
    today = datetime.now()
    days_elapsed = (today - start_date).days + 1
    percentage_completed = (days_elapsed / total_days) * 100
    return percentage_completed

def main():

    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    percentage_completed = int(calculate_percentage(start_date, end_date))
    
    # Centering everything
    st.write('<div style="text-align: center;">', unsafe_allow_html=True)
    
    st.title(f"2024 is {percentage_completed}% over")
    st.progress(percentage_completed / 100)

    st.write("\"Time is free, but it's priceless. You can't own it, but you can use it. You can't keep it, but you can spend it. Once you've lost it you can never get it back.\" - Harvey Mackay")
    
    st.write('</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
