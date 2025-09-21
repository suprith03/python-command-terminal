import re

def parse_natural_command(sentence):
    sentence = sentence.lower()

    if "create" in sentence and "folder" in sentence:
        match = re.search(r"folder (.+)", sentence)
        if match:
            folder = match.group(1).strip()
            return f"mkdir {folder}"

    if "delete" in sentence or "remove" in sentence:
        match = re.search(r"(file|folder|directory) (.+)", sentence)
        if match:
            target = match.group(2).strip()
            return f"rm {target}"

    if "list" in sentence and "files" in sentence:
        return "ls"

    if "current directory" in sentence:
        return "pwd"

    if "cpu" in sentence or "memory" in sentence:
        return "stats"

    return None
