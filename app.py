import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="UNTANGLE | AI P&ID Simplifier", layout="wide")

st.markdown("""
    <style>
    .main {background-color: #FAFAFA;}
    .stButton>button {width: 100%; background-color: #0052FF; color: white;}
    .header-text {color: #1A1A1A; font-family: sans-serif;}
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='header-text'>Project UNTANGLE</h1>", unsafe_allow_html=True)
st.markdown("**AI-Driven P&ID Line Simplification & Flow Graph Layout**")
st.markdown("---")

with st.sidebar:
    st.header("1. Input Data")
    uploaded_pdf = st.file_uploader("Upload P&ID (PDF)", type=["pdf"])
    uploaded_excel = st.file_uploader("Upload IO List (Excel)", type=["xlsx", "xls"])
    
    st.header("2. Engine Settings")
    detect_symmetry = st.checkbox("Enable Pattern Collapse (Duty/Standby)", value=True)
    enforce_orthogonal = st.checkbox("Enforce Orthogonal Lines", value=True)
    
    process_btn = st.button("Generate Simplified Sketch")

if process_btn and uploaded_pdf and uploaded_excel:
    with st.spinner("Initializing Graph-Informed Structural Flattening Engine..."):
        time.sleep(1.5)
        st.success("Extraction & Layout Complete!")
        
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Original P&ID Snippet")
        st.image("https://via.placeholder.com/600x400.png?text=Original+Complex+P%26ID+View", use_column_width=True)
        
    with col2:
        st.subheader("Generated Simplified Sketch")
        st.image("https://via.placeholder.com/600x400.png?text=Clean+Orthogonal+Process+Sketch", use_column_width=True)

    st.markdown("---")
    st.subheader("Tag Reconciliation Audit")
    
    audit_data = {
        "Tag": ["LT-101", "PT-101A", "FT-101B", "XV-204", "TT-305"],
        "Found on P&ID": ["Yes", "Yes", "Yes", "No", "Yes"],
        "In IO List": ["Yes", "Yes", "Yes", "Yes", "No"],
        "Status": ["Matched", "Matched", "Matched", "Missing on Drawing", "Unlisted in IO"]
    }
    df = pd.DataFrame(audit_data)
    
    st.dataframe(df, use_container_width=True)
    
    st.download_button(
        label="Download Simplified Sketch (PDF)",
        data="mock_pdf_byte_stream",
        file_name="Simplified_Sketch_Unit200.pdf",
        mime="application/pdf"
    )

elif process_btn:
    st.error("Please upload both the P&ID PDF and the IO List Excel file to proceed.")
else:
    st.info("Upload your engineering files in the sidebar and click Generate to run the UNTANGLE engine.")