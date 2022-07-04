favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

guys = ['jen', 'edward', 'klaus', 'leonardo']

for guy in guys:
    if guy in favorite_languages.keys():
        print(f"{guy.title()}, thank you for responding")
    else:
        print(f"{guy.title()}, Please take the poll")
