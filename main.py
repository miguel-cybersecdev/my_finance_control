import streamlit as st
from database import create_tables
from services import insert_launch, launch_list, balance_calc

create_tables()

st.title(" Finance Control ")

st.subheader(" New Launch ")
type = st.selectbox("Type", ["Revenue", "Expense"])
value = st.number_input("Value", min_value=0.0, step=0.01)
category = st.text_input("Category")
date = st.date_input("Date")
description = st.text_input("Description")

if st.button("Save"):
    insert_launch(type, value, category, str(date), description)
    st.success("Launch successfully registered!")

st.subheader(" Financial Summary ")
balance = balance_calc()
st.metric("Current balance", f"R$ {balance}")

st.subheader("Launchs")
df = launch_list()
st.dataframe(df)