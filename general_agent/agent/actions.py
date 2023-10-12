
"""
Define and provide means for an AI Agent to perform actions

"Actions" are similar to callback commands, but are placed
at the end of each agents response, allowing conversations
to continue, end, shift direction, etc.

The current end-of-response action list:
<CONTINUE_CONVO, desired_outcome>
<CHANGE_TOPIC, topic, reason_why, message>
<PROMPT_HUMAN, topic, reason_why, message>
<CALLBACK, function, [parameters]>
<>
<>
<>
<END_CONVO, reason_why>
"""

class Action():
    def __init__(self) -> None:
        pass

    def perform(self) -> None:
        """
        Because end-of-response actions can be chained,
        we need to be able to evaluate them one-by-one.
        """
        pass
