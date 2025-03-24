import pandas as pd
import streamlit as st

@st.cache_data
def process_uploaded_file(uploaded_file):
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
    df = pd.DataFrame(df, columns=['Item Code', 'UOM', 'Item Group', 'Item Type', 'Description', 'Qty'])
    df = df.rename(columns={"Qty": "CURRENT STOCK IN AUTOCOUNT", "Item Code": "ITEM CODE"})
    return df.iloc[:-1]

def merge_and_label(df_uploaded, df_sheet):
    df_merged = pd.merge(
        df_uploaded, 
        df_sheet[['ITEM DETAILS', 'ITEM CODE', 'DEPARTMENT', 'CURRENT STOCK IN GA STORE']], 
        on='ITEM CODE', 
        how='left'
    )
    df_merged['DIFF'] = df_merged['CURRENT STOCK IN AUTOCOUNT'] - df_merged['CURRENT STOCK IN GA STORE']
    df_merged['DIFF LABEL'] = df_merged['DIFF'].apply(
        lambda x: 'Balance' if abs(x) < 1e-9 else ('Unbalance (+)' if x > 0 else 'Unbalance (-)')
    )
    return df_merged
