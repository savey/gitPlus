import os
from abc import abstractmethod, ABCMeta
from support import breancEntity

class AbstractCommandStrategy(object):
    __meta_class__ = ABCMeta


    def __init__(self):
        pass

    """
    每种命令的说明
    """
    @abstractmethod
    def useage(self):
        pass

    """注释"""
    def cmd(self, args):
        pass


    def printAllBr(self, args):
        allBr=self.getAllbrs(args)
        for br in allBr:
            print("\033[32;6m[%03d]-%s ##%s" % (br.index, br.branchName, br.desc))

    """
    把所有的分支组成数组对象
    """
    def getAllbrs(self, args):
        var1 = args + " | git branch | sed -e 's/*/ /' -e 's/ //'"
        var2 = self.__cmdWithReturn("branch", var1)
        var4 = var2.replace(" ", "").split("\n")
        i = 1;
        var5 = []
        for b in var4:
            if len(b) == 0:
                continue
            # 打印desc
            _brdesc = self.__cmdWithReturn("config", "branch.%s.description" % b).replace("\n", "")
            i = i + 1
            var5.append(breancEntity.BrEntity(i - 1, b, _brdesc))

        return var5

    def __cmdWithReturn(self, opt, args):
        shellOpt='/usr/bin/git %s %s' % (opt, args)
        p=os.popen(shellOpt)
        r=p.read()
        p.close()
        return r;