
def cowsay(message):
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


if __name__ == "__main__":
    from termcolor import colored
    message = "geeez"
    colored_message = colored("geeez", "red")
    print(cowsay(message))
    print(cowsay(colored_message))
