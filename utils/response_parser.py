def extract_text(response) -> str:
    """
    Extract readable text from a LangGraph response.
    """

    last_message = response["messages"][-1].content

    if isinstance(last_message, list):

        text = ""

        for block in last_message:

            if isinstance(block, dict):

                if block.get("type") == "text":
                    text += block["text"] + "\n"

            elif isinstance(block, str):
                text += block + "\n"

        return text.strip()

    return str(last_message)