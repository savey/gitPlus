from . import commandStrategy
import cmdDict

class GtaskHelper(commandStrategy.AbstractCommandStrategy):
	"""docstring for GitCmd"""
	def __init__(self):
		super(GtaskHelper, self).__init__()


	def cmd(self, args):
		self.useage(args)
		pass


	def useage(self, args):
		var1=cmdDict.cmd
		print("usage:")
		for a in var1:
			d=var1[a]
			# #跳过本类，防止死掉了、~
			if d.__class__ == __class__:
				continue
			d.useage(a)
		print("祝你工作愉快！🥂🥂")
		pass
		