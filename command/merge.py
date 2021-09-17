from . import commandStrategy
from support import parseError
import os

class merge(commandStrategy.AbstractCommandStrategy):

    def command(self):
        return "-m";


    """
    """
    def cmd(self, args):
        var1 = super().getAllbrs(args)
        for br in var1:
            print(br.toString())

        a = int(input("\033[31mPlease select You Branch Index:\033[0m"))
        l = len(var1)
        if a > l or a < 1:
            self.cmd(args)
        else:
            b = a - 1
            br = var1[b]
            CMD = "git merge %s" % br.branchName
            os.system(CMD)


    def useage(self):
        print(self.command() + "\t把某个分支 merge到当前分支！")
        pass