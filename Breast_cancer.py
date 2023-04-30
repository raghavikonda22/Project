import streamlit as st;
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle
#machine learning models imported
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

#import sklearn metrics libraries
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.metrics import classification_report
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_validate, cross_val_score
from sklearn.svm import SVC
from sklearn import metrics


#data preprocessing :
import numpy as np;
import pandas as pd;

st.title("Breast Cancer Prediction");
#to read data from the csv file and show them on the screen;

df = pd.read_csv("pages/breastcancer.csv");
agree = st.checkbox('DataFrame of Breast Cancer');
if agree:
    st.dataframe(df);

#here try to put a list


#data visualization
option = st.selectbox('Data Visualization',('Histogram', 'Pair Plot', 'Scatter Plot','Corelation matrix'));

if option =='Histogram':
    sns.set_style('darkgrid')
    fig, ax = plt.subplots()
    fig = px.histogram(df, x='diagnosis')
    st.plotly_chart(fig, use_container_width=True)
elif option =='Pair Plot':
    #pair plot
    fig, ax = plt.subplots()
    cols = ["diagnosis", "radius_mean", "texture_mean", "perimeter_mean", "area_mean"];
    options = st.multiselect('select columns for pair plot',cols,["diagnosis"]);
    if len(options)==1:
        st.warning('please select columns');
    else:
        fig = sns.pairplot(df[options], hue="diagnosis");
        st.pyplot(fig);
elif option =='Scatter Plot':
#scatter plot
    fig,ax = plt.subplots();
    size = len(df['texture_mean'])
    area = np.pi * (15 * np.random.rand( size ))**2
    colors = np.random.rand( size )
    plt.xlabel("texture mean")
    plt.ylabel("radius mean")
    ax.scatter(df['texture_mean'], df['radius_mean'], s=area, c=colors, alpha=0.5);
    st.pyplot(fig);
elif option =='Corelation matrix':

    st.header("Find the correlation between other features, mean features only");
    # corerelation map
    fig, ax = plt.subplots()
    plt.figure(figsize=(12, 9))
    plt.title("Correlation Graph")
    cmap = sns.diverging_palette(1000, 120, as_cmap=True)
    cols = ["diagnosis", "radius_mean", "texture_mean", "perimeter_mean", "area_mean"];
    options = st.multiselect('What are your favorite colors', cols);
    if len(options) == 0:
        st.warning('please select columns');
    else:
        sns.heatmap(df[options].corr(), annot=True, fmt='.1%', linewidths=.05, cmap=cmap, ax=ax);
        st.pyplot(fig);

#to show the graph on the page
#exploratory data analysis
from sklearn.preprocessing import LabelEncoder
LE_Y = LabelEncoder()
df.diagnosis = LE_Y.fit_transform(df.diagnosis)

st.subheader("Label Encoding");
#radio buttons

#training the machine learning models;
prediction_feature = [ "radius_mean",  'perimeter_mean', 'area_mean', 'symmetry_mean', 'compactness_mean', 'concave points_mean']
targeted_feature = 'diagnosis'

#splitting of the input and outpput variables.
X = df[prediction_feature]
y = df.diagnosis


#printing on to the UI
type = st.radio("Data",( 'InputData', 'Output','Label Encoding'))

if type=='Label Encoding':
    st.dataframe(df);
elif type=='InputData':
    st.dataframe(X[:5]);
elif type =='Output':
    st.dataframe(y[:5]);

#split the datainto testing and training sets;
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=15)

#Scale the df to keep all the values in the same magnitude of 0 -1
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)


def model_building(model, X_train, X_test, y_train, y_test):
    """
    Model Fitting, Prediction And Other stuff
    return ('score', 'accuracy_score', 'predictions' )
    """
    model.fit(X_train, y_train)
    score = model.score(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(predictions, y_test)

    return (score, accuracy, predictions)

#w ehave logistic regression , random forest classifier & decision tree classfifier
models_list = {
    "Logistic" :  LogisticRegression(),
    "RandomForest" :  RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=5),
    "DecisionTree" :  DecisionTreeClassifier(criterion='entropy', random_state=0),
    "SVC" :  SVC(),
}


