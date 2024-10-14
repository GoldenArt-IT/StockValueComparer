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

        st.dataframe(df)

        uploaded_file = st.sidebar.file_uploader("Choose a file (A/R Receivable ONLY)", type=["csv", "xlsx"])
        if uploaded_file is not None:
            if uploaded_file.name.endswith('.csv'):
                df_uploaded = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith('.xlsx'):
                df_uploaded = pd.read_excel(uploaded_file)
            

            
            st.dataframe(df_uploaded)
        else:
              st.warning("please upload file")

if __name__ == "__main__":
    main()

