from . import commandStrategy
import readline,os


class SwitchBranch(commandStrategy.AbstractCommandStrategy):


    def command(self):
        return "--co"

    """
    选择分支、由索引、或者分支名、来切换到对应的分支
    """
    def cmd(self, args):
        var1=super().getAllbrs(args)
        for br in var1:
            print(br.toString())

        a=int(input("\033[31mPlease select You Branch Index:\033[0m"))
        l=len(var1)
        if a > l or a < 1:
            self.cmd(args)
        else:
            b=a-1
            br=var1[b]
            CMD="git checkout %s" % br.branchName
            os.system(CMD)


    def useage(self):
        print(self.command() + "\t切换分支，可以输入具体的索引号！请正确输入哦！")
        pass