
from general_agent.agent import callback


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
