
from general_agent.agent import callback


@callback.new(
    "Create a new skill to help performing tasks in the future",
    None,
    callback.new_arg("steps", list[str], "The list of steps to take when performing the skill")
)
def create_skill(steps: list[str]) -> None:
    pass


@callback.new(
    "Update an already existing skill to help performing tasks in the future",
    None,
    callback.new_arg("skill", str, "The skill you want to update"),
    callback.new_arg("steps", list[str], "The list of steps to take when performing the skill"),
    callback.new_arg("reason", str, "The reason why you are updating this skill")
)
def update_skill(skill: str, steps: list[str], reason: str) -> None:
    pass
