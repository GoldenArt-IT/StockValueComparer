import streamlit as st
from streamlit_gsheets import GSheetsConnection
from core.data_reader import load_sheet_data, load_sheet_record
from core.file_processor import process_uploaded_file, merge_and_label
from core.filters import apply_filters
from core.metrics import show_metrics, show_metric_for_duplicated_data
from core.tables import show_tables, show_records
import time

def main():
    st.set_page_config(layout="wide")
    st.title("Stock Value Comparer")

    start = time.time()
    conn = st.connection("gsheets", type=GSheetsConnection)
    df_sheet = load_sheet_data(conn)
    df_record = load_sheet_record(conn)
    st.write(f"⏱ Load Sheet Time: {time.time() - start:.2f}s")
    st.write(f"🆕Latest data key in GA Store: {df_record.tail(1)['TIMESTAMP'].values}")

    uploaded_file = st.sidebar.file_uploader("Please upload file", type=["csv", "xlsx"])
    if uploaded_file:
        df_uploaded = process_uploaded_file(uploaded_file)
        df_merged = merge_and_label(df_uploaded, df_sheet)
        df_merged = apply_filters(df_merged)

        show_metrics(df_merged)
        show_tables(df_merged)
        show_metric_for_duplicated_data(df_record)
        show_records(df_record)
    else:
        st.warning("Please upload Autocount file", icon="⚠")
        show_metric_for_duplicated_data(df_record)
        show_records(df_record)

if __name__ == "__main__":
    main()
