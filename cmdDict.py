from support import gitCmdStrategy,printCurrentBrStrategy,gtaskHelp,createTaskStrategy


"""
	这里配置下指令对应的命令解释器
"""
cmd = {
	"git": gitCmdStrategy.GitCmd(),
	"-b|branch": printCurrentBrStrategy.PrintBr(),
	"--help": gtaskHelp.GtaskHelper(),
	"-c":createTaskStrategy.CreateTask()
}