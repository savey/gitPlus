import sys
sys.path.append("..") 
import commandStrategy
import subprocess
import os


class PrintBr(commandStrategy.CommandStrategy):
	"""docstring for GitCmd"""
	def __init__(self):
		super(PrintBr, self).__init__()


	def cmd(self, args):
		# 去除*号
		var1 = args +  " | git branch | sed -e 's/*/ /' -e 's/ //'"
		var2=super().cmdWithReturn("branch", var1)
		var4=var2.replace(" ", "").split("\n")
		i=1;
		for b in var4:
			if len(b) == 0:
				continue
			#打印desc
			_brdesc = super().cmdWithReturn("config", "branch.%s.description" % b).replace("\n", "")
			_newbr="\033[32;6m[%03d]-%s %s" % (i, b, "##:"+_brdesc if len(_brdesc) > 0 else "")
			i=i+1
			print(_newbr)

		