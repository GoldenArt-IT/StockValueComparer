import streamlit as st

def show_tables(df):
    st.subheader("Comparison Table")
    st.dataframe(df)

    st.subheader("Balance Summary by Department")
    pivot = df.pivot_table(index='DEPARTMENT', columns='DIFF LABEL', values='DIFF', aggfunc='count', fill_value=0)
    st.dataframe(pivot)

    st.subheader("Duplicate Items")
    st.dataframe(df[df.duplicated(subset='ITEM CODE', keep=False)])

def show_records(df):
    st.subheader("Duplicate Records in GA Store")
    df = df[df.duplicated(subset='TIMESTAMP', keep=False)]
    df = df.sort_values(by='TIMESTAMP')
    st.dataframe(df)