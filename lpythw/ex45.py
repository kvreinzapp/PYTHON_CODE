class Person(object):

    def __init__(self, name, age, eyes):
        self.name = name
        self.age = age
        self.eyes = eyes

    def talk(self, words):
        print(f"I am {self.name} and {words}")


becky = Person("Becky", 39, "green")
print(">>>This is Person.__class__")
print(Person.__class__)
print(">>>This is Person.__dict__")
print(Person.__dict__)
print(">>>This is Person.__class__.__dict__")
print(Person.__dict__.__class__)
print(">>>This is Person.__dict__.__class__")
print(Person.__class__.__dict__)

print(">>>This is becky.__class__")
print(becky.__class__)
print(">>>This is becky.__dict__")
print(becky.__dict__)
print(">>>This is becky.__class__.__dict__")
print(becky.__class__.__dict__)
print(">>>This is becky.__dict__.__class__")
print(becky.__dict__.__class__)

print("This is dir(becky)")
print(dir(becky))

print("This is becky.talk")
print(becky.talk)
print("This is getattr(becky, 'talk')")
print(getattr(becky, 'talk'))
print("This is becky.__class__.dict__('talk')")
print(becky.__class__.__dict__['talk'])
