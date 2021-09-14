import getopt
import cmdDict
from support import clientCommand


class GtaskContext(object):
	"""docstring for ClassName"""
	__args=[]
	def __init__(self, args):
		self.__args = args


	"""解析前端的参数、找到对应的cmd strategy 组成数组返回"""
	def __parse(self):
		var1=[]
		args = self.__args[1:]
		opts, args = getopt.getopt(args, "bc", ["help=","co"]);
		allCmd=cmdDict.cmd
		if len(opts) > 0:
			for opt in opts:
				var2=self.__getStrategy(opt, args, allCmd)
				var1 = var1 + var2
			return var1

		var1.append(clientCommand.ClientCommand(allCmd["git"], " ".join(args)))
		return var1


	"""通过解析出来的opt通过配置的cmd 匹配出来  args这个参数，暂时没有想好怎么用？？？"""
	def __getStrategy(self, opt, args, allCmd):
		var1   = opt[0]
		var2   = opt[1]
		s=[]
		for var3 in allCmd:
			if var3 == 'git':
				continue
			index = -99
			try:
				index = var3.split("|").index(var1)
			except Exception as e:
				continue
			if index == -99:
				continue
			s.append(clientCommand.ClientCommand(allCmd[var3], var2))
		return s


	"""执行cmd"""
	def command(self):
		clientCmds = self.__parse()
		for cmd in clientCmds:
			cmd.command()
		pass