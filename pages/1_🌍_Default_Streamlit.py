# Libraries
import streamlit as st
import pandas as pd
import os
from sqlalchemy import create_engine
import streamlitrq.ui_streamlit as ui
import streamlitrq.task as task
import time

# Global Variables
theme_plotly = None # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Config
st.set_page_config(page_title='Default Streamlit', page_icon=':bar_chart:', layout='wide')

# Title
st.title('🌍 Run Streamlit in the default way - single-threaded')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)




with st.expander("# 🎯 Add New Task"):
    st.write("")
    form = st.form(key="annotation")
    func_input = {}
    with form:
        cols = st.columns(2)
        task_name = cols[0].selectbox("Task:", ["Default - single-threaded"], index=0)
        task_type = cols[1].selectbox("Task Type:", ["Default - single-threaded", "Concurrent - Multithreaded"], index=0)
        job_name = task_name

        if task_name: 
            func = task.sleep
        else: comment = st.text_area("Notes:")
        cols = st.columns(2)
        submitted = cols[0].form_submit_button(label="Submit")
        if submitted:
            #new_task_id = utils.get_start_task_id(process_df)
            st.balloons()
            st.success(f"Submitted task to execute in the **default way.. single-threadedly**.")
            st.error('**Get updates** button above is **greyed out** because everything upcoming is BLOCKED until the completion of the current submitted task...including the code for **Get updates** button...')
            if 'Default' in task_type:
                new_task_id = 1
                st.success(func(60))
                st.success('Now you can see the code for **Get updates** button, which can be clicked and upcoming things can move forward..')

        refreshed = cols[0].form_submit_button(label="Get updates")
        if refreshed:
            task.count_down(60)







