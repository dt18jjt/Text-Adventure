Game = True
Class = ""
Weapon1 = ""
Weapon2 = ""
weapon_list = ['1.Machine Gun', '2.Shotgun', '3.Pistol', '4.Sniper Rifle']
class_list=['1.Gunner','2.Ranger','3.Medic','4.Demolition']
Health = 3
Name = "You"
print("Captain Rock:WAKE UP SOLDIER!YOU THINK YOU CAN SLEEP WHILE ON DUTY!")
print(Name,": No sir! Sor-")
print("Captain Rock: Save your apologies if you're still alive after this!")
print("Captain Rock: What is your name?")
Name = input("")
print(Name,":My name is",Name[0],"-")
print("Captain Rock:It doesn't matter what your name is!")
print("Captain Rock:Matter of fact I'll give you a new name. You've got two choices")
print("Captain Rock: Option 1 - 'Bedtime' because you love to sleep so much")
print("Captain Rock: Option 2 - 'Baby' because you probably going to be first to piss themselves")
while Game:
    print("Type 1 for 'Bedtime' or Type 2 for 'Baby'")
    nameChange = int(input(""))
    if nameChange == 1:
        Name = "Bedtime"
        break
    elif nameChange == 2:
        Name = "Baby"
        break
    else:
        continue
print(Name,":........",Name)
print("Captain Rock:Hear that everybody meet our new recruit",Name,"!")
print("Everyone: HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA")
print("Everyone:",Name*6)
print("Captain Rock:Alright shut up this isn't playtime back to positions!")
print("Captain Rock:",Name,"come with me!")
print(Name,":o-okay sir")

