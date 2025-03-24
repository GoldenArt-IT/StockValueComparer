import streamlit as st

def apply_filters(df):
    dept = st.sidebar.multiselect('Filter by DEPARTMENT', df['DEPARTMENT'].dropna().unique())
    if dept:
        df = df[df['DEPARTMENT'].isin(dept)]

    code = st.sidebar.multiselect('Filter by ITEM CODE', df['ITEM CODE'].dropna().unique())
    if code:
        df = df[df['ITEM CODE'].isin(code)]

    group = st.sidebar.multiselect('Filter by ITEM GROUP', df['Item Group'].dropna().unique())
    if group:
        df = df[df['Item Group'].isin(group)]

    desc = st.sidebar.multiselect('Filter by DESCRIPTION', df['Description'].dropna().unique())
    if desc:
        df = df[df['Description'].isin(desc)]

    diff = st.sidebar.multiselect('Filter by DIFF', ['Balance', 'Unbalance (+)', 'Unbalance (-)'])
    if diff:
        df = df[df['DIFF LABEL'].isin(diff)]

    return df
