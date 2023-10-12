
"""
Load prompts from `.yaml` prompt configs inside of the `/company` folder

Based off of Google Deepminds "Promptbreeder":
Utilizes prompt mutation from `/mutator.py` and prompt effectiveness
evaluation from `/evaluator.py` to self-improve its own prompts from
and its AI Agent `.yaml`s from inside the company workspace.

NOTE: The ONLY prompts and agent files edited are from the company
      workspace, nothing from this folder, not anything else is.
"""

class Prompt():
    """
    Defines a prompt from the `.yaml` prompt config files
    """

    name      : str = ""
    purpose   : str = ""
    prompt    : str = ""
    callbacks : list[str] = []

    def __init__(self) -> None:
        pass

    def load_yaml(path: str) -> str:
        pass
