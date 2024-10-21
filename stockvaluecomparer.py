import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import matplotlib.pyplot as plt
import time

def main():

    # Set page to always wide
    st.set_page_config(layout="wide")

    st.title("Stock Value Comparer")

    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(worksheet="DATA", ttl=5)
    df = df.dropna(how="all")
    df = df.query("~DEPARMENT.isnull()")
    df = df[~df['ITEM DETAILS'].str.contains(r"- FOR \*", na=False)]
    df = df.query("~`ITEM DETAILS`.isnull()")
    columns = ['DEPARMENT', 'ITEM DETAILS', 'ITEM CODE', 'CURRENT STOCK']
    df = pd.DataFrame(df, columns=columns)
    df = df.rename(columns={"CURRENT STOCK": "CURRENT STOCK IN GA STORE"})
    df = df.rename(columns={"DEPARMENT": "DEPARTMENT"})

    # File upload section
    uploaded_file = st.sidebar.file_uploader("Please upload file", type=["csv", "xlsx"])
    if uploaded_file is not None:
        if uploaded_file.name.endswith('.csv'):
            df_uploaded = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df_uploaded = pd.read_excel(uploaded_file)

        df_uploaded = pd.DataFrame(df_uploaded, columns=['Item Code', 'UOM', 'Item Group', 'Item Type', 'Description', 'Qty'])
        df_uploaded = df_uploaded.rename(columns={"Qty": "CURRENT STOCK IN AUTOCOUNT"})
        df_uploaded = df_uploaded.rename(columns={"Item Code": "ITEM CODE"})
        df_uploaded = df_uploaded.iloc[:-1]

        # Merge and compute differences
        df_merged = pd.merge(df_uploaded, df[['ITEM CODE', 'DEPARTMENT', 'CURRENT STOCK IN GA STORE']], on='ITEM CODE', how='left')
        df_merged['DIFF'] = df_merged['CURRENT STOCK IN AUTOCOUNT'] - df_merged['CURRENT STOCK IN GA STORE']

        # Add a new column 'DIFF LABEL' for filtering
        df_merged['DIFF LABEL'] = df_merged['DIFF'].apply(lambda x: 'Balance' if x == 0 else ('Unbalance (+)' if x > 0 else 'Unbalance (-)'))

        # Apply dynamic filtering
        selected_departments = st.sidebar.multiselect('Filter by DEPARTMENT', df_merged['DEPARTMENT'].dropna().unique())
        if selected_departments:
            df_merged = df_merged[df_merged['DEPARTMENT'].isin(selected_departments)]

        # After department filter, dynamically limit other filters
        selected_item_codes = st.sidebar.multiselect('Filter by ITEM CODE', df_merged['ITEM CODE'].dropna().unique())
        if selected_item_codes:
            df_merged = df_merged[df_merged['ITEM CODE'].isin(selected_item_codes)]

        selected_item_groups = st.sidebar.multiselect('Filter by ITEM GROUP', df_merged['Item Group'].dropna().unique())
        if selected_item_groups:
            df_merged = df_merged[df_merged['Item Group'].isin(selected_item_groups)]

        selected_descriptions = st.sidebar.multiselect('Filter by DESCRIPTION', df_merged['Description'].dropna().unique())
        if selected_descriptions:
            df_merged = df_merged[df_merged['Description'].isin(selected_descriptions)]

        # Finally apply DIFF filter
        selected_diff_label = st.sidebar.multiselect('Filter by DIFF', ['Balance', 'Unbalance (+)', 'Unbalance (-)'])
        if selected_diff_label:
            df_merged = df_merged[df_merged['DIFF LABEL'].isin(selected_diff_label)]

        # Metrics display
        total_items, total_items_not_exist, total_balance_items, total_over_items, total_negative_items = st.columns(5)

        with total_items:
            st.metric(label="Total Items", value=len(df_merged))

        with total_items_not_exist:
            st.metric(label="Total Items not Exist", value=df_merged["CURRENT STOCK IN GA STORE"].isnull().sum())

        with total_balance_items:
            st.metric(label="Total Items are Balance", value=len(df_merged.query('DIFF == 0')))

        with total_over_items:
            st.metric(label="Total Items Over (-diff)", value=len(df_merged.query('DIFF < 0')))

        with total_negative_items:
            st.metric(label="Total Items Below (+diff)", value=len(df_merged.query('DIFF > 0')))

        # Display filtered data
        st.dataframe(df_merged)
    else:
        st.warning("Please upload file", icon="⚠")

if __name__ == "__main__":
    main()
