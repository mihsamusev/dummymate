def martin_say(message: str) -> str:
    if len(message) > 8:
        return "are you sure about that?"

    return f"I have great news: {message}"
