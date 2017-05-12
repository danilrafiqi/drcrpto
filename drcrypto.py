#Script By Muhamad Danil Rafiqi
import base64
print "===================================="
print "            DRCryptopy v.1           "
print "            Copyright by            " 
print " Muhamad Danil Rafiqi a.k.a DRCyber "
print "   http://rafibanget.blogspot.com   "
print "===================================="

def hexencode():
	a=raw_input("Input Text Here : ")
	print a.encode("hex")

def base64encode():
	a=raw_input("Input Text Here : ")
	print base64.b64encode(a)

def base32encode():
	a=raw_input("Input Text Here : ")
	print base64.b32encode(a)

def hexdecode():
	a=raw_input("Input Text Here : ")
	print a.decode("hex")

def base64decode():
	a=raw_input("Input Text Here : ")
	print base64.b64decode(a)

def base32decode():
	a=raw_input("Input Text Here : ")
	print base64.b32decode(a)

def menucode():
	print "1. Hex\n2. Base64\n3. Base32"

print "1. Encode/Encrypt\n2. Decode/Decrypt"


pilih=input("Input here : ")
if pilih==1:
	menucode()
	pilih2=input("Input Here : ")
	if pilih2==1:
		hexencode()
	elif pilih2==2:
		base64encode()
	else:
		base32encode()

else :
	menucode()
	pilih2=input("Input Here : ")
	if pilih2==1:
		hexdecode()
	elif pilih2==2:
		base64decode()
	else:
		base32decode()
	


