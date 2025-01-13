from ex50 import Person


def test_combat():
    boxer = Person("Boxer", 100, 10)
    zombie = Person("Zed", 1000, 1000)

    assert boxer.hp == 100, "Boxer has wrong hp"
    assert zombie.hp == 1000, "Zombie has wrong hp"

    boxer.hit(zombie)
    assert zombie.alive()

    zombie.hit(boxer)
    assert not boxer.alive()
