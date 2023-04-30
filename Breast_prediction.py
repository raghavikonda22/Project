import streamlit as st;
import pickle;
from sklearn.preprocessing import StandardScaler



st.header("Enter the Breast Cancer symptoms")
#data input for the prediction whether is it breast cancer or not;
radiusmean = st.number_input('radius_mean',min_value=6.0,max_value=29.0,step=0.001);
pmean = st.number_input('perimeter_mean',min_value=43.0,max_value=189.0,step=0.01);
areamean = st.number_input('area_mean',min_value=143.0,max_value=2501.0,step=0.5);
symmetricmean = st.select_slider('symmetry_mean',options=[i/1000 for i in range(100,304)]);
compactmean= st.select_slider('compactness_mean',options=[i/100000 for i in range(1938,34540)]);
cpointsmean = st.select_slider('concave points_mean',options=[i/10000 for i in range(0,2012)]);
#get the inputs and then load them into thte file;

def predict_model(X_test):
    filename = 'pages/RandomForestClassifier.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    scaler = StandardScaler()
    X_test = scaler.fit_transform(X_test);
    #X_test =[[-0.80661002, -0.85857337, -0.75422051, -0.44179819, -1.28962021, -1.00393917]]
    print("X_test :::: ",X_test)
    result = loaded_model.predict(X_test)
    print(result);
    print(" prediction model ");
    if(result[0]==1):
        st.error("cancer Diagnoised");
    else:
        st.success("Not a cancer");
        st.balloons();
    st.header(result[0]);


x_t = [radiusmean,pmean,areamean,symmetricmean,compactmean,cpointsmean]

if(st.button('predict')):
    predict_model([x_t]);


