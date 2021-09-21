from . import commandStrategy, gitCmdStrategy

class Status(commandStrategy.AbstractCommandStrategy):


    def command(self):
        return "-s";

    """
    """
    def cmd(self, args):
        git=gitCmdStrategy.GitCmd()
        git.cmd("status -s")

    def useage(self):
        print(self.command() + "\t查看当前分支状态  M(modified)、A(added)、 D(deleted)")
        pass