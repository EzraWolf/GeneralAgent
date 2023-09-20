
from general_agent.agent import callback

@callback.new(
    "View the current project space, its structure, and what folders and files are in it",
    dict,
)
def view_workspace() -> dict:
    pass


@callback.new(
    "Create a new file. This does not update nor read files.",
    None,
    callback.new_arg("contents", str, "The file contents"),
    callback.new_arg("filetype", str, "The filetype"),
    callback.new_arg("location", str, "The path to save the file in your workspace"),
)
def create_file(
    contents: str,
    filetype: str,
    location: str,
) -> None:
    pass


@callback.new(
    "Return a list of all possible agents",
    list[str]
)
def get_all_agents() -> list[str]:
    pass


@callback.new(
    "Talk and work with other agents. Returns their response",
    str,
    callback.new_arg("agent", str, "The agent you are trying to talk to", enum=get_all_agents())
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


@callback.new(
    "Search the internet for any information",
    str,
    callback.new_arg("text_query", str, "The search query")
)
def basic_web_search(text_query: str) -> str:
    """
    So-called "basic" search sequence of operations:
    1. Calls serper.dev's API using `text_query` and results about 10-12 URLs
    2. Uses `https://columbus.elmasy.com/api/lookup/{base domain}` to get all subdomains
    3. Scrapes each URL and subdomain for text and links
    4. Cleans and sanitizes the text output, and converts it to Markdown
    5. Gets the Markdown files and links text embedding through OpenAI's ADA V2 dodel
    6. Stores the raw text, sanitized text, URL links, and link and text embeddings in it's DB
    """
    pass


@callback.new(
    "Perform a deep search of the internet for any information",
    str,
    callback.new_arg("text_query", str, "The search query"),
    callback.new_arg(
        "search_engine",
        str,
        "The search engine used to search with",
        enum=["Google", "DuckDuckGo", "Bing", "Qwant"]
    )
)
def advanced_web_search(
    self,
    text_query: str,
    search_engine: str="google"
) -> str:
    """
    Use google parameter searching (also called google dorking) to obtain
    significantly more specific search results for specific topics.
    """
    pass


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


@callback.new(
    "Search a vector database of all of your prior knowledge",
    dict,
    callback.new_arg("db_query", str, "The query used to search the database"),
    callback.new_arg("n_results", int, "Return the n most similar results")
)
def search_database(db_query: str, n_results: int) -> dict:
    """
    As the company continues to search the internet, scrape and store
    articles, create and update new skills, departments, roles, etc.,
    it slowely starts building up its own general knowledge base
    """
    pass


@callback.new(
    "Calculate a math problem",
    dict,
    callback.new_arg("equation", dict, "??")
)
def calculate(equation: dict) -> dict:
    pass


@callback.new(
    "Fetch historical stock data",
    dict,
    callback.new_arg("stock_ticker", str, "The abbreviated name of the stock"),
    callback.new_arg("timeframe", str, "The duration of each candle",
        enum=[
            "1m", "5m", "15m",
            "1h", "4h",
            "1d",
            "1w",
        ]
    )
)
def get_stock_data(stock_ticker: str, timeframe: str) -> dict:
    pass