# 📊 Stock Value Comparer

A **Streamlit** app to compare stock value data from **AutoCount** uploads against existing **Google Sheets** records.

[👉 **Access the Live App Here**](https://stockvaluecomparer-gait.streamlit.app/)

---

## 📑 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Example Workflow](#example-workflow)
- [Project Structure](#project-structure)
- [Reference](#reference)

---

## ✨ Features

- **Google Sheets Integration**
  - Reads reference and record data.
- **File Upload**
  - Supports `.csv` and `.xlsx` files from AutoCount.
- **Data Merging**
  - Merges uploaded data with existing sheets and labels them.
- **Filtering**
  - Interactive filtering of merged data.
- **Metrics & Records**
  - Displays summaries, duplication metrics, and recent records.
- **Performance Timing**
  - Shows sheet load time for monitoring.

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-org/stock-value-comparer.git

   cd stock-value-comparer
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Create** `.streamlit/secrets.toml`

   ```toml
   [gsheets]
   credentials = "<YOUR GOOGLE SERVICE ACCOUNT JSON>"
   spreadsheet = "<YOUR GOOGLE SHEET URL>"
   ```

4. **Run the app**

   ```bash
   streamlit run app.py
   ```

---

## ⚙️ Configuration

* **Google Sheets Connection**

  * Your service account must have Editor access to the target spreadsheet.
  * Spreadsheet should contain:

    * Reference data sheet
    * Records sheet

---

## 🛠️ Usage

1. **Open the App**

   * The app will connect to Google Sheets and show the latest timestamp.
2. **Upload File**

   * Use sidebar to upload `.csv` or `.xlsx` AutoCount file.
3. **Processing**

   * File will be merged and labeled against sheet data.
4. **Filtering**

   * Use available filters to narrow results.
5. **Metrics**

   * View metrics for total items, value discrepancies, and duplications.
6. **Records**

   * See historical records from Google Sheets.

---

## 💡 Example Workflow

**Scenario:**

* You received an AutoCount export file (`stock_data.xlsx`).
* You want to validate it against the master record.

**Steps:**

1. Open the app.
2. Check the timestamp of the latest GA Store entry.
3. Upload your file.
4. Review merged data.
5. Filter to view discrepancies.
6. Check duplication metrics.
7. Confirm records.

**Daily Habit Example:**

* Each time you get new stock data:

  * Upload it immediately.
  * Review and save the metrics.
  * Keep your Google Sheets updated.

---

## 📂 Project Structure

```bash
stock-value-comparer/
├── app.py                  # Main Streamlit app script
├── core/
│   ├── data_reader.py      # Functions to load sheet data and records
│   ├── file_processor.py   # File upload and merge logic
│   ├── filters.py          # Filtering utilities
│   ├── metrics.py          # Metrics calculation and display
│   └── tables.py           # Table rendering functions
├── requirements.txt        # Dependency list
└── README.md               # This README file
```

---

## 📚 Reference

* [Streamlit Documentation](https://docs.streamlit.io)
* [streamlit\_gsheets](https://github.com/streamlit/streamlit-gsheets)
* [Google Sheets API](https://developers.google.com/sheets/api)
* [👉 Access the Stock Value Comparer App](https://stockvaluecomparer-gait.streamlit.app/)
