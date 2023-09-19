
# from .assets import prompts
from general_agent.agent import callback
from general_agent.agent import openai_api

def main() -> None:
    # ?

    """
    chat = openai_api.OpenAI()

    first_msg = chat.create_usr_message(
        "gpt-4",
        "user"
        "What is today",
        
        sys_prompt="You are an expert at something",
    )
    chat.messages.append(first_msg)

    chat.gpt_generate(
        "gpt-3.5-turbo",
        "Hello world",
        "You are an expert at assisting people",
        msg_lookback_ct=5,
        temperature=0,
    )
    """

if __name__ == "__main__":
    main()
