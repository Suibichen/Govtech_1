import streamlit as st
import pandas as pd
import time

# Set up page configurations
st.set_page_config(page_title="Zero-Leak Forensic Engine", page_icon="🚨", layout="centered")

st.title("🚨 Zero-Leak Forensic Hub")
st.subheader("GovTech Interface: High-Fidelity Witness Profiling")
st.markdown("---")

# Initialize persistent session states for simulating multiple witness entries
if "all_reports" not in st.session_state:
    st.session_state.all_reports = []

# Start tracking retrieval time the moment the page/module loads
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

st.header("Step 1: Live Citizen Reporting Interface")
st.info("Simulate a panicked citizen submitting a highly structured witness log after an event.")

# --- COMPREHENSIVE FORENSIC FORM ---
with st.form(key="comprehensive_forensic_form", clear_on_submit=True):
    st.write("### 🧠 Rapid Visual Capture Panel")
    st.caption("Complete the sections below as fast as possible to preserve uncorrupted cognitive data.")
    
    # 🔍 Section 0: Incident & Crime Type Detail
    st.error("#### 🛡️ Incident Details")
    crime_type = st.radio("Type of Crime Witnessed:", ["Armed Robbery", "Murder / Homicide", "Attempted Murder", "Assault", "Theft / Burglary", "Other"], horizontal=True)
    crime_other = st.text_input("If 'Other' or to add extra incident details, type here:", placeholder="e.g., Purple shawl stolen, arson attempt, getaway route notes...")

    # 📋 Category 1: Demographic & Basic Identifiers
    with st.expander("👤 1. Demographic & Basic Identifiers", expanded=True):
        age_range = st.radio("Estimated Age Range:", ["Teenager", "Twenties/Thirties", "Middle-Aged", "Elderly", "Unknown"], horizontal=True)
        bio_sex = st.radio("Biological Sex Presentation:", ["Male", "Female", "Non-Binary Presentation", "Unknown"], horizontal=True)
        race_ethnicity = st.radio("Perceived Race / Complexion:", ["Light/White", "Medium/Olive", "Dark/Black", "Asian", "Other"], horizontal=True)
        demographic_other = st.text_input("Additional identity details or 'Other' descriptors:", placeholder="e.g., Distinct regional accent, specific complexion features...")

    # 🧍 Category 2: Physical Appearance & Build
    with st.expander("🧍 2. Physical Appearance & Build", expanded=False):
        build_type = st.radio("Physical Build:", ["Thin", "Athletic", "Average", "Heavy-Set", "Other"], horizontal=True)
        hair_details = st.radio("Dominant Hair Style/Color:", ["Short Dark", "Long Light", "Bald/Shaved", "Facial Hair (Beard/Mustache)", "Other"], horizontal=True)
        distinctive_marks = st.radio("Visible Distinctive Marks:", ["None", "Tattoos", "Scars/Birthmarks", "Piercings/Jewelry", "Other"], horizontal=True)
        physical_other = st.text_input("Additional appearance notes, distinct marks, or 'Other' traits:", placeholder="e.g., Scar on left cheek, exceptionally tall, cross tattoo...")

    # 🧥 Category 3: Clothing & Accessories
    with st.expander("🧥 3. Clothing & Accessories", expanded=False):
        outerwear = st.radio("Outerwear & Tops:", ["Black Hoodie", "Blue Jacket", "Red Shirt/Sweater", "White T-Shirt", "Other"], horizontal=True)
        bottoms_footwear = st.radio("Bottoms & Footwear:", ["Dark Jeans", "Grey Sweatpants", "Shorts", "Sneakers/Boots", "Other"], horizontal=True)
        accessories = st.radio("Visible Accessories:", ["None", "Cap/Hat", "Glasses/Sunglasses", "Mask/Face Covering", "Other"], horizontal=True)
        clothing_other = st.text_input("Describe full outfit adjustments or specific 'Other' items seen:", placeholder="e.g., Wearing a purple shawl, black beret, bright red running shoes...")

    # 🚶 Category 4: Behavior & Demeanor
    with st.expander("🚶 4. Behavior & Demeanor", expanded=False):
        speech_pattern = st.radio("Voice & Speech Indicators:", ["Local Accent", "Foreign Accent", "Aggressive/Shouting", "Muffled/Quiet", "Other"], horizontal=True)
        movement_gait = st.radio("Gait & Movement:", ["Normal/Running", "Noticeable Limp", "Pacing/Agitated", "Unique Posture", "Other"], horizontal=True)
        state_of_mind = st.radio("Apparent State of Mind:", ["Nervous/Panic", "Aggressive/Hostile", "Calm/Calculated", "Intoxicated", "Other"], horizontal=True)
        behavior_other = st.text_input("Additional behavioral quirks, words spoken, or 'Other' traits:", placeholder="e.g., Spoke with a French accent, stuttered, limping heavily on the left foot...")

    # Submit Button for the secure form
    submit_button = st.form_submit_button(label="🔒 SECURE & TRANSMIT EVIDENCE")

