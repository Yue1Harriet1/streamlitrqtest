# Libraries
import streamlit as st
import pandas as pd
import time



def make_an_order(food_name:str, seconds:int):
    ph = st.empty()
    st.write(f"You've ordered {food_name}! Ready in {seconds}")
    time.sleep(seconds)