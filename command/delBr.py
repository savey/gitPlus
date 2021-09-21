from . import commandStrategy
import os

class Del(commandStrategy.AbstractCommandStrategy):

    def command(self):
        return "-d";


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
            CMD = "git checkout master; git br -D  %s" % br.branchName
            os.system(CMD)


    def useage(self):
        print(self.command() + "\删除某个分支、不可用于删除Master分支，若删除Master分支，请用原生的命令！")
        pass