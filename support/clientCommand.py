class ClientCommand:
	"""docstring for ClientCommand"""
	__commandStrategy=None
	__args=""

	def __init__(self, strategy, args):
		self.__args = args
		self.__commandStrategy = strategy;


	def command(self):
		return self.__commandStrategy.cmd(self.__args)
		pass
		