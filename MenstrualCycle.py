import streamlit as st;
import numpy as np;
import datetime;
from sklearn.preprocessing import StandardScaler
st.header("Menstrual Cycle ");
import pickle;
from streamlit import _RerunData
from streamlit import _RerunException
#from streamlit.script_runner import RerunException
from streamlit.source_util import get_pages


def switch_page(page_name: str):
    def standardize_name(name: str) -> str:
        return name.lower().replace("_", " ")


    page_name = standardize_name(page_name)

    pages = get_pages("streamlit_app.py")  # OR whatever your main page is called

    for page_hash, config in pages.items():
        if standardize_name(config["page_name"]) == page_name:
            raise _RerunException(
                _RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
            )
        )

    page_names = [standardize_name(config["page_name"]) for config in pages.values()]

    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")


def predict_model(X_test):
    filename = 'finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    print("x_test : ",X_test);
    scaler = StandardScaler()
    #X_test = scaler.fit_transform(X_test);
    #X_test=[11.660 ,73.70,421.0,0.1671,0.03630,0.01162]
    result = loaded_model.predict(X_test)
    print(result[0]);
    print(" prediction model ")
    st.header(result[0]);
    st.session_state['result']=result[0];
    print(st.session_state);
    switch_page("model_prediction")

#input the data for prediction;
#st.text_input("Cycle is heavy or not");
X_new = [];
cycle = st.radio("How is your flow in the current cycle?",options=["High", "Normal"]);

if cycle == "High":
    X_new.append(1);
else:
    print(" cycle is normal !!!");
    X_new.append(0);

#ReproductiveCategory

Reprod_category = st.multiselect('Reproductive Category ',[0,1,2,9]);
print(Reprod_category);
if len(Reprod_category)>=1:
    X_new.append(Reprod_category[0]);

#LengthofCycle

#minimum 18 days to 54 days

length_of_cycle = st.number_input('What is your current cycle length?',min_value=18,max_value = 54, step=1);
X_new.append(length_of_cycle);
st.session_state['length_of_cycle']=length_of_cycle;
#EstimatedDayofOvulation

Estimatd_day_of_ovulation = st.select_slider('Select day of ovulation',options=[i for i in range(0,31)]);
X_new.append(Estimatd_day_of_ovulation);

#LengthofLutealPhase
Length_of_Luteal_Phase = st.select_slider('Length of Luteal Phase',options=[i for i in range(1,50)]);
X_new.append(Length_of_Luteal_Phase);


#TotalDaysofFertility
TotalDaysofFertility = st.number_input('Enter total fertility days',min_value=0,max_value = 27, step=1);
X_new.append(TotalDaysofFertility);


#TotalFertilityFormula
TotalFertilityFormula = st.number_input('Enter total fertility formula',min_value=3,max_value = 40, step=1);
X_new.append(TotalFertilityFormula);

#input the calender data and store or show for last 3 months dhani
# start_date = st.date_input('Period start_date and end date ! ',value = [datetime.date(2023, 4, 15),datetime.date(2023,4,20)]);
# print(start_date);
# if start_date:
#     lm= start_date[1]-start_date[0];
#     LengthofMenses = lm.days;
#     print("LengthofMenses ",LengthofMenses);
#     X_new.append(LengthofMenses);
#LengthofMenses

#inthe next phase we will  try add a calender and then get the data out of it for the past months;

#LengthofMenses = st.select_slider('LengthofMenses',options=[i for i in range(2,15)]);
col1 , col2 = st.columns(2);
if 'n_rows' not in st.session_state:
    st.session_state.n_rows = 1
add = st.button(label="+")
sub = st.button(label="-")
with col1:
    if add:
        st.session_state.n_rows += 1
        st.experimental_rerun()
with col2:
    if sub:
        if st.session_state.n_rows>0:
            st.session_state.n_rows -= 1
            st.experimental_rerun()
        else:
            st.warning("all the text boxes were deleted")
period_dates=[];
for i in range(st.session_state.n_rows):
    start_date = st.date_input('what are the current period start and enddate?'+str(i)+" month ",value=[datetime.date(2023, 4, 15), datetime.date(2023, 4, 20)]);
    period_dates.append(start_date);

st.session_state['dates_months'] = period_dates;
#get the average of those mensus cycle

with st.form("my_form"):
   st.subheader("Symptoms ")
   st.radio("Tension",( 'Low', 'Medium','High'));
   st.slider("Weight Gain",min_value=0,max_value=10);
   st.radio("Moodiness",('Low','Medium','High'));
   st.selectbox("Body Aches",['Low','Medium','High']);
   st.radio("PMS", ('Low', 'Medium', 'High'));
   st.select_slider("Shoulder Aches", options=['Low', 'Medium', 'High']);
   st.selectbox("Neck Aches", ['Low', 'Medium', 'High']);
   # Every form must have a submit button.
   submitted = st.form_submit_button("Predict")
   if submitted:
       each_month = [];
       # save the button
       for i in period_dates:
           lm = i[1] - i[0];
           LengthofMenses = lm.days;
           each_month.append(lm.days);
       print(X_new);
       X_new.append(sum(each_month) / len(each_month));
       print("inside the period dates")
       print(X_new);
       X_test = [X_new];
       X_test = np.array(X_test);
       print(X_test);
       predict_model(X_test);


#
# print(X_test);
#train the machine learning model and then convert it into .h5 file for the ml processing;
















