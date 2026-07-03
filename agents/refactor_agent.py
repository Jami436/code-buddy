import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from tools.file_manager import list_sandbox_files, read_file_content, write_file_content
from tools.analyzer import run_flake8_analysis
from prompts.system_prompt import SYSTEM_PROMPT
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

def create_code_agent():
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

    tools = [list_sandbox_files, read_file_content, write_file_content, run_flake8_analysis]

    
    memory_saver = InMemorySaver()

    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=SYSTEM_PROMPT,
        checkpointer=memory_saver
    )

    return agent