#to show the classification report & confusion matrix.


df_prediction = []
confusion_matrixs = []
df_prediction_cols = ['model_name', 'score', 'accuracy_score', "accuracy_percentage"]

for name, model in zip(list(models_list.keys()), list(models_list.values())):
    (score, accuracy, predictions) = model_building(model, X_train, X_test, y_train, y_test)

    print("\n\nClassification Report of '" + str(name), "'\n")

    print(classification_report(y_test, predictions))

    df_prediction.append([name, score, accuracy, "{0:.2%}".format(accuracy)])

    # For Showing Metrics
    confusion_matrixs.append(confusion_matrix(y_test, predictions))

df_pred = pd.DataFrame(df_prediction, columns=df_prediction_cols)

#accuray

st.subheader("Accuracy after training the models with different classifiers");

model_select = st.selectbox('Models Criteria',['Logistic','RandomForest','DecisionTree','SVC']);
if len(model_select)>0:
    st.dataframe(df_pred[df_pred['model_name'] == model_select]);
#graph plottign
fig,ax = plt.subplots();
X= list(df_pred['model_name']);
print(X);
y = list(df_pred['accuracy_score'])
# fig = plt.bar(X,y);
# plt.xlabel('Name of the model')
# plt.ylabel("Percentage")
# plt.title('Model Comparisions')
# plt.show()
if(st.button("accuracyComparision")):
    sns.barplot(data=df_pred, x="model_name", y="accuracy_score", ax=ax)

    st.pyplot(fig);
    st.success("Random Forest highest Accuracy ")

import streamlit as st
import streamlit.components.v1 as components
c1=components.html("""  
<form class="rating">
  <label>
    <input type="radio" name="stars" value="1" />
    <span class="icon">★</span>
  </label>
  <label>
    <input type="radio" name="stars" value="2" />
    <span class="icon">★</span>
    <span class="icon">★</span>
  </label>
  <label>
    <input type="radio" name="stars" value="3" />
    <span class="icon">★</span>
    <span class="icon">★</span>
    <span class="icon">★</span>   
  </label>
  <label>
    <input type="radio" name="stars" value="4" />
    <span class="icon">★</span>
    <span class="icon">★</span>
    <span class="icon">★</span>
    <span class="icon">★</span>
  </label>
  <label>
    <input type="radio" name="stars" value="5" />
    <span class="icon">★</span>
    <span class="icon">★</span>
    <span class="icon">★</span>
    <span class="icon">★</span>
    <span class="icon">★</span>
  </label>
</form>
<style>
.rating {
  display: inline-block;
  position: relative;
  height: 50px;
  line-height: 50px;
  font-size: 50px;
}

.rating label {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  cursor: pointer;
}

.rating label:last-child {
  position: static;
}

.rating label:nth-child(1) {
  z-index: 5;
}

.rating label:nth-child(2) {
  z-index: 4;
}

.rating label:nth-child(3) {
  z-index: 3;
}

.rating label:nth-child(4) {
  z-index: 2;
}

.rating label:nth-child(5) {
  z-index: 1;
}

.rating label input {
  position: absolute;
  top: 0;
  left: 0;
  opacity: 0;
}

.rating label .icon {
  float: left;
  color: transparent;
}

.rating label:last-child .icon {
  color: #000;
}

.rating:not(:hover) label input:checked ~ .icon,
.rating:hover label:hover input ~ .icon {
  color: #09f;
}

.rating label input:focus:not(:checked) ~ .icon:last-child {
  color: #000;
  text-shadow: 0 0 5px #09f;
} 
</style>
    """);
#Mood swings;




# Now add a submit button to the form:




