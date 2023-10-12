
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
