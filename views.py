from orm import ORM


my_orm = ORM()

while True:
	username = input("Enter your username: ")
	password = input("Enter your password: ")
	if my_orm.check_credentials(username, password):
		print(my_orm.welcome(username))
	else:
		print("Invalid Credentials")


	x	action = input("Would you like to: "
			  	  	   "[1]: Create a new user? "
			  	  	   "[2]: Update your password? "
			  	  	   "[3]: Change your email? "
			  	  	   "[4]: Log out? "
			  	  	   "Type a number. ")