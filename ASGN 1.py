Game = True
Class = ""
classChange = ""
Decision = ""
Weapon1 = ""
Weapon2 = ""
weapon_list = ['1.Machine Gun', '2.Shotgun', '3.Pistol', '4.Sniper Rifle']
class_list = ['1.Gunner', '2.Ranger', '3.Medic', '4.Demolition']
yes_List = ['YES', 'yes', 'Y', 'Yes', 'y']
no_List = ['NO', 'no', 'No', 'N', 'n']
ammoDict = {"MachineGun": 60, "Shotgun": 20, "Pistol": 40, "Sniper": 10, "Grenade": 3}
damageDict = {"MachineGun": 1, "Shotgun": 1, "Pistol": 1, "Sniper": 1, "Grenade": 1}
Health = 3
Name = "You"
def Choice():
    while Game:
        print("Are you sure? TYPE YES OR NO")
        global Decision
        try:
            Decision = input("")
        except ValueError:
            continue
        if Decision in yes_List:
            break
        elif Decision in no_List:
            classChoice()
        else:
            continue



def classChoice():
    global classChange
    global Class
    while Game:
        print("Type the number of the class you want")
        print(class_list)
        try:
            classChange = int(input(""))
        except ValueError:
            continue
        if classChange == 1:
            print("Gunner specializes in firearms but bad with explosives 'INCREASED DAMAGE'")
            Class = "Gunner"
            Choice()
            break
        elif classChange == 2:
            print("Ranger specializes in sniping but less health'INCREASED ACCURACY")
            Class = "Ranger"
            Choice()
            break
        elif classChange == 3:
            print("Medic can heal themselves at any time but do little damage 'INCREASED HEALTH")
            Class = "Medic"
            Choice()
            break
        elif classChange == 4:
            print("Demolition can carry more bombs but has bad aim 'INCREASED EXPLOSIVES")
            Class = "Demolition"
            Choice()
            break
        else:
            continue


print("Capt.Rock:WAKE UP SOLDIER!YOU THINK YOU CAN SLEEP WHILE ON DUTY!")
print(Name, ": No sir! Sor-")
print("Capt.Rock: Save your apologies if you're still alive after this!")
print("Capt.Rock: What is your name?")
Name = input("")
print(Name, ":My name is", Name[0], "-")
print("Capt.Rock:It doesn't matter what your name is!")
print("Capt.Rock:Matter of fact I'll give you a new name. You've got two choices")
print("Capt.Rock: Option 1 - 'Bedtime' because you love to sleep so much")
print("Capt.Rock: Option 2 - 'Baby' because you probably going to be first to piss themselves")
while Game:
    print("Type 1 for 'Bedtime' or Type 2 for 'Baby'")
    try:
        nameChange = int(input(""))
    except ValueError:
        continue
    if nameChange == 1:
        Name = "Bedtime"
        break
    elif nameChange == 2:
        Name = "Baby"
        break
    else:
        continue
print(Name, ":........", Name)
print("Capt.Rock Rock:Hear that everybody meet our new recruit", Name, "!")
print("Everyone: HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA")
print("Everyone:", Name * 6)
print("Capt.Rock Rock:Alright shut up this isn't playtime back to positions!")
print("Capt.Rock:", Name, "come with me!")
print(Name, ":o-okay sir")
print("Capt.Rock: You've been here for a while now and I'm glad to say your training is done")
print("Capt.Rock: DON'T CELEBRATE NOW! This is only the start, Each solider has their own class")
print("Capt.Rock: A class is a area of expertise and you only have choice of 4")
print("Capt.Rock: You can choose only one. Just like your name type the number of the class you want")
classChoice()

print("Capt.Rock: So you choose", Class, "very well.")
