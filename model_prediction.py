import pandas as pd;
import streamlit as st;
import datetime
from streamlit import _RerunData
from streamlit import _RerunException
#from streamlit.script_runner import RerunException
from streamlit.source_util import get_pages

st.header("The estimate for your next month's cycle is : "+str(st.session_state['result']));
#st.session_state['dates_months'] = period_dates;
#date_input

start_date = st.session_state['dates_months'];
lengthofcycle=st.session_state['length_of_cycle'];
next_month_start_date = start_date[0][0]+datetime.timedelta(days=lengthofcycle);
next_month_end_date = next_month_start_date+datetime.timedelta(days =int(st.session_state['result']));
st.subheader('Calendar view of your menstrual cycle next month:')
sd = st.date_input('',value=[next_month_start_date,next_month_end_date]);




