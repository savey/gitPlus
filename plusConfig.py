from command import printCurrentBrStrategy,gtaskHelp,createTaskStrategy,switchBranch,gitCmdStrategy,editBrDesc, \
	merge, status, delBr

"""  定义整个plusGit支持的长短选项、 ==STRT=="""
shortOpts="bcmsd"
longOpts=["help","co","desc="]
""" ===============================END==== """

"""
	这里配置下指令对应的命令解释器
"""
def keyCommand():
		yield printCurrentBrStrategy.PrintBr()
		yield gtaskHelp.GtaskHelper()
		yield createTaskStrategy.CreateTask()
		yield switchBranch.SwitchBranch()
		yield editBrDesc.EditBrDesc()
		yield merge.Merge()
		yield status.Status()
		yield delBr.Del()


"""
特殊的配置，解析git的命令
"""
git = {
    "git": gitCmdStrategy.GitCmd()
}
