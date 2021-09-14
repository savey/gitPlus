class ParseError(RuntimeError):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(RuntimeError, self).__init__()
		self.arg = arg

	
		