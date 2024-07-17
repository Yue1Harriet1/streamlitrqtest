# Libraries
import streamlit as st
import pandas as pd
import rqueue.ui_streamlit as ui
import os
from sqlalchemy import create_engine
from rqueue import task
import time
import mytask


# Global Variables
theme_plotly = None # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Config
st.set_page_config(page_title='Fees - Cross Chain Monitoring', page_icon=':bar_chart:', layout='wide')

# Title
st.title('🪙 Fast Ordering in Streamlit Fast with Redis Task Queue')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

HOME_DIR = os.path.join(os.path.expanduser("~"), '.rqueue')
if not os.path.isdir(HOME_DIR):
    os.mkdir(HOME_DIR)

APP_ENGINE_PATH = f"sqlite:///{HOME_DIR}/process_data.db"
sql_engine = create_engine(APP_ENGINE_PATH, echo=False)



foods = ["Beef Burger", "Chicken Burger", "Fries", "Ice Lemon Tea"]
task_list = [task.Task(mytask.make_an_order, f) for f in foods]
ui.homepage(sql_engine, task_list)
