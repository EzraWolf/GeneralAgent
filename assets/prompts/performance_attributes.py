
def accurate(intensity: int=1) -> str:
	"""
	Tell the LLM (typically in the system prompt) to be
	accurate given an intensity level between 0 and 2
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


INACCURATE: str = """\

"""

CONSISTENT: str = """\

"""


INCONSISTENT: str = """\

"""

RELIABLE: str = """\

"""

UNRELIABLE: str = """\

"""

BIASED: str = """\

"""

UNBIASED: str = """\

"""
