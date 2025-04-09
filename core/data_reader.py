import pandas as pd
import streamlit as st

@st.cache_data(ttl=300)
def load_sheet_data(_conn):
    df = _conn.read(worksheet="DATA", ttl=5)
    df = df.dropna(how="all")
    df = df.query("~DEPARMENT.isnull()")
    df = df[~df['ITEM DETAILS'].str.contains(r"- FOR \*", na=False)]
    df = df.query("~`ITEM DETAILS`.isnull()")
    df = pd.DataFrame(df, columns=['DEPARMENT', 'ITEM DETAILS', 'ITEM CODE', 'CURRENT STOCK'])
    df = df.rename(columns={
        "CURRENT STOCK": "CURRENT STOCK IN GA STORE",
        "DEPARMENT": "DEPARTMENT"
    })
    return df

def load_sheet_record(_conn):
    df = _conn.read(worksheet="STOCK RECORDS", ttl=5)
    df = df.dropna(how="all")
    return df
