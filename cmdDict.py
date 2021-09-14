from support import gitCmdStrategy,printCurrentBrStrategy,gtaskHelp

cmd = {
	"git": gitCmdStrategy.GitCmd(),
	"-b|branch": printCurrentBrStrategy.PrintBr(),
	"--help": gtaskHelp.GtaskHelper()
}