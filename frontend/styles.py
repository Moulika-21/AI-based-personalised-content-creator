import streamlit as st

PRIMARY = "#2563EB"     # Blue
BG = "#E0F2FE"          
CARD_BG = "#FFFFFF"    

def apply_theme():
    st.markdown("""
    <style>

    /* Page background */
    .stApp {
        background-color: #E0F2FE;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #1E293B;
    }

    section[data-testid="stSidebar"] * {
        color: white;
    }
            

    /* Cards */
    .card {
        background-color: white;
        padding: 28px;
        border-radius: 18px;
        margin-bottom: 26px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.12);
        color: black;
    }
    

        
    /* Headings */
    .title {
        font-size: 40px;
        font-weight: 900;
        color: #1E293B;
        margin-bottom: 10px;
    }

    .subtitle {
        font-size: 18px;
        color: #334155;
        margin-bottom: 20px;
    }

    .feature-title {
        font-size: 20px;
        font-weight: 700;
        color: black;
        margin-bottom: 8px;
    }

    /* Buttons */
    .stButton > button {
        background-color: #2563EB;
        color: white;
        border-radius: 14px;
        padding: 10px 24px;
        font-weight: 700;
        border: none;
    }

    /* Labels */
    label {
        color: black !important;
        font-weight: 600;
    }

    </style>
    """, unsafe_allow_html=True)
