import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
import joblib
import streamlit as st
from sklearn.pipeline import Pipeline

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

from lightgbm import LGBMClassifier


with open("Lightgbmmodel.pkl","rb") as f:
    model=joblib.load("Lightgbmmodel.pkl")

    
def main():
    
    data = {
    'Gender' : [],
    "Admission_type_id" : [0],
    'discharge_disposition_id' : [0],
    'admission_source_id' : [0],
    'time_in_hospital' : [0],
    'num_lab_procedures' : [0],
    "num_procedures" : [0],
    "num_medications" : [0],
    "number_outpatient" : [0],
    "number_emergency" : [0],
    "number_inpatient" : [0],
    'diag_1':[0],
    'diag_2':[0],
    'diag_3':[0],
    'number_diagnoses':[0],
     'max_glu_serum':[],
     'A1Cresult':[],
      'metformin':[],
      'glimepiride':[],
      'glipizide':[],
        'glyburide':[],
       'pioglitazone':[], 
        'rosiglitazone':[],
        'insulin':[],
        'change':[],
       'diabetesMed':[],
        'race':[],
        'age':[]      
         }
    
    
    
    st.sidebar.title("Diabetic Patients Readmission Prediction 📊")
    
    gen = st.radio(

    "Enter gender of the patient",

    ('Male','Female'))
    data["Gender"].append(gen)

    
    age = st.radio(

    "What is the age interval of the patient?",

    ('(0-10)' ,'(10-20)' ,'(20-30)', '(30-40)', '(40-50)', '(50-60)', '(60-70)','(70-80)', '(80-90)' ,'(90-100)'))
    data["age"].append(age)
    
    
    
    rc = st.radio(

    "Which race does the patient affiliate with ?",

    ('Caucasian', 'AfricanAmerican' ,'Other' ,'Asian' ,'Hispanic'))
    
    data["race"].append(rc)
    
    
    
    mgs = st.radio(

    "What is the glucose range in the blood?",

    ('None', '>300', 'Norm', '>200'))
    
    data["max_glu_serum"].append(mgs)
    
    
    a1c = st.radio(

    "What is the range of the result?",

    ('None', '>7' ,'>8' ,'Norm'))
    
    data["A1Cresult"].append(a1c)
    
    
    mef = st.radio(

    "What is the range of the result for metformin?",

    ('No', 'Steady' ,'Up' ,'Down'))
    
    data["metformin"].append(mef)
     
        
    glp = st.radio(

    "What is the range of the result for glimepiride?",

    ('No', 'Steady' ,'Up' ,'Down'))
    
    data["glimepiride"].append(glp)
    
    
    
    gld = st.radio(

    "What is the range of the result for glipizide?",

    ('No', 'Steady' ,'Up' ,'Down'))
        
    data["glipizide"].append(gld)
    
    
    
    glb = st.radio(

   "What is the range of the result for glyburide?",

    ('No', 'Steady' ,'Up' ,'Down'))
    
    data["glyburide"].append(glb)
    
    
    
    pio = st.radio(

    "What is the range of the result for pioglitazone?",

    ('No', 'Steady' ,'Up' ,'Down'))
    
    data["pioglitazone"].append(pio)
    
    
    ros = st.radio(

    "What is the range of the result for rosiglitazone?",

    ('No', 'Steady' ,'Up' ,'Down'))
    
    data["rosiglitazone"].append(ros)
    
    ins = st.radio(

    "What is the range of the result for insulin?",

    ('No', 'Steady' ,'Up' ,'Down'))
    
    data["insulin"].append(ins)
    
    
    ch = st.radio(

    "What is the change in the condition of the patient in the year preceding the encounter?",

    ('No', 'Change' ))
    
    data["change"].append(ch)
    
    
    dm = st.radio(

    "Does the patient has any diabetic medication prescribed?",

    ('No', 'Yes' ))
    
    data["diabetesMed"].append(dm)
    
    
    
    
    
    
    dia1 = st.number_input("Enter the primary diagonsis code of the patient")
    dia2 = st.number_input("Enter the secondry diagonsis code of the patient")
    dia3 = st.number_input("Enter the tertiary diagonsis code of the patient")
    admtype = st.number_input("Enter admission type id of the patient")
    disid = st.number_input("Enter the previously discharge code of the patient")
    asid = st.number_input("Enter the admission sorce of the patient")
    time = st.number_input("Enter the number of days between admission and discharge")
    numlp = st.number_input("Enter the number lab procedure performed on patient")
    nump = st.number_input("Enter the number of procedures (other than lab tests) performed during the encounter")
    numm = st.number_input("Enter the number of distinct generic names administered during the encounter")
    numlo = st.number_input("Enter the number of outpatient visits of the patient in the year preceding the encounter")
    numle = st.number_input("Enter the number of emergency visits of the patient in the year preceding the encounter")
    numle = st.number_input("Enter the number of inpatient visits of the patient in the year preceding the encounter")
    numd = st.number_input("Enter the number of diagnoses entered to the system ")

    data["diag_1"] = [dia1]
    data["diag_2"]=[dia2]
    data["diag_3"] = [dia3]
    data["Admission_type_id"] = [admtype]
    data["discharge_disposition_id"] = [disid]
    data["admission_source_id"] = [asid]
    data["time_in_hospital"] = [time]
    data["num_lab_procedures"] = [numlp]
    data["num_procedures"] = [nump]
    data["num_medications"] = [numm]
    data["number_outpatient"] = [numo]
    data["number_emergency"] = [nume]
    data["number_inpatient"] = [numip]
    data["number_diagnoses"] = [numd]
    
    
    data = pd.DataFrame(data)
    st.write(data)
    
    if st.button("Predict"):
        p=model.predict(data)
        if p==1:
            st.write("Patient has high chance of readmitting")
            
        else :
            st.write("Patient haslow chance of readmitting")
    
    
    
if __name__ =='__main__':
    main()
