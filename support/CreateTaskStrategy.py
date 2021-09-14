import sys,time,os
sys.path.append("..") 
import commandStrategy
import readline


class CreateTask(commandStrategy.CommandStrategy):
	"""创建分支任务"""
	__args=["f", "h"]

	
	def __init__(self):
		super(CreateTask, self).__init__()


	def cmd(self, args):
		a = input("\033[32;6mCreate Feature/Hotfix. Please Key[F/H]:")
		b = a.lower();
		for c in self.__args:
			if b == c:
				e = input("\033[32;6mInput task name. demo: tapd-{id}:")
				self.__createBranch(b, e)
				return
		
		self.cmd(a)


	def __createBranch(self, type, name):
		a=time.strftime("%Y%m%d-") + name
		if type == 'f':
			CMD="git checkout develop; git fetch origin develop:develop; git checkout -b feature/%s" % a
			os.system(CMD);
			pass
		if type == 'h':
			CMD="git checkout master; git fetch origin master:master; git checkout -b hotfix/%s" % a
			os.system(CMD);
			pass