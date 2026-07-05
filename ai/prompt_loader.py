from pathlib import Path


PROMPT_FOLDER = Path("prompts")


def load_prompt(filename):
    path = PROMPT_FOLDER / filename

    with open(path, "r", encoding="utf-8") as f:
        return f.read()