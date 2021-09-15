class ParseError(RuntimeError):
	"""docstring for ClassName"""
	def __init__(self, arg):
		self.arg = arg

	def __str__(self):
		return self.arg
		