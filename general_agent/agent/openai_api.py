
import os
import openai
import tiktoken


# Chatting Models
GPT_4_08K_CHAT_INP_TOKEN_COST           : float = 0.00003    # $0.03   / 1K
GPT_4_08K_CHAT_OUT_TOKEN_COST           : float = 0.00006    # $0.06   / 1K
GPT_4_32K_CHAT_INP_TOKEN_COST           : float = 0.00006    # $0.06   / 1K
GPT_4_32K_CHAT_OUT_TOKEN_COST           : float = 0.00012    # $0.12   / 1K

GPT_3_5_TURBO_04K_CHAT_INP_TOKEN_COST   : float = 0.0000015  # $0.0015 / 1K
GPT_3_5_TURBO_04K_CHAT_OUT_TOKEN_COST   : float = 0.000002   # $0.002  / 1K
GPT_3_5_TURBO_16K_CHAT_INP_TOKEN_COST   : float = 0.000003   # $0.003  / 1K
GPT_3_5_TURBO_16K_CHAT_OUT_TOKEN_COST   : float = 0.000004   # $0.004  / 1K

# Fine-Tuning
GPT_3_5_TURBO_FINE_TUNING_TUN_TOKEN_COST: float = 0.000008   # $0.008  / 1K
GPT_3_5_TURBO_FINE_TUNING_INP_TOKEN_COST: float = 0.000012   # $0.012  / 1K
GPT_3_5_TURBO_FINE_TUNING_OUT_TOKEN_COST: float = 0.000016   # $0.016  / 1K

# Embedding
ADA_002_8K_EMBEDDING_TOKEN_COST            : float = 0.0000001  # $0.0001 / 1K

# Image Creation
DALLE_1024_1024_IMAGE_COST                 : float = 0.02
DALLE_512_512_IMAGE_COST                   : float = 0.018
DALLE_256_256_IMAGE_COST                   : float = 0.016

# Dictionary that holds info on each model
# Costs are defined as *per token* NOT as *per 1K tokens*
MODELS: dict = {

	# GPT-4
	"gpt-4": {

		# This is as of 28 Aug., 23. It may change with newer updates
		"cost": {
			"tokens_per_msg": 3,
			"tokens_per_name": 1,
			"input": GPT_4_08K_CHAT_INP_TOKEN_COST,
			"output": GPT_4_08K_CHAT_OUT_TOKEN_COST
		}
	},
	"gpt-4-0613": {
		"cost": {
			"tokens_per_msg": 3,
			"tokens_per_name": 1,
			"input": GPT_4_08K_CHAT_INP_TOKEN_COST,
			"output": GPT_4_08K_CHAT_OUT_TOKEN_COST
		}
	},
	"gpt-4-32k": {

		# This is as of 28 Aug., 23. It may change with newer updates
		"cost": {
			"tokens_per_msg": 3,
			"tokens_per_name": 1,
			"input": GPT_4_32K_CHAT_INP_TOKEN_COST,
			"output": GPT_4_32K_CHAT_OUT_TOKEN_COST
		}
	},
	"gpt-4-32k-0613": {
		"cost": {
			"tokens_per_msg": 3,
			"tokens_per_name": 1,
			"inp_token_cost": GPT_4_32K_CHAT_INP_TOKEN_COST,
			"out_token_cost": GPT_4_32K_CHAT_OUT_TOKEN_COST
		}
	},

	# GPT-3.5-Turbo
	"gpt-3.5-turbo": {

		# This is as of 28 Aug., 23. It may change with newer updates
		"cost": {
			"tokens_per_msg": 3,
			"tokens_per_name": 1,
			"tuning": GPT_3_5_TURBO_FINE_TUNING_TUN_TOKEN_COST,
			"input": GPT_3_5_TURBO_04K_CHAT_INP_TOKEN_COST,
			"output": GPT_3_5_TURBO_04K_CHAT_OUT_TOKEN_COST
		}
	},
	"gpt-3.5-turbo-0613": {
		"cost": {
			"tokens_per_msg": 3,
			"tokens_per_name": 1,
			"tuning": GPT_3_5_TURBO_FINE_TUNING_TUN_TOKEN_COST,
			"input": GPT_3_5_TURBO_04K_CHAT_INP_TOKEN_COST,
			"output": GPT_3_5_TURBO_04K_CHAT_OUT_TOKEN_COST
		}
	},
	"gpt-3.5-turbo-16k": {

		# This is as of 28 Aug., 23. It may change with newer updates
		"cost": {
			"tokens_per_msg": 3,
			"tokens_per_name": 1,
			"tuning": GPT_3_5_TURBO_FINE_TUNING_TUN_TOKEN_COST,
			"input": GPT_3_5_TURBO_16K_CHAT_INP_TOKEN_COST,
			"output": GPT_3_5_TURBO_16K_CHAT_OUT_TOKEN_COST
		}
	},
	"gpt-3.5-turbo-16k-0613": {
		"cost": {
			"tokens_per_msg": 3,
			"tokens_per_name": 1,
			"tuning": GPT_3_5_TURBO_FINE_TUNING_TUN_TOKEN_COST,
			"input": GPT_3_5_TURBO_16K_CHAT_INP_TOKEN_COST,
			"output": GPT_3_5_TURBO_16K_CHAT_OUT_TOKEN_COST
		}
	},

	# ADA-002
	"text-embedding-ada-002": {
		"cost": {
			"embedding": ADA_002_8K_EMBEDDING_TOKEN_COST
		}
	}
}