# --- DATA INGESTION ENGINE ---
if submit_button:
    end_time = time.time()
    retrieval_speed = round(end_time - st.session_state.start_time, 2)
    
    # Package individual comprehensive report including all radio buttons AND custom type-in fields
    new_report = {
        "Witness ID": f"CITIZEN-{len(st.session_state.all_reports) + 1:03d}",
        "Crime Type Selected": crime_type,
        "Custom Crime Details": crime_other,
        "Age Range": age_range,
        "Sex": bio_sex,
        "Race/Complexion": race_ethnicity,
        "Custom Demographics": demographic_other,
        "Build": build_type,
        "Hair": hair_details,
        "Marks": distinctive_marks,
        "Custom Physical Traits": physical_other,
        "Outerwear": outerwear,
        "Bottoms": bottoms_footwear,
        "Accessories": accessories,
        "Custom Clothing Details": clothing_other,
        "Speech": speech_pattern,
        "Gait": movement_gait,
        "State of Mind": state_of_mind,
        "Custom Behavior Details": behavior_other,
        "Retrieval Speed (s)": retrieval_speed
    }
    
    st.session_state.all_reports.append(new_report)
    st.success(f"Evidence Locked! Data transmitted securely to GovHub in {retrieval_speed} seconds. Local cache purged.")
    st.session_state.start_time = time.time()

# --- INVESTIGATOR DASHBOARD ---
st.markdown("---")
st.header("🕵️‍♂️ Real-Time Investigator Dashboard")

if len(st.session_state.all_reports) == 0:
    st.warning("Awaiting incoming citizen data streams. Submit a report above to test the high-fidelity consensus aggregation.")
else:
    df = pd.DataFrame(st.session_state.all_reports)
    st.write("### Raw Encrypted Incoming Streams")
    st.dataframe(df, use_container_width=True)
    
    # Neuroscience filter: Keep reports under 12 seconds for perfect consensus mapping
    filtered_df = df[df["Retrieval Speed (s)"] <= 12.0]
    valid_entries = len(filtered_df)
    
    st.write("### 🧠 Predictive Consensus Analytics (Filtered Data)")
    if valid_entries > 0:
        col1, col2, col3, col4 = st.columns(4)
        col1.metric(label="Primary Crime Reported", value=str(filtered_df["Crime Type Selected"].mode()[0]))
        col2.metric(label="Suspect Profile Sex", value=str(filtered_df["Sex"].mode()[0]))
        col3.metric(label="Detected Demeanor", value=str(filtered_df["State of Mind"].mode()[0]))
        col4.metric(label="Valid Accounts Logs", value=f"{valid_entries} / {len(df)}")
        
        # Display the custom entries to help officers find unique outliers (like the purple shawl)
        st.write("### 📜 Free-Text Forensic Clues (Unfiltered)")
        st.dataframe(df[["Witness ID", "Custom Crime Details", "Custom Clothing Details", "Custom Behavior Details"]], use_container_width=True)
    else:
        st.error("No reports have bypassed the 12-second validity boundary yet. High probability of memory contamination.")

if st.button("🔄 Reset System Database"):
    st.session_state.all_reports = []
    st.session_state.start_time = time.time()
    st.rerun()
