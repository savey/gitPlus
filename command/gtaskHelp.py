from . import commandStrategy
import Config

class GtaskHelper(commandStrategy.AbstractCommandStrategy):


    def command(self):
        return "--help"


    def cmd(self, args):
        self.useage()
        pass


    def useage(self):
        var1 = Config.keyCommand()
        print("usage:")
        for a in var1:
            # #跳过本类，防止死掉了、~
            if a.__class__ == __class__:
                continue
            a.useage()
        print("祝你工作愉快！🥂🥂")
        pass
		