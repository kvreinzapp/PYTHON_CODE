rivers = {
    'nile': 'egypt',
    'mississippi': 'us',
    'danube': 'europe'
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through The {country.title()}")

# for river,country in rivers.items():
#     print(river.title())
# for river,country in rivers.items():
#     print(country.title())

for river in rivers.keys():
    print(f"-{river.title()}")
for country in rivers.values():
    print(f"-{country.title()}")
