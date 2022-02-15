#Author: Tom Frisenda
#purpose: to brute force a 3x3 matrix such as android graphical password
import hashlib
import urllib.request
# code works but need to save list and replace every number with -1 , as the git list is based on a 3x3 where lowest num is 1 and higher is 9
# instead replace them with a-i (where a = 1 )
# code will be found apond doing this on pc with more computing power
h = "" # enter hash here
# test = str(urllib.request.urlopen("https://raw.githubusercontent.com/delight-im/AndroidPatternLock/master/OUTPUT.txt").read(), 'utf-8')
f = open ("combos.txt","r")


def crack(password_hash):
	for line in f:
		h2 = hashlib.sha1(bytes(line,'utf-8')).hexdigest()
		print(h2)
		if h2 == h :
			print("the combinaton is:", line)
			return line
	print("no hashes in the list match")

if __name__ == "__main__":
	crack(h)

