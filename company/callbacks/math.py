
from general_agent.agent import callback


@callback.new(
    "Calculate a math problem",
    dict,
    callback.new_arg("equation", dict, "??")
)
def calculate(equation: dict) -> dict:
    pass
