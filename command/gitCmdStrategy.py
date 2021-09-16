import os
from . import commandStrategy

class GitCmd(commandStrategy.AbstractCommandStrategy):

    def command(self):
        return "git"

    def cmd(self, args):
        os.system('/usr/bin/git %s' % args)

    def useage(self):
        pass