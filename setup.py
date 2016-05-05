import sys
try:
	import mechanize
	import bs4
except:
	print "mechanize and bs4 must be installed.  \n"
	"--- pip install mechanize\n"
	"--- pip install bs4"
	sys.exit()

print "Welcome to the Python Facebook Bot!"
print "To use this program, you will need a Facebook account that does NOT have \n" \
		"two-factor authentication enabled.  \n" \
		"To start out, you will need to enter your Facebook-connected email address \n" \
		"along with the password associated with it.  Don't worry, I promise there's \n" \
		"no way for me to find out your password.  You'll also need to enter the name of \n" \
		"the chat conversation this bot is going to be connected to.  Basically, if \n" \
		"it's a group conversation, then you gotta put the full name of that \n" \
		"conversation that you see on Facebook.  If it's an individual person, then \n" \
		"their name (as it appears on Facebook) is what you need to enter\n\n" \

email = raw_input("----Enter your Email Address: ")
print "\n"
password = raw_input("----Enter your password: ")
print "\n"
chatname = raw_input("----Enter the chat name: ")
print "\n"
confirm = raw_input("To confirm, type y if the following is correct: \n"\
		"Email: " + email + "\nPassword: " + password + "\nChatname: " + chatname + "\n[y/n]:")
print "\n"
if confirm != 'y':
	print "Exiting"
	sys.exit()

with open('config','wb') as f:
	f.write('email="' + email + '"\n')
	f.write('password="' + password + '"\n')
	f.write('chatName="' + chatname + '"\n')

print "you're all set up now!  run `python fb.py` to get started!"


