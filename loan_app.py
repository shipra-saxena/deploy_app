from pycaret.classification import *
import streamlit as st
import numpy as np
import pandas as pd

model= load_model('/home/shipra/Downloads/deployed_model')
def predict(model, input_df):
  predictions_df= predict_model(model,data=input_df)
  prediction= predictions_df['Label'][0]
  return prediction
  
  
def run(): 
    st.title('Loan Prediction APP') 
    Dependents  = st.selectbox('Dependents',("1","2","3+"))
    Married = st.selectbox('Marital Status',("Unmarried","Married"))
    Education = st.selectbox('Education',("Graduate","Not Graduate"))
    Self_employed = st.selectbox('Self Employed',("Yes","No"))
    ApplicantIncome = st.number_input("Applicants monthly income")
    LoanAmount = st.number_input("Total loan amount")
    LoanTerm = st.number_input("Total loan Term")
    Credit_History = st.selectbox('Credit_History',("Unclear Debts","No Unclear Debts"))
    Property_area= st.selectbox('Property Area',('Rural','SemiUrban','Urban'))
    result =""
    input_dict={ 'Dependents': Dependents, 'Married':  Married,'Education':Education,'Self_employed':Self_employed,'ApplicantIncome':ApplicantIncome, 'LoanAmount':LoanAmount,'LoanTerm':LoanTerm,'Credit_History':Credit_History,'Property_area':Property_area }
    input_df= pd.DataFrame([input_dict])
    
    if st.button("Predict"):
        
        result = predict(model=model, input_df=input_df) 
        st.success('Your loan is {}'.format(result))
        print(LoanAmount)
        
if __name__=='__main__': 
    main()