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