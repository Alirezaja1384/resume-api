def to_list(txt: str):
    return [item.strip() for item in txt.split(",")]


def file_or_text(inp: str) -> str:
    # Example: "some string"
    if not inp.startswith("file:"):
        return inp

    # Example: "file: the_file_to_read.txt"
    file_name = inp[5:].strip()
    with open(file_name, "r", encoding="utf8") as file:
        return file.read()
