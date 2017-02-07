#!/usr/bin/env python

import os, optparse
from _winreg import *

def banner():
	print "#######   Recycle Bin Dump p91    #######"


def sid2user(sid):
	try:
		key = OpenKey(HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows_NT\CurrentVersion\ProfileList"+'\\'+sid)
		(value, type) = QueryValueEx(key, 'ProfileImagePath')
		user = value.split('\\')[-1]
		return user
	except:
		return sid

def returnDir():
	dirs =['C:\\Recycler\\','C:\\Recycled\\','C:\\$Recycle.Bin\\']
	for recycleDir in dirs:
		if os.path.isdir(recycleDir):
			return recycleDir
	return None

def main():
	banner()
	recycleDir = returnDir()
	findRecycled(recycleDir)

if __name__ == '__main__':
	main()