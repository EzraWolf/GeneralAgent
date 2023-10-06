

class BuildLLMPrompt(object):
	def __init__(self, llm_name: str) -> None:

		# LLM Information
		self.llm_name : str = llm_name

		# Prompt settings
		self.llm_allowed_callbacks    : list[str] = []
		self.llm_allow_short_term_mem : bool      = False
		self.llm_allow_assist_prompts : bool      = False
		self.llm_input_token_cap      : int       = -1
		self.llm_output_token_cap     : int       = -1

		# System prompt information
		self.llm_sys_self_info        : str = ""
		self.llm_sys_crnt_info        : str = ""
		self.llm_sys_main_role        : str = ""
		self.llm_sys_purposes         : list[str] = []
		self.llm_sys_performance_attr : list[str] = []
		self.llm_sys_behaviors        : list[str] = []
		self.llm_sys_constraints      : list[str] = []

		# The prompt base is what the "main" prompt is about. E.G., copywrite, translate, etc.
		# It's called a the prompt "base" because it containts the all of the variables written
		# as "{{variable}}" and eventually replaces them.
		self.llm_usr_prompt_base   : str = ""
		self.llm_usr_prompt_assist : str = ""
		self.llm_usr_prompt_output_modifier : str = ""
		self.llm_usr_prompt_output_format   : str = ""



	def set_llm_settings(
			self,
			allowed_callbacks: list[str],

	) -> str:
		pass

	def build_system_prompt():
		'''
		Build the LLMs system prompt
		The system prompt relies on these prompt blocks from `./assets/prompts`
		specifically in this order:
			- Self-Information
			- Current Information
			- Main Role
			- (3x) Purposes
			- (3x) Performance Attributes
			- (3x) Behaviors
			- (5x) Constraints
		'''
		pass

	def build_user_prompt() -> str:

	# Build user prompt too tired right now going to bed
