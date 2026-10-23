import streamlit as st
import pandas as pd
import time
from collections import Counter
import re

# Set up page configurations
st.set_page_config(page_title="Zero-Leak Forensic Engine", page_icon="🚨", layout="centered")

st.title("🚨 Zero-Leak Forensic Hub")
st.subheader("GovTech Interface: Text-Extraction Consensus Enabled")
st.markdown("---")

# Initialize persistent session states for simulating multiple witness entries
if "all_reports" not in st.session_state:
    st.session_state.all_reports = []

# Start tracking retrieval time the moment the page/module loads
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

st.header("Step 1: Live Citizen Reporting Interface")

# --- COMPREHENSIVE FORENSIC FORM ---
with st.form(key="comprehensive_forensic_form", clear_on_submit=True):
    st.error("#### 🛡️ Incident Details")
    crime_type = st.radio("Type of Crime Witnessed:", ["Armed Robbery", "Murder / Homicide", "Attempted Murder", "Assault", "Theft / Burglary", "Other"], horizontal=True)
    crime_other = st.text_input("If 'Other' or to add extra incident details, type here:", placeholder="e.g., Gun used, getaway route notes...")

    with st.expander("👤 1. Demographic & Basic Identifiers", expanded=True):
        age_range = st.radio("Estimated Age Range:", ["Teenager", "Twenties/Thirties", "Middle-Aged", "Elderly", "Unknown"], horizontal=True)
        bio_sex = st.radio("Biological Sex Presentation:", ["Male", "Female", "Non-Binary Presentation", "Unknown"], horizontal=True)
        race_ethnicity = st.radio("Perceived Race / Complexion:", ["Light/White", "Medium/Olive", "Dark/Black", "Asian", "Other"], horizontal=True)
        demographic_other = st.text_input("Additional identity details or 'Other' descriptors:", placeholder="e.g., Height markers, accent notes...")

    with st.expander("🧍 2. Physical Appearance & Build", expanded=False):
        build_type = st.radio("Physical Build:", ["Thin", "Athletic", "Average", "Heavy-Set", "Other"], horizontal=True)
        hair_details = st.radio("Dominant Hair Style/Color:", ["Short Dark", "Long Light", "Bald/Shaved", "Facial Hair (Beard/Mustache)", "Other"], horizontal=True)
        distinctive_marks = st.radio("Visible Distinctive Marks:", ["None", "Tattoos", "Scars/Birthmarks", "Piercings/Jewelry", "Other"], horizontal=True)
        physical_other = st.text_input("Additional appearance notes, distinct marks, or 'Other' traits:", placeholder="e.g., Scar on left cheek...")

    with st.expander("🧥 3. Clothing & Accessories", expanded=False):
        outerwear = st.radio("Outerwear & Tops:", ["Black Hoodie", "Blue Jacket", "Red Shirt/Sweater", "White T-Shirt", "Other"], horizontal=True)
        bottoms_footwear = st.radio("Bottoms & Footwear:", ["Dark Jeans", "Grey Sweatpants", "Shorts", "Sneakers/Boots", "Other"], horizontal=True)
        accessories = st.radio("Visible Accessories:", ["None", "Cap/Hat", "Glasses/Sunglasses", "Mask/Face Covering", "Other"], horizontal=True)
        clothing_other = st.text_input("Describe full outfit adjustments or specific 'Other' items seen:", placeholder="e.g., Wearing a purple shawl, black beret...")

    with st.expander("🚶 4. Behavior & Demeanor", expanded=False):
        speech_pattern = st.radio("Voice & Speech Indicators:", ["Local Accent", "Foreign Accent", "Aggressive/Shouting", "Muffled/Quiet", "Other"], horizontal=True)
        movement_gait = st.radio("Gait & Movement:", ["Normal/Running", "Noticeable Limp", "Pacing/Agitated", "Unique Posture", "Other"], horizontal=True)
        state_of_mind = st.radio("Apparent State of Mind:", ["Nervous/Panic", "Aggressive/Hostile", "Calm/Calculated", "Intoxicated", "Other"], horizontal=True)
        behavior_other = st.text_input("Additional behavioral quirks, words spoken, or 'Other' traits:", placeholder="e.g., French accent, heavy limp...")

    submit_button = st.form_submit_button(label="🔒 SECURE & TRANSMIT EVIDENCE")

# --- DATA INGESTION ENGINE ---
if submit_button:
    end_time = time.time()
    retrieval_speed = round(end_time - st.session_state.start_time, 2)
    
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
    st.success(f"Evidence Locked! Data transmitted securely in {retrieval_speed} seconds.")
    st.session_state.start_time = time.time()

# --- INVESTIGATOR DASHBOARD ---
st.markdown("---")
st.header("🕵️‍♂️ Real-Time Investigator Dashboard")

if len(st.session_state.all_reports) == 0:
    st.warning("Awaiting incoming citizen data streams.")
else:
    df = pd.DataFrame(st.session_state.all_reports)
    
    # Process through the Cognitive Filter (Drop inputs over 12 seconds)
    filtered_df = df[df["Retrieval Speed (s)"] <= 12.0]
    valid_entries = len(filtered_df)
    
    st.write("### 🧠 Predictive Consensus Analytics")
    if valid_entries > 0:
        col1, col2, col3 = st.columns(3)
        col1.metric(label="Primary Crime", value=str(filtered_df["Crime Type Selected"].mode()[0]))
        col2.metric(label="Suspect Sex Presenting", value=str(filtered_df["Sex"].mode()[0]))
        col3.metric(label="Data Integrity Base", value=f"{valid_entries} / {len(df)}")
        
        # --- NLP / KEYWORD EXTRACTION LOGIC ---
        st.write("### 🔍 Extracted Custom Clue Consensus")
        st.caption("The engine crawls open-text boxes, strips background noise, and displays matching tactical alerts.")
        
        # Combine all custom text strings into one large dataset pool
        text_fields = ["Custom Crime Details", "Custom Demographics", "Custom Physical Traits", "Custom Clothing Details", "Custom Behavior Details"]
        all_words = []
        stop_words = {"the", "a", "an", "and", "or", "but", "is", "was", "were", "with", "wearing", "in", "on", "at", "to", "he", "she", "they", "had", "seemed", "looked"}
        
        for field in text_fields:
            for text in filtered_df[field].dropna():
                words = re.findall(r'\b\w+\b', text.lower())
                all_words.extend([word for word in words if word not in stop_words])
        
        # Find recurring terms (appearing more than once)
        word_counts = Counter(all_words)
        common_clues = {word: count for word, count in word_counts.items() if count >= 2}
        
        if common_clues:
            for clue, count in common_clues.items():
                st.warning(f"🚨 **High-Frequency Narrative Match Detected:** '{clue.upper()}' mentioned by {count} separate rapid-response witnesses.")
        else:
            st.info("No matching high-frequency narrative phrases detected yet. Data arrays remain diverse.")
            
        st.write("#### Full Text Logging Review")
        st.dataframe(df[["Witness ID", "Custom Crime Details", "Custom Clothing Details", "Custom Behavior Details"]], use_container_width=True)
    else:
        st.error("No high-speed reports available for automatic cross-examination processing.")

if st.button("🔄 Reset System Database"):
    st.session_state.all_reports = []
    st.session_state.start_time = time.time()
    st.rerun()
