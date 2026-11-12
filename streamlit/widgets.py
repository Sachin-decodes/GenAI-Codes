import streamlit as st
import pandas as pd
st.title('Your so called Bio-Data')

name=st.text_input("Enter the name: ",'JOHN')

if name:
    st.write(f"Welcome, {name} ")

age=st.slider('Enter your age',0,100,25)
st.write(f'Age: {age}')

options=['Python','JavaScript','C++','Java']
choice=st.selectbox('choose your favourite programming language ',options)
st.write(f"You have opted for {choice}")

st.write("This is just a sample dataFrame ")
df=pd.DataFrame({
    'usn':['1SI24IS084','1SI24IS090','1SI24IS078','1SI24IS096'],
    'name':['Sachin','Samridh','Rehan','Shivesh'],
    'Address':['Muzaffarpur','Gaya','Patna','Jammu']
})

st.write(df)

file_uploaded=st.file_uploader(f"Upload a csv file",type="csv")
if file_uploaded:
    data=pd.read_csv(file_uploaded)
    st.write(data)

else:  
    st.write(f"File content not available")