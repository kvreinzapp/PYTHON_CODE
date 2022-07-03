# user_names = ['admin', 'klaus', 'leo', 'zack']
user_names = []
if user_names:
    for user_name in user_names:
        if user_name.lower() == 'admin':
            print(
                f"Hello {user_name.title()}, would you like to see a status report?")
        else:
            print(f"hello {user_name.title()}, thank you for loggin in again!")
else:
    print("We need to find some users!")
