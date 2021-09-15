from . import commandStrategy
from support import parseError
import os

class EditBrDesc(commandStrategy.AbstractCommandStrategy):


    def cmd(self, args):
        if len(args) <= 0:
            raise parseError.ParseError("请输入分支的描述")
        #CMD
        CMD="git config branch.%s.description %s" % (super().showCurrentBr().replace("\n", ""), args.replace("\n",""))
        os.system(CMD)
        print("✅Success!!")
        pass


    def useage(self, args):
        print(args + "\t为当前分支打上描述、--desc=<description> or --desc <description>")
        pass