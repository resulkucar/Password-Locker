import sys, pyperclip

"""
To use, sudo apt install xclip and pip3 install pyperclip
then run the script with python3 plocker.py [Account Name]
"""

#You can enter your account name followed by the password here
locker = {'email': 'hello123', 'netflix': 'jfdsngj', 'bank': 'kittenl0ver'}

#checks to see if you have the account name as an argument
if len(sys.argv) < 2:
	print('To use: python3 pw.py [account]')
	sys.exit()

#the account name entered is stored into act
act = sys.argv[1] 

#if the account name is in the "Locker" then the password is copied
if act in locker:
	pyperclip.copy(locker[act])
	print(act + ' password is copied to clipboard.')
else:    
	#if the account doesn't exist, user is informed
	print(act+ " not found!")
