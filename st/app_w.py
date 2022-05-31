import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(
    page_title="Financial Planning Calculator")

st.title("Financial Planning Calculator")

st.header("**Monthly Income**")
st.subheader("Salary")
colAnnualSal, colTax = st.beta_columns(2)

with colAnnualSal:
    salary = st.number_input("Enter your annual salary($): ", min_value=0.0, format='%f')
with colTax:
    tax_rate = st.number_input("Enter your tax rate(%): ", min_value=0.0, format='%f')

tax_rate = tax_rate / 100.0
salary_after_taxes = salary * (1 - tax_rate)
monthly_takehome_salary = round(salary_after_taxes / 12.0, 2)

st.header("**Monthly Expenses**")
colExpenses1, colExpenses2 = st.beta_columns(2)

with colExpenses1:
    st.subheader("Monthly Rental")
    monthly_rental = st.number_input("Enter your monthly rental($): ", min_value=0.0,format='%f' )
    
    st.subheader("Daily Food Budget")
    daily_food = st.number_input("Enter your daily food budget ($): ", min_value=0.0,format='%f' )
    monthly_food = daily_food * 30
    
    st.subheader("Monthly Unforeseen Expenses")
    monthly_unforeseen = st.number_input("Enter your monthly unforeseen expenses ($): ", min_value=0.0,format='%f' ) 
    
with colExpenses2:
    st.subheader("Monthly Transport")
    monthly_transport = st.number_input("Enter your monthly transport fee ($): ", min_value=0.0,format='%f' )   
    
    st.subheader("Monthly Utilities Fees")
    monthly_utilities = st.number_input("Enter your monthly utilities fees ($): ", min_value=0.0,format='%f' )
    
    st.subheader("Monthly Entertainment Budget")
    monthly_entertainment = st.number_input("Enter your monthly entertainment budget ($): ", min_value=0.0,format='%f' )   

monthly_expenses = monthly_rental + monthly_food + monthly_transport + monthly_entertainment + monthly_utilities + monthly_unforeseen
monthly_savings = monthly_takehome_salary - monthly_expenses 

st.header("**Savings**")
st.subheader("Monthly Take Home Salary: $" + str(round(monthly_takehome_salary,2)))
st.subheader("Monthly Expenses: $" + str(round(monthly_expenses, 2)))
st.subheader("Monthly Savings: $" + str(round(monthly_savings, 2)))

st.markdown("---")
