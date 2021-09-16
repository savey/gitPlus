from . import commandStrategy

class PrintBr(commandStrategy.AbstractCommandStrategy):


    def command(self):
        return "-b"


    def cmd(self, args):
        super().printAllBr(args)


    def useage(self):
        print(self.command() + "\t打印出当前所有分支，列表出索引号和描述")
        pass