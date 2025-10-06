import streamlit as st

def get_name():
    st.write("Thai")

agree = st.checkbox("I agree", on_change=get_name)

if agree:
    st.write("Great!")

st.radio(
    "Your favorite color:",
    ['Yellow', 'Blue'],
    captions=['Vàng', 'Xanh']
)
