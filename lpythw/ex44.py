def water(calons):
    return print(f"{calons} of water are given.")


def pick(numbers):
    return print(f"{numbers} of apples are picked.")


appleCare = {'status': True, 'water': water, 'pick': pick}

appleCare['water'](3)
appleCare['pick'](33)
