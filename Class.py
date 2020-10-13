class character:
    name = "Name"
    hp = 100
    mp = 50
    atk = 12
    lvl = 1

characterOne = character()
characterOne.name = "Miki"
characterOne.hp = 150
characterOne.mp = 80
characterOne.atk = 50
characterOne.lvl = 8

characterTwo = character()
characterTwo.name = "yssa"
characterOne.hp = 150
characterOne.mp = 80
characterOne.atk = 55
characterOne.lvl = 10
characterThree = character()


print(characterOne.name, characterOne.hp)
print(characterTwo.name)

print(character.name)

class product:
    id = 1
    name = "name"
    price = 20
    qty = 10

productOne = product()
productOne.id = 3
productOne.name = "milk"
productOne.price = 40
productOne.qty = 3

print(productOne)