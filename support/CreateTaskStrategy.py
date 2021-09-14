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
		# date=
		if type == 'f':
			CMD="git checkout develop; git fetch origin develop:develop; git checkout -b hotfix/"
			os.system();
			pass

		if type == 'h':
			pass