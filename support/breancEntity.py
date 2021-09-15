class BrEntity:
    """docstring for ClientCommand"""
    __branchName = ""
    __index = 0
    __desc = ""


    def __init__(self, a, b, c):
        self.__index = a
        self.__branchName = b;
        self.__desc = c;

    @property
    def index(self):
        return self.__index

    @property
    def branchName(self):
        return self.__branchName

    @property
    def desc(self):
        return self.__desc

    #打印成分支格式
    def toString(self):
        return "\033[32;6m[%03d] - %s\033[0m %s" % (self.index, self.branchName, "##" + self.desc if len(self.desc) > 0 else "")