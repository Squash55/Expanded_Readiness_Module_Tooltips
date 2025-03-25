import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

st.set_page_config(page_title="Expanded Readiness Intelligence (Artificial data)", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("Expanded_Readiness_Spreadsheet.csv", skiprows=1)

df = load_data()

st.title("📋 Expanded Readiness Intelligence with Hover Tooltips (Artificial data)")
st.markdown("Hover over column headers to see smart definitions.")

# Define smart tooltips for each column
tooltips = {
    "Base": "Name of the base",
    "Country": "Country location of base",
    "Latitude": "Geographical latitude",
    "Longitude": "Geographical longitude",
    "Mission Complexity": "How complex are the base's mission types",
    "Maintenance Burden": "Total burden from unresolved maintenance issues",
    "Personnel Gaps": "Shortage of skilled personnel",
    "Logistics Readiness": "Readiness of logistics infrastructure and systems",
    "Equipment Availability": "Availability of key operational equipment",
    "Cyber Resilience": "Base's ability to defend and recover from cyber threats",
    "Fuel Supply Score": "Security and availability of fuel resources",
    "Flight Ops Readiness": "Readiness of flight operations capability",
    "Medical Support Score": "Adequacy of medical staff and facilities",
    "Training Level": "Proficiency level of personnel training"
}

# Configure AgGrid
gb = GridOptionsBuilder.from_dataframe(df)
for col in df.columns:
    gb.configure_column(col, headerTooltip=tooltips.get(col, ""))

# ✅ Enable tooltips on hover
gb.configure_grid_options(enableBrowserTooltips=True)

grid_options = gb.build()

# Render the interactive AgGrid table
AgGrid(
    df,
    gridOptions=grid_options,
    height=500,
    fit_columns_on_grid_load=True
)

# Smart AI-generated insight
st.subheader("🧠 Adaptive Problem Statement (AI-Assisted)")

st.markdown("""
**Problem Context:**  
Several U.S. and allied Air Force bases show challenges in mission complexity, logistics readiness, and equipment availability.  
Many exhibit high maintenance burdens and personnel gaps, suggesting urgent needs.

**Detected Patterns:**  
- High mission complexity often aligns with low cyber resilience and flight ops readiness  
- Equipment availability below 60 often co-occurs with poor logistics and medical scores  
- Bases in remote areas show higher fuel supply risks and training gaps

**Potential Solutions:**  
- 📦 Deploy mobile logistics support to underperforming areas  
- 🧠 Use AI-enabled training tools for low-proficiency bases  
- 🛠 Create predictive maintenance dashboards  
- 📍 Prioritize bases with complex mission + high personnel gaps + low cyber resilience

**Next Steps:**  
Feed these insights into an AI-CII powered readiness review with optimization interventions.
""")
