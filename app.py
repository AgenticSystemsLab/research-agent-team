"""
Simple web interface for the Research Agent Team.
Works both locally and on Streamlit Community Cloud.
"""

import streamlit as st
import os
from dotenv import load_dotenv

# Load .env for local development
load_dotenv()

# Page config
st.set_page_config(
    page_title="Research Agent Team",
    page_icon="🔍",
    layout="wide"
)

# Custom styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #666;
        margin-bottom: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4F46E5;
        color: white;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)


def get_openai_key():
    """Get OpenAI API key from Streamlit secrets (cloud) or environment (local)."""
    # First try Streamlit secrets (for Streamlit Cloud)
    try:
        key = st.secrets.get("OPENAI_API_KEY", None)
        if key:
            return key
    except Exception:
        pass

    # Fallback to environment variable / .env (for local)
    return os.getenv("OPENAI_API_KEY")


def main():
    st.markdown('<div class="main-header">🔍 Research Agent Team</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="sub-header">A multi-agent AI system that researches any topic and writes a clear report for you.</div>',
        unsafe_allow_html=True
    )

    # Sidebar
    with st.sidebar:
        st.header("About this project")
        st.markdown("""
        This is a **multi-agent AI system** built with CrewAI.
        
        **The Team:**
        - 🔎 **Researcher** → searches the web
        - 🧠 **Analyst** → finds key insights
        - ✍️ **Writer** → creates the final report
        
        Built as a portfolio project to demonstrate AI agent skills.
        """)
        
        st.divider()
        st.markdown("**How it works**")
        st.markdown("""
        1. You enter a research topic
        2. The Researcher agent searches the web
        3. The Analyst agent extracts key insights
        4. The Writer agent produces a clean report
        """)

    # Get API key
    openai_key = get_openai_key()

    if not openai_key or openai_key == "sk-your-openai-key-here":
        st.error("⚠️ OpenAI API key is missing.")
        st.info("If you are the owner: Add the key in Streamlit Cloud → App Settings → Secrets.")
        st.stop()

    # Make sure the key is available as an environment variable for CrewAI
    os.environ["OPENAI_API_KEY"] = openai_key

    # Main input
    st.subheader("What would you like to research?")
    
    example_topics = [
        "Best AI tools for beginners in 2026",
        "How multi-agent systems work",
        "Pros and cons of remote work in 2026",
        "Latest trends in renewable energy",
        "How to start a career in AI engineering"
    ]

    # Use session state so example buttons work properly
    if "topic" not in st.session_state:
        st.session_state.topic = ""

    topic = st.text_input(
        "Enter your research topic",
        value=st.session_state.topic,
        placeholder="e.g. Best practices for building AI agents",
        key="topic_input"
    )

    st.caption("Or try one of these examples:")
    cols = st.columns(len(example_topics))
    for i, example in enumerate(example_topics):
        if cols[i].button(example, key=f"ex_{i}"):
            st.session_state.topic = example
            st.rerun()

    # Run button
    if st.button("🚀 Start Research", type="primary", use_container_width=True):
        final_topic = topic.strip() if topic else st.session_state.topic.strip()

        if not final_topic or len(final_topic) < 5:
            st.warning("Please enter a more specific research topic.")
        else:
            with st.spinner("The agent team is working... This usually takes 30–90 seconds."):
                try:
                    from src.crews.research_crew import run_research
                    report = run_research(final_topic)
                    
                    st.success("✅ Research complete!")
                    st.divider()
                    st.subheader("📄 Final Report")
                    st.markdown(report)
                    
                    st.download_button(
                        label="Download Report as Markdown",
                        data=report,
                        file_name=f"research_report_{final_topic[:30].replace(' ', '_')}.md",
                        mime="text/markdown"
                    )
                except Exception as e:
                    st.error(f"Something went wrong: {str(e)}")
                    st.info("Common fixes: Check your OpenAI API key and internet connection.")

    # Footer
    st.divider()
    st.caption("Built with CrewAI + Streamlit • Portfolio project demonstrating multi-agent AI systems")


if __name__ == "__main__":
    main()
