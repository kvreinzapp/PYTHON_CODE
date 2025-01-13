try:
    count = int("Hello")
except ValueError:
    print("Bad number given")

try:
    assert 1 == 2
except Exception as what:
    print("assert throws", type(what))
