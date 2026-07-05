import os
from datetime import datetime


def save_output(output_folder, output_file, result):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    folder_path = os.path.join(base_dir, output_folder)
    os.makedirs(folder_path, exist_ok=True)

    path = os.path.join(folder_path, output_file)

    with open(path, "a", encoding="utf-8") as f:
        f.write(f"\n\n---\n\n## {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write(result)

    return path
