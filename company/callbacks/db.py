
from general_agent.agent import callback


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
