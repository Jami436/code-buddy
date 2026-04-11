# Code Buddy 🛠️ AI Code Refactor Agent

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![LangGraph](https://img.shields.io/badge/LangGraph-ReAct%20Agent-orange.svg)](https://langchain-ai.github.io/langgraph/)

**Code Buddy** is an AI-powered code analysis and refactoring agent built with [LangGraph](https://langchain-ai.github.io/langgraph/) ReAct agents and Google's Gemini LLM. It helps you identify issues in Python code (in the `sandbox/` directory), run linters (flake8, mypy), and automatically refactor files.

Perfect for cleaning up messy scripts – try it on `sandbox/messy_script.py`!

## ✨ Features
- **AI-Driven Refactoring**: Natural language queries like "Refactor messy_script.py, fix style issues, add types."
- **Code Analysis Tools**: Integrated flake8 (style/syntax) and mypy (type checking).
- **Sandbox File Ops**: List, read, write Python files in isolated `sandbox/`.
- **LangGraph ReAct Agent**: Tool-calling LLM agent for step-by-step reasoning.
- **Gemini 2.5 Flash**: Fast, cost-effective LLM integration.
- **Easy Setup**: Virtualenv-ready, dotenv for API keys.

## 🚀 Quick Start

1. **Clone &amp; Setup Environment**:
  git clone https://github.com/Jami436/code-buddy.git code-buddy
   cd code-buddy
   python -m venv venv
   # Windows: venv\\Scripts\\activate
   # macOS/Linux: source venv/bin/activate
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set API Key**:
   Create `.env`:
   ```
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```
   Get key from [Google AI Studio](https://aistudio.google.com/app/apikey).

4. **Run the Agent**:
   ```bash
   python main.py
   ```
   It runs an example refactor on `sandbox/messy_script.py`!

## 📖 Usage

Edit the `user_query` in `main.py` for custom tasks:
```python
user_query = "Your custom instruction here, e.g., Analyze sandbox files, fix messy_script.py bugs, improve structure."
```

Example Output:
```
---Code Buddy Agent Live---
---Agent&#39;s Final Report---
[Agent steps: lists files, analyzes with flake8/mypy, suggests/proposes refactors, writes fixed code]
Successfully wrote changes to messy_script.py.
```

## 🏗️ Architecture

```
main.py → agents/refactor_agent.py (create_react_agent)
          ↓
       Tools:
       - file_manager: list/read/write sandbox/*.py
       - analyzer: flake8/mypy
          ↓
     Gemini LLM → ReAct Loop → Actions/Observations
```

**Agent Flow**:
1. User query → Agent plans (ReAct: Thought → Action → Observation).
2. Calls tools (e.g., list files, run flake8).
3. Reasons, generates fixed code.
4. Writes back to sandbox file.

## 🗂️ Sandbox Setup

- Place Python files in `sandbox/` (e.g., `messy_script.py`).
- Agent auto-discovers `*.py` files.
- Safe: Isolated dir, overwrites only on write tool call.

Example messy code in `sandbox/messy_script.py`:
```python
x = 10  # Globals, no types, style issues → Agent fixes!
```

## 🛠️ Tools

| Tool | Description | Example |
|------|-------------|---------|
| `list_sandbox_files` | Lists all `*.py` in sandbox | `[\&#39;messy_script.py\&#39;]` |
| `read_file_content` | Reads file content | Raw Python source |
| `write_file_content` | Overwrites file with new code | `"Successfully wrote..."` |
| `run_flake8_analysis` | Runs flake8 linting | Errors or "No issues" |
| `run_mypy_analysis` | Runs mypy type check | Type errors or "No issues" |

## 📦 Requirements

Populated `requirements.txt` with:
```
langchain-google-genai
langgraph
python-dotenv
flake8
mypy
```

## 🔮 Roadmap
- [ ] Support more linters (pylint, black formatter).
- [ ] Multi-language (JS, etc.).
- [ ] Web UI for queries.
- [ ] Git integration (commit changes).
- [ ] More agents (e.g., test generator).

## 🤝 Contributing
1. Fork &amp; PR.
2. Add tools to `tools/`, update agent.
3. Follow PEP8.

## 📄 License
MIT – See [LICENSE](LICENSE) (create if needed).

**Built with ❤️ using LangChain ecosystem. Star if useful! ⭐**

