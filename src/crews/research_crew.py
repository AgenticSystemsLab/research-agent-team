"""
This is the heart of the project.
It creates a team (Crew) of AI agents that work together on research.
"""

from crewai import Agent, Task, Crew, Process, LLM
import os
from dotenv import load_dotenv

from src.tools.search_tools import get_search_tools

load_dotenv()


def create_research_crew(topic: str):
    """
    Create and return a fully configured research crew for the given topic.
    """

    # 1. Choose the language model (modern CrewAI way)
    llm = LLM(
        model="gpt-4o-mini",
        temperature=0.3,  # Lower = more focused and consistent
    )

    # 2. Get search tools
    search_tools = get_search_tools()

    # 3. Create the three agents
    researcher = Agent(
        role="Senior Research Specialist",
        goal="Find accurate, up-to-date, and relevant information from the web about the given topic",
        backstory=(
            "You are an expert researcher with years of experience finding high-quality information online. "
            "You know how to use search tools effectively, identify reliable sources, and collect the most "
            "important facts. You always aim for accuracy and avoid low-quality or outdated information."
        ),
        tools=search_tools,
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )

    analyst = Agent(
        role="Critical Analyst",
        goal="Analyze the research findings, identify key insights, patterns, and important takeaways",
        backstory=(
            "You are a sharp analyst who can look at a pile of information and quickly extract what matters. "
            "You are good at spotting trends, comparing different viewpoints, and highlighting the most "
            "valuable insights. You think critically and do not just summarize — you add real understanding."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )

    writer = Agent(
        role="Professional Report Writer",
        goal="Write a clear, well-structured, and engaging research report based on the analysis",
        backstory=(
            "You are an excellent writer who turns complex information into easy-to-read reports. "
            "You structure content with clear headings, bullet points, and a logical flow. "
            "Your writing is professional but friendly, and always ends with a useful summary."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )

    # 4. Create the three tasks
    research_task = Task(
        description=(
            f"Research the following topic thoroughly: {topic}\n\n"
            "Use the search tools available to find recent and reliable information. "
            "Collect key facts, statistics, different viewpoints, and useful examples. "
            "Focus on quality over quantity. Prefer recent sources when possible."
        ),
        expected_output=(
            "A detailed collection of research findings including:\n"
            "- Key facts and data points\n"
            "- Important sources and links\n"
            "- Different perspectives on the topic\n"
            "- Any notable trends or recent developments"
        ),
        agent=researcher,
    )

    analysis_task = Task(
        description=(
            "Analyze the research findings provided by the researcher.\n\n"
            "Identify the most important insights, patterns, and takeaways. "
            "Highlight what is most valuable for someone learning about this topic. "
            "Point out any conflicting information or areas that need caution."
        ),
        expected_output=(
            "A clear analysis containing:\n"
            "- Top 5-7 key insights\n"
            "- Main trends or patterns\n"
            "- Important caveats or limitations\n"
            "- What a beginner should know first"
        ),
        agent=analyst,
        context=[research_task],
    )

    writing_task = Task(
        description=(
            "Write a professional research report based on the analysis.\n\n"
            "The report should be easy to read and well structured. "
            "Use headings, bullet points, and short paragraphs. "
            "Make it valuable for someone who wants to understand the topic quickly."
        ),
        expected_output=(
            "A complete research report with:\n"
            "- Clear title\n"
            "- Short introduction\n"
            "- Main sections with headings\n"
            "- Key takeaways or conclusion\n"
            "- Sources section (if available)"
        ),
        agent=writer,
        context=[analysis_task],
    )

    # 5. Create the Crew (the team)
    crew = Crew(
        agents=[researcher, analyst, writer],
        tasks=[research_task, analysis_task, writing_task],
        process=Process.sequential,
        verbose=True,
    )

    return crew


def run_research(topic: str) -> str:
    """
    Simple function to run the full research process and return the final report.
    """
    print(f"\n🚀 Starting research on: {topic}\n")
    crew = create_research_crew(topic)
    result = crew.kickoff()
    return str(result)