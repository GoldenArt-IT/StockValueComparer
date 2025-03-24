import streamlit as st

def show_tables(df):
    st.subheader("Comparison Table")
    st.dataframe(df)

    st.subheader("Balance Summary by Department")
    pivot = df.pivot_table(index='DEPARTMENT', columns='DIFF LABEL', values='DIFF', aggfunc='count', fill_value=0)
    st.dataframe(pivot)

    st.subheader("Duplicate Items")
    st.dataframe(df[df.duplicated(subset='ITEM CODE', keep=False)])
