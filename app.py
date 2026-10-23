import streamlit as st
import pandas as pd
import time
import random
from collections import Counter
import re

# Set up page configurations
st.set_page_config(page_title="Zero-Leak Forensic Engine", page_icon="🚨", layout="centered")

st.title("🚨 Zero-Leak Forensic Hub")
st.subheader("GovTech Interface: Predictive Consensus & Analytics Engine")
st.markdown("---")

# Initialize persistent session states for reports and timing metrics
if "all_reports" not in st.session_state:
    st.session_state.all_reports = []

if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

# --- PROACTIVE PORTFOLIO CONTROLS (Top Panel for Admissions Officers) ---
st.sidebar.header("🛠️ Portfolio Developer Controls")
st.sidebar.write("Use these options to simulate high-velocity data load inputs dynamically.")

if st.sidebar.button("🤖 Simulate 50 Witness Influx"):
    simulated_batch = []
    current_count = len(st.session_state.all_reports)
    
    # Pre-defined traits for smart generation
    crime_pool = ["Armed Robbery", "Murder / Homicide", "Attempted Murder", "Assault"]
    sex_pool = ["Male", "Female", "Non-Binary Presentation"]
    apparel_pool = ["Black Hoodie", "Blue Jacket", "Red Shirt/Sweater", "Other"]
    state_pool = ["Nervous/Panic", "Aggressive/Hostile", "Calm/Calculated"]
    
    # Custom forensic context variations to test text-extraction logic
    clothing_narratives = [
        "Subject wore a distinct purple shawl over the outfit.",
        "Wearing a purple shawl and dark sneakers.",
        "Fled scene with a black beret pulled low.",
        "Noticed a black beret on the suspect's head.",
        "Normal attire but wearing a bright red running shoe.",
        "Standard dark jeans, nothing else noted."
    ]
    
    behavior_narratives = [
        "Spoke briefly with a strong local accent.",
        "Shouted aggressively with a foreign accent.",
        "Noticed a heavy limp on the left foot.",
        "Suspect was limping heavily away from the scene.",
        "Pacing continuously before the sudden escalation."
    ]
    
    for i in range(1, 51):
        # 80% of generated witnesses will be fast (under 12s), 20% slow/corrupted memory
        speed_profile = random.choice([random.uniform(2.5, 9.8), random.uniform(13.1, 25.0)])
        
        # Inject matching keywords to force a consensus trigger
        custom_cloth = random.choice(clothing_narratives) if random.random() > 0.3 else ""
        custom_behav = random.choice(behavior_narratives) if random.random() > 0.4 else ""
        
        simulated_batch.append({
            "Witness ID": f"SIM-CITIZEN-{current_count + i:03d}",
            "Crime Type Selected": random.choice(crime_pool),
            "Custom Crime Details": "Automatic simulation data vector stream.",
            "Age Range": random.choice(["Teenager", "Twenties/Thirties", "Middle-Aged"]),
            "Sex": "Male" if random.random() > 0.3 else random.choice(sex_pool),
            "Race/Complexion": "Dark/Black",
            "Custom Demographics": "",
            "Build": "Athletic",
            "Hair": "Short Dark",
            "Marks": "None",
            "Custom Physical Traits": "",
            "Outerwear": random.choice(apparel_pool),
            "Bottoms": "Dark Jeans",
            "Accessories": "None",
            "Custom Clothing Details": custom_cloth,
            "Speech": "Local Accent",
            "Gait": "Normal/Running",
            "State of Mind": random.choice(state_pool),
            "Custom Behavior Details": custom_behav,
            "Retrieval Speed (s)": round(speed_profile, 2)
        })
    
    st.session_state.all_reports.extend(simulated_batch)
    st.sidebar.success("Successfully ingested 50 simulated cryptographic data streams!")

if st.sidebar.button("🔄 Clear System Database"):
    st.session_state.all_reports = []
    st.session_state.start_time = time.time()
    st.rerun()

# --- CITIZEN INTERFACE ---
st.header("Step 1: Live Citizen Reporting Interface")
with st.form(key="comprehensive_forensic_form", clear_on_submit=True):
    st.error("#### 🛡️ Incident Details")
    crime_type = st.radio("Type of Crime Witnessed:", ["Armed Robbery", "Murder / Homicide", "Attempted Murder", "Assault", "Theft / Burglary", "Other"], horizontal=True)
    crime_other = st.text_input("If 'Other' or to add extra incident details, type here:", placeholder="e.g., Weapon used, getaway route notes...")

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

