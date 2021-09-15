from command import printCurrentBrStrategy,gtaskHelp,createTaskStrategy,switchBranch,gitCmdStrategy,editBrDesc

"""
	这里配置下指令对应的命令解释器
"""
cmd = {
	"-b": printCurrentBrStrategy.PrintBr(),
	"--help": gtaskHelp.GtaskHelper(),
	"-c":createTaskStrategy.CreateTask(),
    "--co":switchBranch.SwitchBranch(),
	"--desc":editBrDesc.EditBrDesc()
}

"""
特殊的配置，解析git的命令
"""
git = {
    "git": gitCmdStrategy.GitCmd()
}