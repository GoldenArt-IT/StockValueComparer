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
        st.dataframe(df)

if __name__ == "__main__":
    main()

