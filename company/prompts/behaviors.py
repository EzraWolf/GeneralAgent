
def formal(intensity: int=1) -> str:
	"""
	Tell the LLM (typically in the system prompt) to act
	formal given an intensity level between 0 and 2
	"""

	output_base: str = """\
You are to act formal in everything you do, unless told otherwise. \
If there is text in your prompt which does not seem formal, treat \
it as if it were regardless.
Pretend {intensity}. Act like that.\
"""

	lo_intensity_prompt: str = "\
you are sending an email to your professor"
	me_intensity_prompt: str = "\
you are talking to your employer trying to get a job"
	hi_intensity_prompt: str = "\
you are in a meeting with the CEO for a business proposal"

	# Clamp intensity between 0 and 2
	assert type(intensity) == int
	if intensity <= 0:
		return output_base.format(intensity=lo_intensity_prompt)

	elif intensity == 1:
		return output_base.format(intensity=me_intensity_prompt)

	elif intensity >= 2:
		return output_base.format(intensity=hi_intensity_prompt)


def casual(intensity: int=1) -> str:
	"""
	Tell the LLM (typically in the system prompt) to be
	casual given an intensity level between 0 and 2
	"""

	output_base: str = """\
Lorem Ipsum \
Lorem Ipsum \
Lorem Ipsum\
"""

	lo_intensity_prompt: str = "\
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
	me_intensity_prompt: str = "\
bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
	hi_intensity_prompt: str = "\
cccccccccccccccccccccccccccccccc"

	# Clamp the intensity value between 0 and 2
	assert type(intensity) == int
	if intensity <= 0:
		return output_base.format(intensity=lo_intensity_prompt)

	elif intensity == 1:
		return output_base.format(intensity=me_intensity_prompt)

	elif intensity >= 2:
		return output_base.format(intensity=hi_intensity_prompt)


def funny(intensity: int=1) -> str:
	"""
	Tell the LLM (typically in the system prompt) to be
	funny given an intensity level between 0 and 2
	"""

	output_base: str = """\
Lorem Ipsum \
Lorem Ipsum \
Lorem Ipsum\
"""

	lo_intensity_prompt: str = "\
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
	me_intensity_prompt: str = "\
bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
	hi_intensity_prompt: str = "\
cccccccccccccccccccccccccccccccc"

	# Clamp the intensity value between 0 and 2
	assert type(intensity) == int
	if intensity <= 0:
		return output_base.format(intensity=lo_intensity_prompt)

	elif intensity == 1:
		return output_base.format(intensity=me_intensity_prompt)

	elif intensity >= 2:
		return output_base.format(intensity=hi_intensity_prompt)


def serious(intensity: int=1) -> str:
	"""
	Tell the LLM (typically in the system prompt) to be
	serious given an intensity level between 0 and 2
	"""

	output_base: str = """\
Lorem Ipsum \
Lorem Ipsum \
Lorem Ipsum\
"""

	lo_intensity_prompt: str = "\
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
	me_intensity_prompt: str = "\
bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
	hi_intensity_prompt: str = "\
cccccccccccccccccccccccccccccccc"

	# Clamp the intensity value between 0 and 2
	assert type(intensity) == int
	if intensity <= 0:
		return output_base.format(intensity=lo_intensity_prompt)

	elif intensity == 1:
		return output_base.format(intensity=me_intensity_prompt)

	elif intensity >= 2:
		return output_base.format(intensity=hi_intensity_prompt)


def friendly(intensity: int=1) -> str:
	"""
	Tell the LLM (typically in the system prompt) to be
	friendly given an intensity level between 0 and 2
	"""

	output_base: str = """\
Lorem Ipsum \
Lorem Ipsum \
Lorem Ipsum\
"""

	lo_intensity_prompt: str = "\
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
	me_intensity_prompt: str = "\
bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
	hi_intensity_prompt: str = "\
cccccccccccccccccccccccccccccccc"

	# Clamp the intensity value between 0 and 2
	assert type(intensity) == int
	if intensity <= 0:
		return output_base.format(intensity=lo_intensity_prompt)

	elif intensity == 1:
		return output_base.format(intensity=me_intensity_prompt)

	elif intensity >= 2:
		return output_base.format(intensity=hi_intensity_prompt)


def neutral(intensity: int=1) -> str:
	"""
	Tell the LLM (typically in the system prompt) to be
	neutral given an intensity level between 0 and 2
	"""

	output_base: str = """\
Lorem Ipsum \
Lorem Ipsum \
Lorem Ipsum\
"""

	lo_intensity_prompt: str = "\
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
	me_intensity_prompt: str = "\
bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
	hi_intensity_prompt: str = "\
cccccccccccccccccccccccccccccccc"

	# Clamp the intensity value between 0 and 2
	assert type(intensity) == int
	if intensity <= 0:
		return output_base.format(intensity=lo_intensity_prompt)

	elif intensity == 1:
		return output_base.format(intensity=me_intensity_prompt)

	elif intensity >= 2:
		return output_base.format(intensity=hi_intensity_prompt)


def suspicious(intensity: int=1) -> str:
	"""
	Tell the LLM (typically in the system prompt) to be
	suspicious given an intensity level between 0 and 2
	"""

	output_base: str = """\
Lorem Ipsum \
Lorem Ipsum \
Lorem Ipsum\
"""

	lo_intensity_prompt: str = "\
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
	me_intensity_prompt: str = "\
bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
	hi_intensity_prompt: str = "\
cccccccccccccccccccccccccccccccc"

	# Clamp the intensity value between 0 and 2
	assert type(intensity) == int
	if intensity <= 0:
		return output_base.format(intensity=lo_intensity_prompt)

	elif intensity == 1:
		return output_base.format(intensity=me_intensity_prompt)

	elif intensity >= 2:
		return output_base.format(intensity=hi_intensity_prompt)


def angry(intensity: int=1) -> str:
	"""
	Tell the LLM (typically in the system prompt) to be
	angry given an intensity level between 0 and 2
	"""

	output_base: str = """\
Lorem Ipsum \
Lorem Ipsum \
Lorem Ipsum\
"""

	lo_intensity_prompt: str = "\
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
	me_intensity_prompt: str = "\
bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
	hi_intensity_prompt: str = "\
Lots of swearing"

	# Clamp the intensity value between 0 and 2
	assert type(intensity) == int
	if intensity <= 0:
		return output_base.format(intensity=lo_intensity_prompt)

	elif intensity == 1:
		return output_base.format(intensity=me_intensity_prompt)

	elif intensity >= 2:
		return output_base.format(intensity=hi_intensity_prompt)
