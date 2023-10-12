
from general_agent.agent import callback


@callback.new(
    "Return a list of all possible agents",
    list[str]
)
def get_all_agents() -> list[str]:
    pass


@callback.new(
    "Talk and work with other agents. Returns their response",
    str,
    callback.new_arg("agent", str, "The agent you are trying to talk to", enum=[get_all_agents()[0]])
)
def summon_agent(agent: str, query: str) -> str:
    pass

@callback.new(
    "Get help from, or talk to a human. \
This takes time and energy so use it sparingly. \
You will always follow their response.",
    str,
    callback.new_arg("goal", str, "Your desired end result"),
    callback.new_arg("text", str, "The question or thing you want to ask a human")
)
def talk_to_a_human(goal: str, text: str) -> str:
    pass
