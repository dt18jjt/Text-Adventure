Game = True
combatAction = ""
baseAction = ""
Class = ""
classChange = ""
Weapon = ""
Health = 3
turnCounter = 0
shoot_List = ['Shoot', 'shoot', 'shot', 'fire', 'SHOOT', 'S', 's']
equip_List = ['Equip', 'equip', 'EQUIP', 'E', 'e']
help_List = ['Help', 'help', 'HELP', 'H', 'h']
IntroAction_List = ['Shoot(s)', 'Equip(e)', 'Help(h)']
WepEquip_List = ['1.Machine Gun', '2.Shotgun', '3.Pistol', '4.Sniper Rifle', '5.Unequip']
weapon_List = ['Machine Gun', 'Shotgun', 'Pistol', 'Sniper Rifle']
class_List = ['1.Gunner', '2.Ranger', '3.Medic', '4.Demolition']
ammoDict = {"MachineGun": 10, "Shotgun": 4, "Pistol": 15, "Sniper": 2, "Grenade": 3}
damageDict = {"MachineGun": 1, "Shotgun": 1, "Pistol": 1, "Sniper": 1, "Grenade": 1}


def introCombat():
    global combatAction
    global turnCounter
    while turnCounter < 5:
        print("What will you do?")
        try:
            combatAction = input("")
        except ValueError:
            continue
        if combatAction in equip_List:
            equip()
            turnCounter += 1
            continue
        elif combatAction in shoot_List:
            if Weapon in weapon_List:
                print("You fire your", Weapon)
                print("Missed")
                turnCounter += 1
                continue
            else:
                print("You don't have a weapon equipped!")
                turnCounter += 1
                continue
        elif combatAction in help_List:
            print(IntroAction_List)
            continue
        if turnCounter >= 5:
            break



def equip():
    global Weapon
    weaponchoice = 0
    while Game:
        print(WepEquip_List)
        print("Type the number.")
        try:
            weaponchoice = int(input(""))
        except ValueError:
            continue
        if weaponchoice == 1:
            Weapon = "Machine Gun"
            break
        elif weaponchoice == 2:
            Weapon = "Shotgun"
            break
        elif weaponchoice == 3:
            Weapon = "Pistol"
            break
        elif weaponchoice == 4:
            Weapon = "Sniper Rifle"
            break
        elif weaponchoice == 5:
            Weapon = ""
            break
        else:
            continue
