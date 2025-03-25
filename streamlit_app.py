
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

# Column tooltips
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

# ✅ Enable hover tooltips
gb.configure_grid_options(enableBrowserTooltips=True)

grid_options = gb.build()

AgGrid(df, gridOptions=grid_options, height=500, fit_columns_on_grid_load=True)

# Smart AI-powered problem framing
st.subheader("🧠 Adaptive Problem Statement (AI-Assisted)")

st.markdown("""
**Problem Context:**  
Several U.S. and allied Air Force bases show a range of challenges in mission complexity, logistics readiness, and equipment availability.  
Notably, multiple bases present high maintenance burdens and personnel gaps, signaling a need for targeted interventions.

**Detected Issues:**  
- High mission complexity often aligns with low cyber resilience and flight ops readiness  
- Equipment availability below 60 correlates with poor logistics readiness and medical scores  
- Bases in remote areas tend to have higher fuel supply issues and training gaps

**Impact:**  
These patterns reduce operational flexibility and threaten mission success in time-sensitive scenarios. Delayed logistics or medical support can severely degrade deployment readiness.

**Potential Solutions:**  
- 📦 Deploy mobile logistics teams to bases with low logistics and fuel scores  
- 🧑‍🏫 Launch remote or AI-enabled training modules for undertrained personnel  
- 🛠️ Create a predictive maintenance model to address high maintenance burden bases  
- 🧬 Use AI to identify bases with latent risk combinations (e.g., high complexity + low cyber + high personnel gaps)  
- 🛰️ Improve data-driven prioritization of resource allocation across regions

**Next Steps:**  
This dashboard should feed into a command-level readiness review and support continuous improvement initiatives using AI-CII principles.
""")

st.markdown("---")
st.markdown("Powered by simulated readiness analytics and adaptive AI framing.")
