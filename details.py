import getpass
def enterDetails():
	print("-----------------------------Enter Your Details-----------------------------\n")
	print ("First Name: ",end="")
	First_Name=input()
	print("Last Name: ",end="")
	Last_Name=input()
	'''print("DateOfBirth: ",end="")
	DateOfBirth=input()
	print("Address: ",end="")
	Address=input()
	print("Mobile Number: ",end="")
	Mobile=input()
	print("Email Address: ",end="")
	Email=input()'''
	print("-----------------------------Set Your Account-----------------------------\n")
	print("Your user name :" +First_Name +" "+ Last_Name  )
	print("Set Your Login ID: ")
	login_id=input()
	#print("Set Your PASSWORD:")
	password=getpass.getpass("Set Your PASSWORD:")
	#print(password)
enterDetails()	
