import pandas as pd;
import streamlit as st;
import datetime
from streamlit import _RerunData
from streamlit import _RerunException
#from streamlit.script_runner import RerunException
from streamlit.source_util import get_pages

st.header(" next menstrual cyccle number of days : "+str(st.session_state['result']));
#st.session_state['dates_months'] = period_dates;
#date_input
st.session_state['length_of_cycle']
start_date = st.session_state['dates_months'];
print(start_date)
lengthofcycle=st.session_state['length_of_cycle'];
next_month_start_date = start_date[0][0]+datetime.timedelta(days=lengthofcycle);
next_month_end_date = next_month_start_date+datetime.timedelta(days =int(st.session_state['result']));

sd = st.date_input('Predicted next month period days ',value=[next_month_start_date,next_month_end_date]);

