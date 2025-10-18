import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(page_title="🚀 SpaceX Falcon 9 Dashboard", layout="wide")

# -----------------------------
# Custom Styling (Bootstrap feel)
# -----------------------------
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    h1 {
        color: #007bff;
        text-align: center;
    }
    .stSlider > div[data-baseweb="slider"] {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 10px;
    }
    .footer {
        text-align: center;
        color: gray;
        font-size: 0.9em;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv("data/processed/launches_clean.csv")
df["year"] = pd.to_datetime(df["date_utc"]).dt.year

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("🔧 Filters")

sites = df["launch_site"].dropna().unique()
selected_sites = st.sidebar.multiselect("Select Launch Sites:", options=sites, default=None)

payload_min = int(df["payload_mass_kg"].min())
payload_max = int(df["payload_mass_kg"].max())
payload_range = st.sidebar.slider(
    "Payload Mass Range (kg):",
    min_value=payload_min,
    max_value=payload_max,
    value=(payload_min, payload_max),
    step=100
)

# -----------------------------
# Filter Data
# -----------------------------
filtered_df = df.copy()

if selected_sites:
    filtered_df = filtered_df[filtered_df["launch_site"].isin(selected_sites)]

filtered_df = filtered_df[
    (filtered_df["payload_mass_kg"] >= payload_range[0]) &
    (filtered_df["payload_mass_kg"] <= payload_range[1])
]

# -----------------------------
# Dashboard Title
# -----------------------------
st.markdown("<h1>🚀 SpaceX Falcon 9 Dashboard</h1>", unsafe_allow_html=True)
st.markdown("---")

# -----------------------------
# Create Visualizations
# -----------------------------

# 1️⃣ Payload Histogram
fig1 = px.histogram(
    filtered_df,
    x="payload_mass_kg",
    color=filtered_df["landing_success"].map({1: "Success", 0: "Failure"}),
    nbins=40,
    title="Payload Mass vs Landing Outcome",
    color_discrete_map={"Success": "green", "Failure": "red"},
    template="plotly_white"
)
fig1.update_layout(bargap=0.2)

# 2️⃣ Yearly Success Rate
yearly = filtered_df.groupby("year")["landing_success"].mean().mul(100).reset_index()
fig2 = px.line(
    yearly,
    x="year",
    y="landing_success",
    markers=True,
    title="Success Rate (%) by Year",
    template="plotly_white"
)
fig2.update_traces(line=dict(color='royalblue', width=3))
fig2.update_yaxes(range=[0, 100], title="Success Rate (%)")
fig2.update_xaxes(dtick=1)

# 3️⃣ Launch Site Map
site_counts = filtered_df.groupby("launch_site")["landing_success"].mean().reset_index()
site_counts["lat"] = site_counts["launch_site"].map({
    "CCAFS LC-40": 28.5618571,
    "KSC LC-39A": 28.6080585,
    "VAFB SLC-4E": 34.632093,
})
site_counts["lon"] = site_counts["launch_site"].map({
    "CCAFS LC-40": -80.577366,
    "KSC LC-39A": -80.604166,
    "VAFB SLC-4E": -120.610829,
})
fig3 = px.scatter_mapbox(
    site_counts,
    lat="lat",
    lon="lon",
    size="landing_success",
    hover_name="launch_site",
    zoom=3,
    height=500,
    title="Launch Site Success Rate",
    color="landing_success",
    color_continuous_scale="Viridis"
)
fig3.update_layout(mapbox_style="open-street-map")
fig3.update_traces(marker=dict(sizemode='area', sizeref=0.2))

# -----------------------------
# Display Layout
# -----------------------------
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig1, use_container_width=True)
with col2:
    st.plotly_chart(fig2, use_container_width=True)

st.plotly_chart(fig3, use_container_width=True)

# -----------------------------
# Footer
# -----------------------------
st.markdown(f"""
    <div class='footer'>
    Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    </div>
""", unsafe_allow_html=True)
