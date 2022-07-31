import numpy as np
import streamlit as st
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

loaded_model=joblib.load(open('trained_model.joblib', 'rb'))

st.header("Predicting Clinker Mineralogy")
df=pd.DataFrame(columns={'Al2O3','Cao','Fe2O3','MgO','SO3','SiO2','FCaO''LSF','SM','AF','LIQUID','LT_WT','K2O','Na2O','TiO2'})

st.sidebar.header("Specify input parameters:")
def user_input():
    Al2O3=st.sidebar.slider('Al2O3',0.0,15.0,7.5)
    CaO=st.sidebar.slider('Cao',0.0,100.0,50.0)
    Fe2O3=st.sidebar.slider('Fe2O3',3.0,7.0,5.0)
    MgO=st.sidebar.slider('MgO',1.0,2.5,1.75)
    SO3=st.sidebar.slider('SO3',0.1,2.0,1.5)
    SiO2=st.sidebar.slider('SiO2',19.9,24.0,22.0)
    FCaO=st.sidebar.slider('FCaO',0.4,4.0,2.0)
    LSF=st.sidebar.slider('LSF',85.0,120.0,100.0)
    SM=st.sidebar.slider('SM',0.0,5.0,2.5)
    AF=st.sidebar.slider('AF',0.0,5.0,2.5)
    LIQUID=st.sidebar.slider('LIQUID',22.0,35.0,28.0)
    LT_WT=st.sidebar.slider('LT_WT',700.0,1600.0,1250.0)
    K2O=st.sidebar.slider('K2O',0.0,4.0,2.0)
    Na2O=st.sidebar.slider('Na2O',0.0,4.0,2.0)
    TiO2=st.sidebar.slider('TiO2',0.0,0.5)
    input={'Al2O3':Al2O3,
           'CaO':CaO,
           'Fe2O3':Fe2O3,
           'MgO':MgO,
           'SO3':SO3,
           'SiO2':SiO2,
           'FCaO':FCaO,
           'LSF':LSF,
           'SM':SM,
           'AF':AF,
           'LIQUID %':LIQUID,
           'LT.WT Gm/Ltr':LT_WT,
           'K2O':K2O,
           'Na2O':Na2O,
           'TiO2':TiO2}
    features=pd.DataFrame(input,index=[0])
    return features

input=user_input()


prediction=loaded_model.predict(input)
pred=pd.DataFrame(data=prediction,columns=['C3S','C2S','C3A','C4AF'])
st.header("Predictions:")
st.write(pred)
st.bar_chart(pred)