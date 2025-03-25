
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

st.set_page_config(page_title="AgGrid Tooltip Test", layout="wide")

df = pd.DataFrame({
    "Base": ["Alpha", "Bravo", "Charlie"],
    "Readiness": [88, 73, 65],
    "Cyber Resilience": [75, 60, 50]
})

tooltips = {
    "Base": "Name of the Air Force base",
    "Readiness": "Overall mission readiness score",
    "Cyber Resilience": "Ability to withstand and recover from cyber attacks"
}

gb = GridOptionsBuilder.from_dataframe(df)
for col in df.columns:
    gb.configure_column(col, headerTooltip=tooltips.get(col, ""))

# ✅ Required to make tooltips work
gb.configure_grid_options(enableBrowserTooltips=True)

grid_options = gb.build()

st.title("🔍 Minimal AgGrid Tooltip Test")
st.markdown("Hover over column headers to see definitions.")

AgGrid(df, gridOptions=grid_options, height=200, fit_columns_on_grid_load=True)
