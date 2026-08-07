# 🔍 Research Agent Team

**A multi-agent AI system that researches any topic and writes a clear, structured report.**

Built as a portfolio project to demonstrate practical AI agent skills.

# 🔍 Research Agent Team

🚀 **Live App:** [Click here to try the Live Agent](https://research-agent-team-git-981831266697.us-central1.run.app)

---

---

## What This Project Does

You give it a research question → a team of 3 AI agents work together → you get a well-written report.

| Agent | Role | What it does |
|-------|------|--------------|
| 🔎 **Researcher** | Senior Research Specialist | Searches the web for relevant, up-to-date information |
| 🧠 **Analyst** | Critical Analyst | Extracts key insights, trends, and important takeaways |
| ✍️ **Writer** | Professional Report Writer | Turns the analysis into a clean, readable report |

This is a real example of **multi-agent orchestration** — one of the core skills companies look for when hiring people who work with AI agents.

---

## Why This Project Matters (for recruiters / hiring managers)

This repository demonstrates:

- Building and coordinating multiple specialized AI agents
- Tool use (web search)
- Sequential agent workflows with context passing
- Clean project structure and readable code
- A working interactive demo (Streamlit)
- Practical understanding of agent roles, goals, and backstories

---

## Quick Demo

```bash
# After setup (see below)
streamlit run app.py
```

Or from the terminal:

```bash
python main.py "Best AI tools for beginners in 2026"
```

---

## Project Structure

```
research-agent-team/
├── app.py                  # Streamlit web interface (recommended way to try it)
├── main.py                 # Simple command-line version
├── requirements.txt
├── .env.example
├── src/
│   ├── crews/
│   │   └── research_crew.py    # The main multi-agent logic
│   ├── tools/
│   │   └── search_tools.py     # Web search tools
│   └── config/
│       ├── agents.yaml         # Agent role definitions
│       └── tasks.yaml          # Task definitions
├── examples/
└── docs/
```

---

## Setup Instructions (Beginner Friendly)

### 1. Prerequisites

- Python 3.10 or higher
- An OpenAI API key ([get one here](https://platform.openai.com/api-keys))

### 2. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/research-agent-team.git
cd research-agent-team
```

### 3. Create a virtual environment (recommended)

```bash
python -m venv venv

# On Mac/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Add your API key

```bash
cp .env.example .env
```

Open the `.env` file and paste your OpenAI API key:

```
OPENAI_API_KEY=sk-your-real-key-here
```

(Optional) For better search results, also add a free Tavily key from [tavily.com](https://tavily.com):

```
TAVILY_API_KEY=tvly-your-key-here
```

### 6. Run the project

**Option A – Web interface (easiest):**
```bash
streamlit run app.py
```

**Option B – Terminal:**
```bash
python main.py "Your research topic here"
```

---

## How the Agents Work Together

```
User Topic
    ↓
[Researcher]  →  searches the web using tools
    ↓
[Analyst]     →  reads the findings and extracts insights
    ↓
[Writer]      →  produces the final structured report
    ↓
Final Report
```

This sequential process is called a **Crew** in CrewAI. Each agent has:
- A clear **role**
- A specific **goal**
- A **backstory** that shapes how it behaves
- Access to tools (only the Researcher needs search tools)

---

## Example Output

When you run a topic like *"Best practices for building AI agents in 2026"*, you get a structured report with:

- Clear title and introduction
- Key insights section
- Practical recommendations
- Summary / takeaways

---

## Technologies Used

- **CrewAI** – Multi-agent orchestration framework
- **OpenAI (gpt-4o-mini)** – Language model
- **DuckDuckGo Search** – Free web search (no API key required)
- **Tavily** – Higher quality search (optional)
- **Streamlit** – Simple web interface
- **Python** – Core language

---

## What I Learned Building This

- How to design specialized agent roles instead of one general-purpose agent
- Passing context between agents cleanly
- Giving agents the right tools (and only the tools they need)
- Balancing cost, speed, and quality (using `gpt-4o-mini`)
- Creating a simple UI so non-technical people can try the system
- Writing clear documentation so others can run the project easily

---

## Possible Improvements (Future Work)

- Add memory so the system remembers previous research
- Support for uploading PDFs / documents
- Parallel research on multiple sub-topics
- Evaluation metrics (how good is the report?)
- Deployment to Streamlit Cloud or Hugging Face Spaces for a public demo link

---

## License

MIT License – feel free to use and modify.

---

**Built as a first AI agent portfolio project.**  
If you're a recruiter or hiring manager reading this — thank you for taking a look!
