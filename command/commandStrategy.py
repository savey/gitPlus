import os
from abc import abstractmethod, ABCMeta
from support import breancEntity

class AbstractCommandStrategy(object):
    __meta_class__ = ABCMeta


    def __init__(self):
        pass


    """
    存入指令的实现方法
    """
    @abstractmethod
    def command(self):
        pass


    """
    每种命令的说明
    """
    @abstractmethod
    def useage(self):
        pass

    """注释"""
    @abstractmethod
    def cmd(self, args):
        pass


    def printAllBr(self, args):
        allBr=self.getAllbrs(args)
        for br in allBr:
            print(br.toString())

    """
    把所有的分支组成数组对象
    """
    def getAllbrs(self, args):
        var1 = args + " | git branch | sed -e 's/*/ /' -e 's/ //'"
        var2 = self.cmdWithReturn("branch", var1)
        var4 = var2.replace(" ", "").split("\n")
        i = 1;
        var5 = []
        for b in var4:
            if len(b) == 0:
                continue
            # 打印desc
            _brdesc = self.cmdWithReturn("config", "branch.%s.description" % b).replace("\n", "")
            i = i + 1
            var5.append(breancEntity.BrEntity(i - 1, b, _brdesc))

        return var5

    """
    获取当前分支的名字
    """
    def showCurrentBr(self):
        return self.cmdWithReturn("branch", "--show-current")



    def cmdWithReturn(self, opt, args):
        shellOpt='/usr/bin/git %s %s' % (opt, args)
        p=os.popen(shellOpt)
        r=p.read()
        p.close()
        return r;