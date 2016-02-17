from orm import ORM


my_orm = ORM()

while True:
	username = input("Enter your username: ")
	password = input("Enter your password: ")
	if my_orm.get_username(username) and my_orm.get_password(password):
		print(my_orm.welcome(username))
		logged_out = False
		while not logged_out:
			action = input("Would you like to: "
				  	  	   "[1]: Create a new user? "
				  	  	   "[2]: Update your password? "
				  	  	   "[3]: Change your email? "
				  	  	   "[4]: Log out? "
				  	  	   "Type a number. ")
			decision = my_orm.actions(int(action))
			if decision == 1:
				username = input("Enter a username: ")
				password = input("Enter a password: ")
				full_name = input("Enter a full name: ")
				email = input("Enter a email: ")
				new_user = my_orm.add_user(username, password, full_name, email)
				decision = 0
	else:
		print("Invalid Credentials")