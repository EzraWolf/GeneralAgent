
"""
Combines the other files inside of `/agent` here to create a uniform AI Agent
"""

class Agent():
    """
    This defines all AI agents
    NOTE: Humans / users / operators are also considered
          agents, and they have the same capabilitites as
          any other agent would.

    What makes an agent different from just a regular AI
    chat completion is the ability to:
        - Have agents create / update agents through yaml config files
        - Have agents reate / update / use functional callbacks
        - Log and process conversation similar how people do, storing, summarizing,
          conceptualizing, creating observations, and drawing relationships, etc. 
        - Express thought and reason before making a final response
          (Similar to us thinking in our head, it just needs to be outloud here)
        - Multiple of the same agent can exist, acting like people with the same
          expertise / experiences talking to each other. Helps kick up new thought
        - TODO: Tired and forgot the other things goodnight.
    """

    role        : str = ""
    purpose     : str = ""
    agent_ct    : int = 3

    # Backend configs
    sys_prompt  : str = ""
    focuses     : list[str] = []
    constraints : list[str] = []

    def __init__(self) -> None:
        pass
