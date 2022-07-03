user_names = ['admin', 'klaus', 'leonardo', 'zapp']
for user_name in user_names:
    if user_name.lower() == 'admin':
        print(
            f"Hello {user_name.title()}, would you like to see a status report?")
    else:
        print(f"hello {user_name.title()}, thank you for loggin in again!")
