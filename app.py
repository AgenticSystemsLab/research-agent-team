"""
Simple web interface for the Research Agent Team.
Run with: streamlit run app.py
"""

import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
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

    # Check for API key
    openai_key = os.getenv("OPENAI_API_KEY")
    if not openai_key or openai_key == "sk-your-openai-key-here":
        st.error("⚠️ Please set your OPENAI_API_KEY in the .env file before running.")
        st.info("Copy `.env.example` to `.env` and add your OpenAI API key.")
        st.stop()

    # Main input
    st.subheader("What would you like to research?")
    
    example_topics = [
        "Best AI tools for beginners in 2026",
        "How multi-agent systems work",
        "Pros and cons of remote work in 2026",
        "Latest trends in renewable energy",
        "How to start a career in AI engineering"
    ]

    topic = st.text_input(
        "Enter your research topic",
        placeholder="e.g. Best practices for building AI agents"
    )

    st.caption("Or try one of these examples:")
    cols = st.columns(len(example_topics))
    for i, example in enumerate(example_topics):
        if cols[i].button(example, key=f"ex_{i}"):
            topic = example
            st.session_state.topic = example

    # Run button
    if st.button("🚀 Start Research", type="primary", use_container_width=True):
        if not topic or len(topic.strip()) < 5:
            st.warning("Please enter a more specific research topic.")
        else:
            with st.spinner("The agent team is working... This usually takes 30–90 seconds."):
                try:
                    from src.crews.research_crew import run_research
                    report = run_research(topic.strip())
                    
                    st.success("✅ Research complete!")
                    st.divider()
                    st.subheader("📄 Final Report")
                    st.markdown(report)
                    
                    # Download button
                    st.download_button(
                        label="Download Report as Markdown",
                        data=report,
                        file_name=f"research_report_{topic[:30].replace(' ', '_')}.md",
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
