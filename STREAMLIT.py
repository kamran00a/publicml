import streamlit as st
import pickle
import pandas as pd
from sklearn.svm import SVC  
import numpy as np
#pipe=pickle.load(open('automl.pkl','rb'))
df=pickle.load(open(r"C:\Users\hp\Desktop\streamlit\df.pkl",'rb'))
pipe=pickle.load(open(r"C:\Users\hp\Desktop\streamlit\pipe.pkl",'rb'))


 
    
st.title("Football Goals Predictor")
team1=st.selectbox('team1', sorted(df.team1.unique()))
team2=st.selectbox('team2', sorted(df.team2.unique()))
stadium=st.selectbox('stadium', sorted(df.stadium.unique()))
temp=st.selectbox("Temperature (°C)",[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42
                                          ])
    
    
    
    


input_reshped=pd.DataFrame({'team1':[team1],'team2':[team2],'stadium':[stadium],'temp':[temp]})
predict=pipe.predict(input_reshped)

if st.button('Predict'):
    prediction = pipe.predict(input_reshped)
    st.balloons()
    if (prediction[0]==0):
         Goals="Predicted Goals are in between Zero to Two (0-2)"
    elif (prediction[0]==1):
         Goals="Predicted Goals are in between Two to Four (2-4)"
    elif (prediction[0]==2):
        Goals="Predicted Goals are in between Four to Six (4-6)"
    else:
         Goals="Predicted Goals are in between Six to Ten (6-10)"
    
    
    #st.success(f'Your predicted price of the laptop is {round(prediction[0],3)}')
    st.success(Goals)