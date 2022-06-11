import streamlit as st
import pandas as pd
import numpy as np


st.title('Greetings')
form = st.form(key='my_form')
name = form.text_input(label='Enter Your Name')
submit_button = form.form_submit_button(label='Submit')

if submit_button:
    st.write(f'Hello {name}')