import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import matplotlib.pyplot as plt
import time

def main():

        # Set page to always wide
        st.set_page_config(layout="wide")

        st.title("Data BOM for Wood Material")

        conn = st.connection("gsheets", type=GSheetsConnection)
        df = conn.read(worksheet="ORDER BY WOOD", ttl=5)
        df = df.dropna(how="all")

if __name__ == "__main__":
    main()

