def cowsay(message: str) -> str:
    top = " " + "_" * (len(message) + 2)
    bottom = " " + "-" * (len(message) + 2)
    msg = f"< {message} >"
    cow = """
        \\   ^__^
         \\  (oo)\\_______
            (__)\\       )\\/\\
                ||----w |
                ||     ||
    """
    return f"{top}\n{msg}\n{bottom}{cow}"
