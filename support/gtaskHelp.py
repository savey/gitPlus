import sys
import os
sys.path.append("..") 
import commandStrategy

class GtaskHelper(commandStrategy.CommandStrategy):
	"""docstring for GitCmd"""
	def __init__(self):
		super(GtaskHelper, self).__init__()


	def cmd(self, args):
		br = os.system('/usr/bin/git branch')
		
		pass
		