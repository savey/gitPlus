import os

class CommandStrategy(object):
    """docstring for ClassName"""
    def __init__(self):
        pass

    """注释"""
    def cmd(self, args):
        pass


    def printAllBr(self, args):
        var1 = args + " | git branch | sed -e 's/*/ /' -e 's/ //'"
        var2 = self.__cmdWithReturn("branch", var1)
        var4 = var2.replace(" ", "").split("\n")
        i = 1;
        for b in var4:
            if len(b) == 0:
                continue
            # 打印desc
            _brdesc = self.__cmdWithReturn("config", "branch.%s.description" % b).replace("\n", "")
            _newbr = "\033[32;6m[%03d]-%s %s" % (i, b, "##:" + _brdesc if len(_brdesc) > 0 else "")
            i = i + 1
            print(_newbr)


    def __cmdWithReturn(self, opt, args):
        shellOpt='/usr/bin/git %s %s' % (opt, args)
        p=os.popen(shellOpt)
        r=p.read()
        p.close()
        return r;