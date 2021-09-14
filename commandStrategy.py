import os
class CommandStrategy(object):
	"""docstring for ClassName"""
	def __init__(self):
		pass

	def cmd(self, args):
		return os.system('/usr/bin/git %s' % args)



	def cmdWithReturn(self, opt, args):
		shellOpt='/usr/bin/git %s %s' % (opt, args)
		p=os.popen(shellOpt)
		r=p.read()
		p.close()
		return r;