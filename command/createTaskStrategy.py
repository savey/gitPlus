import sys,time,os
from . import commandStrategy

class CreateTask(commandStrategy.AbstractCommandStrategy):
	"""创建分支任务"""
	__args=["f", "h"]

	def __init__(self):
		super(CreateTask, self).__init__()

	def command(self):
		return "-c";


	def cmd(self, args):
		a = input("\033[32;6mCreate Feature/Hotfix. Please Key[F/H]:")
		b = a.lower();
		for c in self.__args:
			if b == c:
				e = input("\033[32;6mInput task name. demo: tapd-{id}:")
				d = input("\033[32;6mInput task desc:\033[0m")
				self.__createBranch(b, e, d)
				return
		
		self.cmd(a)


	def __createBranch(self, type, name, desc):
		a=time.strftime("%Y%m%d-") + name
		CMD=""
		b=""
		if type == 'f':
			b="feature/%s" % a
			CMD="git checkout develop; git fetch origin develop:develop; git checkout -b " + b
			pass
		if type == 'h':
			b="hotfix/%s" % a
			CMD="git checkout master; git fetch origin master:master; git checkout -b " + b
			pass

		os.system(CMD)
		if len(desc) > 0:
			os.system("git config branch.%s.description %s" % (b, desc))


	def useage(self):
		print(self.command() + "\t创建任务、feature/hotfix分支，由具体提示输入即可！")
		pass