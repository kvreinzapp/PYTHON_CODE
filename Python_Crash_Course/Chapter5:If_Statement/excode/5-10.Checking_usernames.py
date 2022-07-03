current_users = ['admin', 'klaus', 'leoNARDO', 'zack', 'Chain']
current_users_lower = [user.lower() for user in current_users]

new_users = ['Gilbert', 'KK', 'Steven', 'KLAUS', 'leonardo']
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user.title()} is occupied, enter a new username")
    else:
        print(f'{new_user} is available')

print(new_users)
