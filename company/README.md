
# Project Setup

Here is where you setup your projects and configure your "company"

It's called a company because the way the AI communicates and interacts with itself and other AIs is modeled after various company organizational structures and how company's talk and interact with internal departments / employees, and business partners.

What's unique about this so-called "AI company" though is that each project can have its own company structure, making custom projects easier to implement while still making it possible for new projects to reference older projects and learn from them.


## Directory

`agents` Here is where you define your AI Agents in `.yaml` config files

`projects` Here is where your projects will lie. Under this folder will contain each project folder and its `.yaml` config file

`prompts` Here is where your agent promprs will go. Each `.yaml` file under this will act as both a prompt and config file for how it should be used

`callbacks.py` This is a list of user-defined functions that the AI Agents can call to get some help when needed.

`structure.yaml` Undecided.
