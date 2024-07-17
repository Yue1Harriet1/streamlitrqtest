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
st.title('🪙 Demo: Fast Ordering in Streamlit Fast with Redis Task Queue')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

HOME_DIR = os.path.join(os.path.expanduser("~"), '.rqueue')
if not os.path.isdir(HOME_DIR):
    os.mkdir(HOME_DIR)


ui.demo_homepage(user_tasks=[task.Task(task.sleep, "default task name")], task_inputs={"seconds": 10})

