import streamlit as st
from frontend.sidebar import render_sidebar
from frontend.pages import home_page, create_content_page, settings_page
from frontend.styles import apply_theme

st.set_page_config(
    page_title="AI Content Creator",
    layout="wide"
)

st.markdown("""
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
.block-container {
    padding-top: 0.75rem;
}
</style>
""", unsafe_allow_html=True)

# Session state defaults
if "profile" not in st.session_state:
    st.session_state.profile = {
        "role": "Student",
        "tone": "Professional"
    }

if "theme" not in st.session_state:
    st.session_state.theme = "Light"

# apply_theme(st.session_state.theme)

apply_theme()

page = render_sidebar()

if page == "Home":
    home_page()
elif page == "Create Content":
    create_content_page(st.session_state.profile)
elif page == "Settings":
    settings_page()
