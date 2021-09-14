from command import createTaskStrategy, gitCmdStrategy, printCurrentBrStrategy, gtaskHelp

"""
	这里配置下指令对应的命令解释器/目前只支持短标签 …………
"""
cmd = {
	"git": gitCmdStrategy.GitCmd(),
	"-b": printCurrentBrStrategy.PrintBr(),
	"--help": gtaskHelp.GtaskHelper(),
	"-c": createTaskStrategy.CreateTask()
}