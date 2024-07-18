# Libraries
import streamlit as st
import pandas as pd
import multiprocessing
import os
from sqlalchemy import create_engine
import streamlitrq.ui_streamlit as ui
import streamlitrq.task as task
import time
from streamlit.runtime.scriptrunner import add_script_run_ctx

# Global Variables
theme_plotly = None # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Config
st.set_page_config(page_title='Multitprocessing Streamlit', page_icon=':bar_chart:', layout='wide')

# Title
st.title('💸 Run Streamlit Tasks in Multi-processes')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)



with st.expander("# 🎯 Add New Task"):
    st.write("")
    form = st.form(key="annotation")
    func_input = {}
    with form:
        cols = st.columns(3)
        task_name = cols[0].selectbox("Task Type:", ["Multitprocessing"], index=0)
        task1 = cols[1].radio("Task 1",["e.g.: sleeping"], captions = ["run in process 1"])
        task2 = cols[2].radio("Task 2",["e.g.: counting"], captions = ["Count-down Timer in process 2"])

        job_name = task_name

        
        func = multiprocessing.Process(target=task.sleep, args=[60])
        add_script_run_ctx(func)
        cols = st.columns(3)
        submitted1 = cols[1].form_submit_button(label="Submit Task 1")
        submitted2 = cols[2].form_submit_button(label="Submit Task 2")
        if submitted1:
            #new_task_id = utils.get_start_task_id(process_df)
            st.balloons()
            func.start()
            st.success(f"Submitted task 1 to execute in the **multi-processes way**.")
            st.error("Task 1 Processing.......... !!!")
            st.error('Code is **NOT** blocked in main-thread and can move on to do other tasks while processing Task 1')
            
        if submitted2:
            st.balloons()
            t2 = multiprocessing.Process(target=task.spinner, args=[60])
            #add_script_run_ctx(t2)
            t2.start()
                
        if submitted2: 

            t2.join()
            st.success("Task 2 finished in a different process!")
            st.snow()