class OpenAI(object):
	def __init__(self) -> None:
		openai.api_key = os.getenv("OPENAI_API_KEY")

		# GPT4-8K, GPT4-32K, GPT3.5-TURBO-4K, GPT3.5-TURBO-16K, ADA-002-8K
		self.cl100k_encoding: tiktoken.Encoding = tiktoken.get_encoding("cl100k_base")

		# Eh
		self.p50k_encoding : tiktoken.Encoding = tiktoken.get_encoding("p50k_base")
		self.r50k_encoding : tiktoken.Encoding = tiktoken.get_encoding("r50k_base")

		self.prompt_cost   : float = 0.0
		self.responce_cost : float = 0.0

		# All previous messages from all text models.
		# New messages get appended and fed into the
		# next chat completion.
		self.messages: list[str] = []

	def gpt_generate(
		self,
		gpt_model      : str,
		usr_prompt     : str,
		sys_prompt     : str,
		msg_lookback_ct: int=0,
		temperature    : float=0,
		freq_penalty   : float=0,
		pres_penalty   : float=0,
		functions_list : list[dict]=[],
	) -> str:
		"""
		Generate a GPT message given a model

		If `msg_history_ct` is less than or equal to 0, it
		will only use the current user prompt, no history.
		"""

		# Create and append a message to the history
		user_msg: dict = self.create_usr_message(gpt_model, usr_prompt, sys_prompt, "user")
		self.messages.append(user_msg)

		msg_history: list[dict] = self.get_message_history(msg_lookback_ct)

		print(msg_history)
		print()
		for msg in msg_history:
			print(msg)
		print('\n\n')

		#openai.ChatCompletion.create(
		#	model=gpt_model,
		#	messages=msg_history,
		#	top_p=1,
		#	frequency_penalty=freq_penalty
		#	presence_penalty=pres_penalty
		#)


	def create_usr_message(
		self,
		gpt_model    : str,
		gpt_role     : str,
		usr_prompt   : str,
		gpt_name     : str="",
		sys_prompt   : str="",
		temperature  : float=0,
		freq_penalty : float=0,
		pres_penalty : float=0,
		function_list: list[dict]=[],
	) -> dict:
		"""
		If the gpt_role is "assistant", it means it provided its own response
		so there is no system prompt, and it will be ignored.
		Neatly creates, validates, and calculuates the cost
		for the type of prompt it is and model it uses.
		"""

		# Clamp the temperature
		if temperature <= 0:
			temperature = 0
		elif temperature >= 2:
			temperature = 2

		# Clamp the frequency penalty
		if freq_penalty <= 0:
			freq_penalty = 0
		elif freq_penalty >= 2:
			freq_penalty = 2

		# Clamp the presense penalty
		if pres_penalty <= 0:
			pres_penalty = 0
		elif pres_penalty >= 2:
			pres_penalty = 2

		# Cleanup and validate the model
		gpt_model = gpt_model.lower().strip()
		if gpt_model not in list(MODELS.keys()):
			raise ValueError("model must be a one of these:\n{0}".format(list(MODELS.keys())))

		# Cleanup and validate gpt_role
		gpt_role = gpt_role.lower().strip()
		if gpt_role not in ["system", "user", "assistant"]:
			raise ValueError("gpt_role must be either \"system\", \"user\", or \"assistant\"")

		# Determine which type of message we are
		# working with to determine our costs
		msg_type: str = "input"
		if gpt_role == "assistant":
			msg_type = "output"


		# Determine the message cost by getting the message encoding
		# and following the method for token counting outlined in
		# https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb
		# Since we are only tealing with input prompts, only multiple by the input cost.
		gpt_encoding: tiktoken.Encoding = tiktoken.encoding_for_model(gpt_model)
		token_ct = len(gpt_encoding.encode(usr_prompt))
		msg_cost: float = token_ct * MODELS[gpt_model]["cost"][msg_type]

		# Every message follows the format:
		# `<im_start>{role/name}\n{content}<im_end>\n`
		# Without the quotes
		msg_cost += (
			MODELS[gpt_model]["cost"]["tokens_per_msg"] *
			MODELS[gpt_model]["cost"][msg_type]
		)

		# If we provide a name, we need to count those tokens
		# As far as I know, the "name" field is only an input
		if (msg_type == "input") and (len(gpt_name) > 0):
			msg_cost += (
				MODELS[gpt_model]["cost"]["tokens_per_name"] *
				MODELS[gpt_model]["cost"]["input"]
			)

		# Function information is always an input
		# (Note this for later so that you don't end up using too much money)
		if (msg_type == "input") and (len(function_list) > 0):

			# TODO: Validate function dictionaries...

			msg_cost += (
				MODELS[gpt_model]["cost"]["input"]
			)

		# Every assistant reply starts with:
		# `<|start|>assistant<|message|>`
		# Without the quotes
		if msg_type == "output":
			msg_cost += 3 * MODELS[gpt_model]["cost"]["output"] 

		# Create the base message stored in `self.messages`
		message: dict = {
			"gpt_model": gpt_model,
			"gpt_role": gpt_role,
			"msg_type": msg_type,
			"msg_cost": msg_cost,
			"token_ct": token_ct,
			"temperature": temperature,
			"freq_penalty": freq_penalty,
			"pres_penalty": pres_penalty,
			"gpt_msg": {
				"role": gpt_role,
				"name": "",
				"usr_prompt": usr_prompt,
				"sys_prompt": sys_prompt,
				"functions": function_list
			}
		}

		return message

	def get_message_history(
		self,
		msg_lookback_ct: int=0
	) -> list[dict]:
		"""
		Returns the `self.messages` message history formatted for:
		`openai.ChatCompletions.create(messages=get_message_history(...))`
		```
		"""

		messages: list[dict] = self.messages[-msg_lookback_ct:]
		if msg_lookback_ct <= 1:
			messages = self.messages[-1]


		for msg in messages:
			print(msg)
