import getopt
import Config
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
		opts, args = getopt.getopt(args, "bc", ["help","co","desc="]);
		allCmd=Config.keyCommand()
		if len(opts) > 0:
			for opt in opts:
				var2=self.__getStrategy(opt, args, allCmd)
				var1 = var1 + var2
			return var1
		var1.append(clientCommand.ClientCommand(Config.git["git"], " ".join(args)))
		return var1


	"""通过解析出来的opt通过配置的cmd 匹配出来  args这个参数，暂时没有想好怎么用？？？"""
	def __getStrategy(self, opt, args, allCmd):
		var1   = opt[0]
		var2   = opt[1]
		s=[]
		for sysCmd in allCmd:
			try:
				sysCmd.command().split("|").index(var1)
				s.append(clientCommand.ClientCommand(sysCmd, var2))
			except Exception as e:
				continue
		return s


	"""执行cmd"""
	def command(self):
		clientCmds = self.__parse()
		for cmd in clientCmds:
			cmd.command()
		pass