               ____ ____ __ __   ___   __   __              __
              / __// __// // /  / _ | / /_ / /_ ___ _ ____ / /__ ___  ____
             _\ \ _\ \ / _  /  / _  |/ __// __// _ `// __//  '_// -_)/ __/
            /___//___//_//_/  /_/ |_|\__/ \__/ \_,_/ \__//_/\_\ \__//_/   

 #-----------------------------------------------------------------------------------#
 # Script: sshattacker.py                                                            #
 # Language: Python 3.5.1 (v3.5.1:37a07cee5969) (https://www.python.org/downloads/)  #
 # Dependencies: (1) Paramiko 1.16.0 (www.paramiko.org/installing.html)              #
 # Written by: forScience (james@4a57.xyz)                                           #
 # MD5 checksum: 379e8eeba061fa0a2f02f092e198d9b9                                    #
 #-----------------------------------------------------------------------------------#


 sshattacker.py is a simple (and loud) command line application for conducting 
 dictionary attacks against insecure SSH servers. 
 This script has been written to provide proof of concept for attacking login 
 credentials of insecure SSH servers.

     *This script should only be used for educational purposes, within the law.*


	Installation:
	
		Get python 3.5:  https://www.python.org/downloads/
		Install pip3:  https://pip.pypa.io/en/latest/installing/
		 
  		Install paramiko module:  $ pip3 install paramiko


Usage:

The script is written in Python 3.5.1; therefore, it requires the python3 interpreter to run. 
The script can be run (with Python 3 and Paramiko installed) by navigating to the directory where
it is located and entering the following command into the terminal:


python3 sshattacker.py


This will run the script in the context of the python3 interpreter. 
The script will then print the following to stdout:


 [+] SSH Dictionary Attacker
 [!] No permission is given for the unlawful use of this script

>> Input target host address (IP or hostname):


The first 3 lines provide information about the script. Standard information printed by the 
script is prepended with [+]. Other information printed by the script may be prepended with 
[!] to signify a need for special attention by the user. [-] is also used to identify printed 
text as part of an ongoing action by the script. At this stage the script will wait for entry 
of the target IP or hostname before continuing.


 >> Input target host address (IP or hostname): 192.168.1.139
 >> Input target port (leave blank for default):


It is important to note that validation of the IP/hostname does not occur at this stage. 
Once an IP has been entered the script will the request entry of the port number. 
This functionality is to allow for the attacking of an SSH server listening on a non-standard port. 
If no port number is entered, the script will default to the standard SSH port number 22.


 >> Input target port (leave blank for default): 22
 >> Input SSH username:


Once a port number has been entered, the script will the request a singular SSH username. 
The script (in its current form) does not accept list files containing usernames.


 >> Input SSH username: bob
 >> Input path to password list (one password per line):


An absolute path must be entered for the password list. The password list should be a plain text file containing 
one password per line (standard wordlist format). The script attempts logins using each password on each line of 
the file. The script validates the path to the file and checks that the file can be read.


 >> Input path to password list (one password per line): /home/User/password.list
 [-] Attempt 1: password ... Unsuccessful
 [-] Attempt 2: wordpass ... Unsuccessful
 [-] Attempt 3: batman ... Unsuccessful
 [-] Attempt 4: cookiemonster ... Unsuccessful
 [-] Attempt 5: acidburn ... Unsuccessful
		      .
		      .


Once the password file path has been entered the script will immediately begin to attempt SSH logins using 
the passwords contained in the file. Each attempt number and password will be printed to stdout. 
This process can take some time and it will continue until the password file has been exhausted or a 
login is successful. The script can be terminated at any time with a keyboard interrupt (ctrl+c).


		      .
		      .
 [-] Attempt 6: love ... Unsuccessful
 [-] Attempt 7: 4dm1n ... Unsuccessful
 [-] Attempt 8: secret ... Unsuccessful
 [-] Attempt 9: ilovemykitty ... Unsuccessful
 [-] Attempt 10: 12345678 ... Unsuccessful
 [-] Attempt 11: t0t4ln00b ... Unsuccessful
 [-] Attempt 12: supersecretpassword ... Bingo!

 [!] SUCCESS! Creds: bob@192.168.1.139:22 Password: supersecretpassword

 computer:~ User$ 


In the event that the password is found, login attempts will cease and the successful credentials will be 
printed to the screen. At this point the SSH session is closed. These credentials can then be used to login 
via any normal SSH client.


		      .
		      .
 [+] Unsuccessful, Password list exhausted
 [!] Check username and/or use a larger password list

 [+] Exiting...

 computer:~ User$


In the event that the password list is exhausted before an attack is successful, a notification will be printed to 
the screen. The script will automatically close all SSH sessions and exit the script. This can occur if the 
password file is not comprehensive enough, or the SSH username does not exist or has been entered incorrectly.

