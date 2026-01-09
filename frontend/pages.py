import streamlit as st
from backend.prompt_builder import build_prompt
from backend.gemini_client import generate_content

def home_page():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="title">AI Personalized Content Creator</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">'
        'A modern AI platform to generate personalized, high-quality content for different users and platforms.'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <div class="feature-title">🎯 Personalized Content</div>
            Content tailored based on user role, tone preferences, and platform requirements.
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div class="feature-title">⚡ Powered by Gemini AI</div>
            Uses Google Gemini LLM to generate accurate, human-like, and professional content.
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <div class="feature-title">🎨 Modern UI</div>
            Clean, colorful, and responsive interface built entirely with Streamlit.
        </div>
        """, unsafe_allow_html=True)

    col4, col5 = st.columns(2)

    with col4:
        st.markdown("""
        <div class="card">
            <div class="feature-title">✍️ Multiple Content Types</div>
            Generate social media posts, emails, ad copies, and professional introductions.
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown("""
        <div class="card">
            <div class="feature-title">⚙️ Customizable Settings</div>
            Configure role, tone, and theme to match individual user preferences.
        </div>
        """, unsafe_allow_html=True)

# st.markdown('<div class="form-heading">Create Content</div>', unsafe_allow_html=True)


def create_content_page(profile):
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="form-heading">Create Content</div>', unsafe_allow_html=True)

    content_type = st.selectbox(
        "Content Type",
        ["Social Media Post", "Email", "Ad Copy"]
    )

    platform = st.selectbox(
        "Platform",
        ["LinkedIn", "Instagram", "Email", "Twitter"]
    )

    topic = st.text_area(
        "Content Topic",
        placeholder="Example: First day introduction as an intern"
    )

    if st.button("Generate Content"):
        prompt = build_prompt(profile, topic, platform)
        with st.spinner("Generating content..."):
            output = generate_content(prompt)
        if output is None:
            st.text_area("Something is wrong please try again",output, height=250)
        else:
            st.text_area("Generated Content", output, height=250)
        
            

    st.markdown('</div>', unsafe_allow_html=True)



def settings_page():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="form-heading">Settings</div>', unsafe_allow_html=True)

    # Temporary selections (do NOT save yet)
    temp_role = st.selectbox(
        "Your Role",
        ["Student", "Intern", "Business Analyst", "Developer"],
        index=["Student", "Intern", "Business Analyst", "Developer"].index(
            st.session_state.profile["role"]
        )
    )

    temp_tone = st.selectbox(
        "Preferred Tone",
        ["Professional", "Friendly", "Casual"],
        index=["Professional", "Friendly", "Casual"].index(
            st.session_state.profile["tone"]
        )
    )

    st.markdown("---")

    if st.button("💾 Save Settings"):
        st.session_state.profile["role"] = temp_role
        st.session_state.profile["tone"] = temp_tone
        st.success("Settings saved successfully ✅")

    st.markdown('</div>', unsafe_allow_html=True)
