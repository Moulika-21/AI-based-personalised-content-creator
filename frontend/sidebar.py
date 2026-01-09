import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.markdown("## ✨ AI Content Creator")
        st.markdown("Personalized Content Platform")
        st.markdown("---")

        page = st.radio(
            "Navigation",
            ["Home", "Create Content", "Settings"]
        )

        return page
