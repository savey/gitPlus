import os
from . import commandStrategy

class GitCmd(commandStrategy.AbstractCommandStrategy):
	"""docstring for GitCmd"""
	def __init__(self):
		super(GitCmd, self).__init__()


	def cmd(self, args):
		os.system('/usr/bin/git %s' % args)
		pass


	def useage(self):
		pass