if submit_button:
    end_time = time.time()
    retrieval_speed = round(end_time - st.session_state.start_time, 2)
    
    st.session_state.all_reports.append({
        "Witness ID": f"CITIZEN-{len(st.session_state.all_reports) + 1:03d}",
        "Crime Type Selected": crime_type, "Custom Crime Details": crime_other,
        "Age Range": age_range, "Sex": bio_sex, "Race/Complexion": race_ethnicity, "Custom Demographics": demographic_other,
        "Build": build_type, "Hair": hair_details, "Marks": distinctive_marks, "Custom Physical Traits": physical_other,
        "Outerwear": outerwear, "Bottoms": bottoms_footwear, "Accessories": accessories, "Custom Clothing Details": clothing_other,
        "Speech": speech_pattern, "Gait": movement_gait, "State of Mind": state_of_mind, "Custom Behavior Details": behavior_other,
        "Retrieval Speed (s)": retrieval_speed
    })
    st.success(f"Evidence Locked! Data transmitted securely to GovHub in {retrieval_speed} seconds.")
    st.session_state.start_time = time.time()

# --- INVESTIGATOR DASHBOARD ---
st.markdown("---")
st.header("🕵️‍♂️ Real-Time Investigator Dashboard")

if len(st.session_state.all_reports) == 0:
    st.warning("Awaiting incoming citizen data streams. Submit a report manually or use the Developer Controls panel in the sidebar.")
else:
    df = pd.DataFrame(st.session_state.all_reports)
    
    # Neuroscience filter: Keep rapid-response logs under 12s
    filtered_df = df[df["Retrieval Speed (s)"] <= 12.0]
    valid_entries = len(filtered_df)
    
    st.write("### 🧠 Predictive Consensus Analytics")
    if valid_entries > 0:
        col1, col2, col3 = st.columns(3)
        
        # Guard mode checks to prevent metric display errors if fields are blank
        mode_sex = filtered_df["Sex"].mode()
        mode_state = filtered_df["State of Mind"].mode()
        
        col1.metric(label="Primary Suspect Profile", value=str(mode_sex.iloc if not mode_sex.empty else "N/A"))
        col2.metric(label="Dominant Demeanor", value=str(mode_state.iloc if not mode_state.empty else "N/A"))
        col3.metric(label="Data Integrity Base", value=f"{valid_entries} / {len(df)}")
        
        # --- NLP NARRATIVE ANALYSIS ENGINE ---
        st.write("### 🔍 Extracted Custom Clue Consensus")
        text_fields = ["Custom Crime Details", "Custom Demographics", "Custom Physical Traits", "Custom Clothing Details", "Custom Behavior Details"]
        all_words = []
        stop_words = {"the", "a", "an", "and", "or", "but", "is", "was", "were", "with", "wearing", "in", "on", "at", "to", "over", "data", "vector", "stream", "automatic", "simulation"}
        
        for field in text_fields:
            for text in filtered_df[field].dropna():
                words = re.findall(r'\w+', text.lower())
                all_words.extend([word for word in words if word not in stop_words])
        
        word_counts = Counter(all_words)
        common_clues = {word: count for word, count in word_counts.items() if count >= 3}
        
        if common_clues:
            # Sort clues and display top matches safely wrapped inside the container logic
            sorted_clues = sorted(common_clues.items(), key=lambda item: item, reverse=True)[:3]
            for clue, count in sorted_clues:
                st.warning(f"🚨 **High-Frequency Narrative Match:** '{clue.upper()}' flagged across {count} separate rapid-response accounts.")
        else:
            st.info("Cross-referencing open narratives... No high-frequency phrase anomalies detected.")
            
        st.write("#### Full Text Logging Review")
        st.dataframe(df[["Witness ID", "Custom Crime Details", "Custom Clothing Details", "Custom Behavior Details", "Retrieval Speed (s)"]], use_container_width=True)
    else:
        st.error("No high-speed data arrays available for mathematical profiling.")
