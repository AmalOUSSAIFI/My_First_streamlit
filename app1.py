import pandas as pd
import numpy as np 
import streamlit as st 
import pickle


clf_file = open('model.pkl','rb')
classifier = pickle.load(clf_file) 

def predict(country, year,location_type,
       cellphone_access, household_size, age_of_respondent,
       gender_of_respondent,education_level, job_type):
    pred= classifier.predict([[country, year,location_type,
       cellphone_access, household_size, age_of_respondent,
       gender_of_respondent,education_level, job_type]])
    return "The predicted value is" +str(pred)

def main():
    st.title('Financial inclusion in Africa')
    country = st.selectbox('country',['Kenya','Rawanda','Uganda','Tanzania'])
    year = st.selectbox('year',['2016,2017,2018'])
    location_type=st.selectbox('Location_Type', ['Urban','Rural'])
    cellphone_access=st.selectbox('Cellphone_Access', ['Yes','No'])
    household_size=st.number_input('Household_Size')
    age_of_respondent=st.number_input('Age_of_Respondent')
    gender_of_respondent=st.selectbox('Gender_of_Respondent', ['Male','Female'])
    education_level=st.selectbox('Education_Level', ['Primary education','Secondary education',
                'Vocational/Specialised training','Tertiary education','Other/Dont know/RTA'])
    job_type=st.selectbox('Job_Type', ['Farming and Fishing', 'Other Income', 'Self employed',
                'Formally employed Private', 'Remittance Dependent',
                'Informally employed', 'Formally employed Government',
                'Government Dependent', 'No Income', 'Dont Know/Refuse to answer'])
    
    result = ""
    if st.button("Predict"):
        result = predict(country, year,location_type,
       cellphone_access, household_size, age_of_respondent,
       gender_of_respondent,education_level, job_type)
        if result == 'No':
            st.success("Banking")
        else:
            st.success("Not Banking")
            
if __name__=="__main__":
    main()