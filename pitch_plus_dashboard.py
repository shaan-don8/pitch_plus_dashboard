
import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("pitch_plus_dashboard.csv")

# Clean and rename columns
df = df.rename(columns={
    "player_name": "Pitcher",
    "pitch_type_recovered": "Pitch_Type",
    "avg_stuff_plus": "Stuff+",
    "avg_location_plus": "Location+",
    "avg_pitch_plus": "Pitch+",
    "pitch_count": "Pitch_Count"
})

# Filter out low pitch count if needed (e.g., min 30)
min_pitch_count = 30
df_filtered = df[df["Pitch_Count"] >= min_pitch_count]

# Sort for overall top 25
top_25_df = df_filtered.sort_values(by="Pitch+", ascending=False).head(25)

# App title
st.title("Pitch+ Dashboard")

# Tabs
tab1, *pitch_type_tabs = st.tabs(["Top 25 Overall"] + sorted(df_filtered["Pitch_Type"].unique()))

# Top 25 tab
with tab1:
    st.subheader("Top 25 Overall Pitches by Pitch+")
    st.dataframe(top_25_df[["Pitcher", "Pitch_Type", "Pitch+", "Stuff+", "Location+", "Pitch_Count"]]
                 .sort_values(by="Pitch+", ascending=False), use_container_width=True)

# Individual pitch type tabs
for pitch_tab, pitch_type in zip(pitch_type_tabs, sorted(df_filtered["Pitch_Type"].unique())):
    with pitch_tab:
        st.subheader(f"{pitch_type} Pitches")
        type_df = df_filtered[df_filtered["Pitch_Type"] == pitch_type]
        st.dataframe(type_df[["Pitcher", "Pitch+", "Stuff+", "Location+", "Pitch_Count"]]
                     .sort_values(by="Pitch+", ascending=False), use_container_width=True)
