import os
from . import commandStrategy

class PrintBr(commandStrategy.AbstractCommandStrategy):

    """docstring for GitCmd"""
    def __init__(self):
        super(PrintBr, self).__init__()

    def cmd(self, args):
        super().printAllBr(args)


    def useage(self, args):
        print(args)
        pass