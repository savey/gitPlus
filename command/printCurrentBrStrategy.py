import os
from . import commandStrategy

class PrintBr(commandStrategy.CommandStrategy):

    """docstring for GitCmd"""
    def __init__(self):
        super(PrintBr, self).__init__()

    def cmd(self, args):
        super().printAllBr(args)