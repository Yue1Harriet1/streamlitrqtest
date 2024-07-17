# Libraries
import streamlit as st
import pandas as pd
import threading
import os
from sqlalchemy import create_engine
import rqueue.ui_streamlit as ui
import rqueue.task as task
import time
from streamlit.runtime.scriptrunner import add_script_run_ctx

# Global Variables
theme_plotly = None # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Config
st.set_page_config(page_title='Multithreaded Streamlit', page_icon=':bar_chart:', layout='wide')

# Title
st.title('💸 Run Streamlit in Multi-threading')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)



with st.expander("# 🎯 Add New Task"):
    st.write("")
    form = st.form(key="annotation")
    func_input = {}
    with form:
        cols = st.columns(3)
        task_name = cols[0].selectbox("Task Type:", ["Concurrent - Multithreaded"], index=0)
        task1 = cols[1].radio("Task 1",["e.g.: sleeping, or downloading large online data"], captions = ["eask task with min CPU usage"])
        task2 = cols[2].radio("Task 2",["e.g.: counting, or doing someting else while waiting for task1 to complete"], captions = ["Count-down Timer"])

        job_name = task_name

        
        func = threading.Thread(target=task.sleep, args=[60])
        add_script_run_ctx(func)
        cols = st.columns(3)
        submitted1 = cols[1].form_submit_button(label="Submit Task 1")
        submitted2 = cols[2].form_submit_button(label="Submit Task 2")
        if submitted1:
            #new_task_id = utils.get_start_task_id(process_df)
            st.balloons()
            func.start()
            st.success(f"Submitted task 1 to execute in the **multi-threaded way**.")
            st.error("Task 1 Processing.......... !!!")
            st.error('Code is **NOT** blocked in main-thread and can move on to do other tasks while processing Task 1')
            
        if submitted2:
            st.balloons()
            t2 = threading.Thread(target=task.count_down, args=[60])
            add_script_run_ctx(t2)
            t2.start()
                
        if submitted2: 

            t2.join()
            st.success("Task 2 finished!")
            st.snow()











