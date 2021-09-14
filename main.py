#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys
import gtaskContext
import getopt
from support import parseError

if __name__ == '__main__':
	gtc = gtaskContext.GtaskContext(sys.argv)
	gtc.command()
	pass
	# try:
	# 	gtc = gtaskContext.GtaskContext(sys.argv)
	# 	gtc.command()
	# 	pass
	# except getopt.GetoptError as e:
	# 	print(e.args,e.line)
	# except Exception as e:
	# 	print(e)
	# except ParseError as e:
	# 	print(e.args)