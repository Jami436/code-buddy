# Code Buddy v2.0

**Code Buddy** is an AI-powered software engineering assistant built with **Python**, **LangGraph**, and **Google Gemini**. It provides an interactive command-line interface that helps developers analyze, review, and refactor Python code using an LLM while keeping users in control of file modifications.

---

## Features

- Interactive AI-powered CLI
- List Python files in the sandbox
- Read files with syntax highlighting
- AI code analysis
- AI-powered code refactoring
- Confirmation before overwriting files
- Automatic `.bak` backup creation
- Conversation memory using LangGraph
- Rich terminal interface

---

## Tech Stack

- Python 3.13+
- Google Gemini
- LangGraph
- LangChain
- Rich
- Python Dotenv
- Flake8
- Mypy

---

## Project Structure

```
code-buddy/
│
├── agents/
│   └── refactor_agent.py
│
├── prompts/
│   ├── analyze.py
│   ├── refactor.py
│   ├── review.py
│   └── system_prompt.py
│
├── tools/
│   ├── analyzer.py
│   └── file_manager.py
│
├── utils/
│   ├── banner.py
│   ├── cli.py
│   ├── command_handler.py
│   ├── command_result.py
│   ├── code_parser.py
│   ├── errors.py
│   ├── printer.py
│   └── response_parser.py
│
├── sandbox/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/Jami436/code-buddy.git
cd code-buddy
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

Run the project

```bash
python main.py
```

---

## Available Commands

| Command | Description |
|----------|-------------|
| `/help` | Show available commands |
| `/files` | List Python files inside the sandbox |
| `/read <file>` | Display a Python file |
| `/analyze <file>` | Analyze code using Gemini |
| `/refactor <file>` | Refactor code with AI |
| `/clear` | Clear the terminal |
| `/exit` | Exit Code Buddy |

---

## Example

```text
You: /analyze messy_script.py

Thinking...

## Summary
The code is functional but can be improved.

Issues Found
-------------
• Variable names could be more descriptive
• Missing type hints
• Long functions
• Minor code duplication

Recommendations
----------------
• Add type hints
• Improve readability
• Split large functions
```

---

## Refactoring Workflow

```
User
   │
   ▼
Read Python File
   │
   ▼
Generate AI Refactor
   │
   ▼
Preview Result
   │
   ▼
Apply Changes? (Y/N)
   │
   ├── Yes → Backup Original → Save Refactored File
   │
   └── No → Discard Changes
```

---

## Roadmap

### ✅ Version 2.0

- Interactive CLI
- AI Code Analysis
- AI Code Refactoring
- Rich Terminal UI
- Prompt Management
- Automatic Backups
- LangGraph Memory

### Version 2.1

- Git Integration
- Project-wide Analysis
- Multi-file Refactoring
- AI Code Review
- Unit Test Generation
- Documentation Generation

---

## Author

**Muhammad Jami Ahad**

AI Student | Backend Developer | Building AI-powered solutions

GitHub: https://github.com/Jami436

---

## License

This project is licensed under the MIT License.