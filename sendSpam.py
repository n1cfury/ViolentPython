import smtplib

user = 'username'
pwd = 'password'
msg =MIMEText(text)
msg['From'] = user
msg['To'] = to
msg['subject'] = subject

def banner():
	print "[***]	Anon-mail p238		[***]"

def sendMail(user, pwd, to, subject, text):
	try:
		smtpServer = smtplib.SMTP('smtp.gmail.com', 587)
		print "[+] Connecting to Mail Server."
		smtpServer.ehlo()
		print "[+] Starting Encrypted Session."
		smtpServer.starttls()
		smtpServer.ehlo()
		print "[+] Logging Into Mail Server."
		smtpServer.login(user, pwd)
		print "[+] Sending Mail."
		smtpServer.sendmail(user, to, msg.as_string())
		smtpServer.close()
		print "[+] Mail Sent Successfully."
	except:
		print "[-] Sending Mail failed."

def main():
	banner()
	sendMail(user, pwd, '<target email address>', 'Re: Important', 'Test Message')

if __name__ == '__main__':
	main()