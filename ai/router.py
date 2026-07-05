from ai.config_loader import load_workflows
from ai.prompt_loader import load_prompt
from ai.gemini import ask_gemini
from ai.output_manager import save_output


def process(task, text):

    workflows = load_workflows()

    task_key = task.strip().lower()

    if task_key not in workflows:
        raise ValueError(
            f"Unknown task '{task}'. Available tasks: {list(workflows.keys())}"
        )

    workflow = workflows[task_key]

    system_prompt = load_prompt(
        workflow["prompt"]
    )

    result = ask_gemini(
        system_prompt,
        text
    )

    save_output(
        workflow["output_folder"],
        workflow["output_file"],
        result
    )

    return result