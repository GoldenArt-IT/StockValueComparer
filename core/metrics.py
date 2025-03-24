import streamlit as st

def show_metrics(df):
    total_items, not_exist, balance, over, under = st.columns(5)

    with total_items:
        st.metric("Total Items", len(df))
    with not_exist:
        st.metric("Total Items not Exist", df["CURRENT STOCK IN GA STORE"].isnull().sum())
    with balance:
        st.metric("Total Balance Items", len(df.query('`DIFF LABEL` == "Balance"')))
    with over:
        st.metric("Total Over (-diff)", len(df.query('`DIFF LABEL` == "Unbalance (-)"')))
    with under:
        st.metric("Total Below (+diff)", len(df.query('`DIFF LABEL` == "Unbalance (+)"')))
