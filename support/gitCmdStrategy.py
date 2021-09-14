import sys
import os
sys.path.append("..") 
import commandStrategy

class GitCmd(commandStrategy.CommandStrategy):
	"""docstring for GitCmd"""
	def __init__(self):
		super(GitCmd, self).__init__()


	def cmd(self, args):
		os.system('/usr/bin/git %s' % args)
		pass
		