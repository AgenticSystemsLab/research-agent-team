"""
Simple command-line interface for the Research Agent Team.
Usage:
    python main.py "Your research topic here"
"""

import sys
from dotenv import load_dotenv
from src.crews.research_crew import run_research

load_dotenv()


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"Your research topic\"")
        print('Example: python main.py "Best AI tools for beginners in 2026"')
        sys.exit(1)

    topic = " ".join(sys.argv[1:])
    print("=" * 60)
    print("🔍 RESEARCH AGENT TEAM")
    print("=" * 60)

    try:
        report = run_research(topic)
        print("\n" + "=" * 60)
        print("📄 FINAL REPORT")
        print("=" * 60 + "\n")
        print(report)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Make sure your OPENAI_API_KEY is set in the .env file.")


if __name__ == "__main__":
    main()
