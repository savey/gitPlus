#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys,signal
import gtaskContext
import getopt
from support import parseError
	

def shutDown(signum, frame):
  	print("\nGood Bay!!")
  	exit()


signal.signal(signal.SIGINT, shutDown)



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