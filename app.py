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
    
    # 📋 Category 1: Demographic & Basic Identifiers
    with st.expander("👤 1. Demographic & Basic Identifiers", expanded=True):
        age_range = st.radio("Estimated Age Range:", ["Teenager", "Twenties/Thirties", "Middle-Aged", "Elderly", "Unknown"], horizontal=True)
        bio_sex = st.radio("Biological Sex Presentation:", ["Male", "Female", "Non-Binary Presentation", "Unknown"], horizontal=True)
        race_ethnicity = st.radio("Perceived Race / Complexion:", ["Light/White", "Medium/Olive", "Dark/Black", "Asian", "Other"], horizontal=True)
        
        # Dynamic text input if "Other" is selected
        race_other = ""
        if race_ethnicity == "Other":
            race_other = st.text_input("Specify Complexion/Ethnicity Details:", placeholder="e.g., Tanned, specific regional background...")

    # 🧍 Category 2: Physical Appearance & Build
    with st.expander("🧍 2. Physical Appearance & Build", expanded=False):
        build_type = st.radio("Physical Build:", ["Thin", "Athletic", "Average", "Heavy-Set", "Other"], horizontal=True)
        build_other = st.text_input("Specify Build/Height Details:", placeholder="e.g., Exceptionally tall, muscular...") if build_type == "Other" else ""
        
        hair_details = st.radio("Dominant Hair Style/Color:", ["Short Dark", "Long Light", "Bald/Shaved", "Facial Hair (Beard/Mustache)", "Other"], horizontal=True)
        hair_other = st.text_input("Specify Hair/Facial Features:", placeholder="e.g., Blue hair, clean-shaven but scarred...") if hair_details == "Other" else ""
        
        distinctive_marks = st.radio("Visible Distinctive Marks:", ["None", "Tattoos", "Scars/Birthmarks", "Piercings/Jewelry", "Other"], horizontal=True)
        marks_other = st.text_input("Describe Distinctive Marks:", placeholder="e.g., Dragon tattoo on neck, lip piercing...") if distinctive_marks == "Other" else ""

    # 🧥 Category 3: Clothing & Accessories
    with st.expander("🧥 3. Clothing & Accessories", expanded=False):
        outerwear = st.radio("Outerwear & Tops:", ["Black Hoodie", "Blue Jacket", "Red Shirt/Sweater", "White T-Shirt", "Other"], horizontal=True)
        outerwear_other = st.text_input("Specify Top/Jacket Details:", placeholder="e.g., High-vis yellow vest with logo...") if outerwear == "Other" else ""
        
        bottoms_footwear = st.radio("Bottoms & Footwear:", ["Dark Jeans", "Grey Sweatpants", "Shorts", "Sneakers/Boots", "Other"], horizontal=True)
        bottoms_other = st.text_input("Specify Bottoms/Shoes Details:", placeholder="e.g., Bright red running shoes...") if bottoms_footwear == "Other" else ""
        
        accessories = st.radio("Visible Accessories:", ["None", "Cap/Hat", "Glasses/Sunglasses", "Mask/Face Covering", "Other"], horizontal=True)
        accessories_other = st.text_input("Specify Accessories:", placeholder="e.g., Large black tactical backpack...") if accessories == "Other" else ""

    # 🚶 Category 4: Behavior & Demeanor
    with st.expander("🚶 4. Behavior & Demeanor", expanded=False):
        speech_pattern = st.radio("Voice & Speech Indicators:", ["Local Accent", "Foreign Accent", "Aggressive/Shouting", "Muffled/Quiet", "Other"], horizontal=True)
        speech_other = st.text_input("Specify Speech/Words Used:", placeholder="e.g., Stutter, repeated specific phrases...") if speech_pattern == "Other" else ""
        
        movement_gait = st.radio("Gait & Movement:", ["Normal/Running", "Noticeable Limp", "Pacing/Agitated", "Unique Posture", "Other"], horizontal=True)
        gait_other = st.text_input("Specify Movement Details:", placeholder="e.g., Limping heavily on the left leg...") if movement_gait == "Other" else ""
        
        state_of_mind = st.radio("Apparent State of Mind:", ["Nervous/Panic", "Aggressive/Hostile", "Calm/Calculated", "Intoxicated", "Other"], horizontal=True)
        state_other = st.text_input("Specify State of Mind Notes:", placeholder="e.g., Seemed completely cold and detached...") if state_of_mind == "Other" else ""

    # Submit Button for the secure form
    submit_button = st.form_submit_button(label="🔒 SECURE & TRANSMIT EVIDENCE")

# --- DATA INGESTION ENGINE ---
if submit_button:
    end_time = time.time()
    retrieval_speed = round(end_time - st.session_state.start_time, 2)
    
    # Process "Other" clean values
    final_race = race_other if race_ethnicity == "Other" else race_ethnicity
    final_build = build_other if build_type == "Other" else build_type
    final_hair = hair_other if hair_details == "Other" else hair_details
    final_marks = marks_other if distinctive_marks == "Other" else distinctive_marks
    final_outerwear = outerwear_other if outerwear == "Other" else outerwear
    final_bottoms = bottoms_other if bottoms_footwear == "Other" else bottoms_footwear
    final_acc = accessories_other if accessories == "Other" else accessories
    final_speech = speech_other if speech_pattern == "Other" else speech_pattern
    final_gait = gait_other if movement_gait == "Other" else movement_gait
    final_state = state_other if state_of_mind == "Other" else state_of_mind

    # Package individual comprehensive report
    new_report = {
        "Witness ID": f"CITIZEN-{len(st.session_state.all_reports) + 1:03d}",
        "Age": age_range,
        "Sex": bio_sex,
        "Race/Complexion": final_race,
        "Build": final_build,
        "Hair": final_hair,
        "Marks": final_marks,
        "Outerwear": final_outerwear,
        "Bottoms": final_bottoms,
        "Accessories": final_acc,
        "Speech": final_speech,
        "Gait": final_gait,
        "State of Mind": final_state,
        "Retrieval Speed (s)": retrieval_speed
    }
    
    st.session_state.all_reports.append(new_report)
    st.success(f"Evidence Locked! Data transmitted securely in {retrieval_speed} seconds. Local cache purged.")
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
        # Generate the top mode for key distinct categories
        col1, col2, col3, col4 = st.columns(4)
        col1.metric(label="Suspect Profile", value=str(filtered_df["Sex"].mode()[0]))
        col2.metric(label="Top Apparel Focus", value=str(filtered_df["Outerwear"].mode()[0]))
        col3.metric(label="Detected Demeanor", value=str(filtered_df["State of Mind"].mode()[0]))
        col4.metric(label="Valid Accounts Logs", value=f"{valid_entries} / {len(df)}")
    else:
        st.error("No reports have bypassed the 12-second validity boundary yet. High probability of memory contamination.")

if st.button("🔄 Reset System Database"):
    st.session_state.all_reports = []
    st.session_state.start_time = time.time()
    st.rerun()
