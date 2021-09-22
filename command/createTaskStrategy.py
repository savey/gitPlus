import sys,time,os
from . import commandStrategy

class CreateTask(commandStrategy.AbstractCommandStrategy):
	"""创建分支任务"""
	__args=["f", "h", "n"]

	def __init__(self):
		super(CreateTask, self).__init__()

	def command(self):
		return "-c";


	def cmd(self, args):
		a = input("\033[32;6mCreate Feature/Hotfix/Normal. Please Key[F/H/N]:")
		b = a.lower();
		for c in self.__args:
			if b == c:
				e = input("\033[32;6mInput task name:")
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
			CMD="git checkout develop; git fetch origin develop:develop -u; git checkout -b " + b
			pass
		if type == 'h':
			b="hotfix/%s" % a
			CMD="git checkout master; git fetch origin master:master -u; git checkout -b " + b
			pass
		if type == "n":
			CMD="git checkout -b " + a
			pass
		os.system(CMD)
		if len(desc) > 0:
			os.system("git config branch.%s.description %s" % (b, desc))


	def useage(self):
		print(self.command() + "\t创建feature/hotfix/普通分支，分别基于(develop/master/当前分支)创建！由具体提示输入即可！")
		pass