from agents.refactor_agent import create_code_agent

def main():
    print("---Code Buddy Agent Live---")
    agent = create_code_agent()

    user_query = "Look at the files in my sandbox, find issues in messy_script.py, refactor it, and write the fixed code back to the file."

    response = agent.invoke({
        "messages": [{"role": "user", "content": user_query}]
    })

    last_message = response["messages"][-1].content

    print("---Agent's Final Report---")
    if isinstance(last_message, list):
        for block in last_message:
            if isinstance(block, dict) and block.get("type") == "text":
                print(block["text"])
            elif isinstance(block, str):
                print(block)
    else:
        print(last_message)

if __name__ == "__main__":
    main()