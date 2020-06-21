#!/usr/bin/env python
# coding: utf-8

# # Predict Auto Insurance Fraud

# In[1]:


import pickle
import numpy as np
import streamlit as st
import pandas as pd


# In[2]:


# load the model from disk
loaded_model = pickle.load(open('Streamlit_Autoinsurancefraud1.sav', 'rb'))


# In[3]:


# Creating the Titles and Image

st.title("Predict Auto Insurance fraud claim")
st.header("Predicting if a claim requested for an auto insurance policy is genuine or fraud")


# In[4]:


# create the dropdown menus for input fields

DropDown1 = pd.DataFrame({'insured_hobbies': ['chess', 'cross-fit','other'],
                          'policy_deductable': [500,1000,2000],
                          'police_report_available': ['YES','NO','other']})
DropDown2 = pd.DataFrame({'collision_type': ['Rear Collision', 'Side Collision', 'Front Collision','other'],
                          'incident_severity': ['Minor Damage','Total Loss','Major Damage','Trivial Damage'],
                          'incident_type': ['Multi-vehicle Collision','Single Vehicle Collision','Vehicle Theft','Parked Car']})
DropDown3 = pd.DataFrame({'authorities_contacted': ['Police', 'Fire', 'Ambulance','Other','None']})
DropDown4 = pd.DataFrame({'umbrella_limit': [0,2000000,3000000,4000000,5000000,6000000,7000000,8000000,9000000,10000000]})                        


# In[5]:


# take user inputs

insured_hobbies = st.selectbox('Hobbies',DropDown1['insured_hobbies'].unique())
policy_deductable = st.selectbox('Policy deductable',DropDown1['policy_deductable'].unique())
police_report_available = st.selectbox('Is Police Report available ?',DropDown1['police_report_available'].unique())
collision_type = st.selectbox('Type of collision',DropDown2['collision_type'].unique())
incident_severity = st.selectbox('Severity of incident',DropDown2['incident_severity'].unique())
incident_type = st.selectbox('Type of incident',DropDown2['incident_type'].unique())
authorities_contacted = st.selectbox('Type of authorities contacted',DropDown3['authorities_contacted'].unique())
umbrella_limit = st.selectbox('Select umbrella limit',DropDown4['umbrella_limit'].unique())
months_as_customer = st.number_input('Duration stayed with the insurer: Select any number between 0 - 500')
vehicle_claim = st.number_input('Amount requested: Select any value between 0 - 80000')
number_of_vehicles_involved = st.slider("Number of vehicles involved", 1, 4)
bodily_injuries = st.slider("Number of injuries", 0, 2)
witnesses = st.slider("Number of witnesses", 0, 3)

# dealing with input passed by user in the app and converting them back to type understandable by the machine learning algorithm

# insured_hobbies
if insured_hobbies == 'chess':
    hobby = 0
else:
    if insured_hobbies == 'cross-fit':
        hobby = 1
    else:
        hobby = 2
        
# police_report_available
if police_report_available == 'other':
    report = 0
else:
    if police_report_available == 'NO':
        report = 1
    else:
        report = 2
        
# collision_type
if collision_type == 'other':
    collision = 0
else:
    if collision_type == 'Front Collision':
        collision = 1
    else:
        if collision_type == 'Rear Collision':
            collision = 2     
        else:
            collision = 3

# incident_severity
if incident_severity == 'Major Damage':
    severity = 0
else:
    if incident_severity == 'Minor Damage':
        severity = 1
    else:
        if incident_severity == 'Total Loss':
            severity = 2     
        else:
            severity = 3
        
# incident_type
if incident_type == 'Multi-vehicle Collision':
    incident = 0
else:
    if incident_type == 'Parked Car':
        incident = 1
    else:
        if incident_type == 'Single Vehicle Collision':
            incident = 2     
        else:
            incident = 3
        

# authorities_contacted
if authorities_contacted == 'Ambulance':
    authorities = 0
else:
    if authorities_contacted == 'Fire':
        authorities = 1
    else:
        if authorities_contacted == 'None':
            authorities = 2 
        else:
            if authorities_contacted == 'Other':
                authorities = 3     
            else:
                authorities = 4
        


# In[6]:


# store the inputs

features = [umbrella_limit, hobby, policy_deductable, report, collision, severity, incident, authorities, months_as_customer,
            vehicle_claim, number_of_vehicles_involved, bodily_injuries, witnesses]

# convert user inputs into an array for the model
int_features = [int(x) for x in features]
final_features = [np.array(int_features)]

if st.button('Predict'):
    prediction = loaded_model.predict(final_features)
    st.balloons()
    if round(prediction[0],2) == 1:
        st.success('The claim reported is fraud.')
    else:
        st.success('The claim reported is genuine.')
st.success(features)


# In[7]:


# Save in C folder as 'streamlitpredictautoinsurancefraud1' as python extension.

