import random
Game = True
combatAction = ""
baseAction = ""
Class = ""
classChange = ""
Weapon = ""
enemyName = "" # string varible for title of the enemies
Accuracy = 0
EnemyDistance = 1
Health = 3
turnCounter = 0
Troops = 20
TroopsWounded = 0
TroopsDead = 0
EnemyTroops = 0
EnemyWounded = 0
EnemyKilled = 0
shoot_List = ['Shoot', 'shoot', 'shot', 'fire', 'SHOOT', 'S', 's']
equip_List = ['Equip', 'equip', 'EQUIP', 'E', 'e']
aim_List = ['Aim', 'aim', 'AIM', 'A', 'a']
cover_List = ['Cover', 'cover', 'COVER', 'C', 'c']
medkit_List = ['Medkit', 'medkit', 'MEDKIT', 'M', 'm']
go_List = ['Go', 'go', 'GO', 'G', 'g']
help_List = ['Help', 'help', 'HELP', 'H', 'h']
introAction_List = ['Shoot(s)', 'Equip(e)', 'Help(h)']
combatAction_List = ['Shoot(s)', 'Equip(e)', 'Aim(a)' 'Cover(c)', 'Medkit(m)', 'Go(g)', 'Help(h)']
WepEquip_List = ['1.Machine Gun', '2.Shotgun', '3.Pistol', '4.Sniper Rifle', '5.Unequip']
weapon_List = ['Machine Gun', 'Shotgun', 'Pistol', 'Sniper Rifle']
class_List = ['1.Gunner', '2.Ranger', '3.Medic']
distance_List = ['Close','Mid','Far']
accuracy_List = ['0%','25%','50%','75%','100%']
ammoDict = {"MachineGun": 8, "Shotgun": 2, "Pistol": 10, "Sniper": 1}
damageDict = {"MachineGun": 1, "Shotgun": 2, "Pistol": 1, "Sniper": 3}


def introCombat():
    global combatAction
    global turnCounter
    while turnCounter < 5:
        print("What will you do?")
        print(introAction_List)
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
            print("TYPE 'Equip or e' TO EQUIP A WEAPON.")
            print("TYPE 'Shoot or s' TO FIRE YOUR WEAPON")
            print("TYPE 'Help or h' IF YOU FORGET THE COMMANDS YOU CAN TYPE")
            continue
        if turnCounter >= 5:
            break

def playerTurn():
    global combatAction
    global Troops
    global EnemyTroops
    global enemyName
    EnemyTroops = random.randrange(10,15,1)
    print("Team Bravo has encountered the ",enemyName)
    while Troops > 0 or EnemyTroops > 0:
        print("What will you do?")
        print(combatAction_List)
        try:
            combatAction = input("")
        except ValueError:
            continue
        if combatAction in equip_List:
            equip()
            enemyShoot()
            continue
        elif combatAction in shoot_List:
            if Weapon in weapon_List:
                shoot()
                enemyShoot()
                continue
            else:
                print("You don't have a weapon equipped!")
                enemyShoot()
                continue
        elif combatAction in aim_List:
            aim()
        elif combatAction in help_List:
            help()
            continue
        if Troops <= 0 :
            print("All Soldiers are dead, Mission Failure")
        elif EnemyTroops <= 0:
            print("Enemies Neutralized")
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
        else:
            continue

def help():
    print("TYPE 'Equip or e' TO EQUIP A WEAPON.")
    print("TYPE 'Shoot or s' TO FIRE YOUR WEAPON")
    print("Type 'Aim' or a' to see your chance of hitting a enemy")
    print("Type 'Medkit or m' to heal a teamate")
    print("Type 'Cover or c' to get behind cover")
    print("Type 'Go or g' to move location")
    print("TYPE 'Help or h' IF YOU FORGET THE COMMANDS YOU CAN TYPE")

def accuracyPercentChange():
    global Accuracy
    global AccuracyString
    global EnemyDistance
    global DistanceString
    global Weapon
    global Class

    # Gunner and Medic Accuracy
    # Machine gun
    if EnemyDistance == 0 and Class == "Gunner" or Class == "Medic" and Weapon == "Machine Gun":
        Accuracy = 2
    elif EnemyDistance == 1 and Class == "Gunner" or Class == "Medic" and Weapon == "Machine Gun":
        Accuracy = 2
    elif EnemyDistance == 2 and Class == "Gunner" or Class == "Medic" and Weapon == "Machine Gun":
        Accuracy = 1
    # Shotgun
    elif EnemyDistance == 0 and Class == "Gunner" or Class == "Medic" and Weapon == "Shotgun":
        Accuracy = 3
    elif EnemyDistance == 1 and Class == "Gunner" or Class == "Medic" and Weapon == "Shotgun":
        Accuracy = 1
    elif EnemyDistance == 2 and Class == "Gunner" or Class == "Medic" and Weapon == "Shotgun":
        Accuracy = 0
    # Pistol
    elif EnemyDistance == 0 and Class == "Gunner" or Class == "Medic" and Weapon == "Pistol":
        Accuracy = 3
    elif EnemyDistance == 1 and Class == "Gunner" or Class == "Medic" and Weapon == "Pistol":
        Accuracy = 2
    elif EnemyDistance == 2 and Class == "Gunner" or Class == "Medic" and Weapon == "Pistol":
        Accuracy = 1
    # Sniper Rifle
    elif EnemyDistance == 0 and Class == "Gunner" or Class == "Medic" and Weapon == "Sniper Rifle":
        Accuracy = 0
    elif EnemyDistance == 1 and Class == "Gunner" or Class == "Medic" and Weapon == "Sniper Rifle":
        Accuracy = 2
    elif EnemyDistance == 2 and Class == "Gunner" or Class == "Medic" and Weapon == "Sniper Rifle":
        Accuracy = 3
    # Ranger Accuracy
    # Machine gun
    if EnemyDistance == 0 and Class == "Ranger" and Weapon == "Machine Gun":
        Accuracy = 3
    elif EnemyDistance == 1 and Class == "Ranger" and Weapon == "Machine Gun":
        Accuracy = 3
    elif EnemyDistance == 2 and Class == "Ranger" and Weapon == "Machine Gun":
        Accuracy = 2
    # Shotgun
    elif EnemyDistance == 0 and Class == "Ranger" and Weapon == "Shotgun":
        Accuracy = 4
    elif EnemyDistance == 1 and Class == "Ranger" and Weapon == "Shotgun":
        Accuracy = 3
    elif EnemyDistance == 2 and Class == "Ranger" and Weapon == "Shotgun":
        Accuracy = 0
    # Pistol
    elif EnemyDistance == 0 and Class == "Ranger" and Weapon == "Pistol":
        Accuracy = 3
    elif EnemyDistance == 1 and Class == "Ranger" and Weapon == "Pistol":
        Accuracy = 2
    elif EnemyDistance == 2 and Class == "Ranger" and Weapon == "Pistol":
        Accuracy = 1
    # Sniper Rifle
    elif EnemyDistance == 0 and Class == "Ranger" and Weapon == "Sniper Rifle":
        Accuracy = 0
    elif EnemyDistance == 1 and Class == "Ranger" and Weapon == "Sniper Rifle":
        Accuracy = 3
    elif EnemyDistance == 2 and Class == "Ranger" and Weapon == "Sniper Rifle":
        Accuracy = 4

def aim():
    global Accuracy
    global accuracy_List
    print("Your chance of hitting is ",accuracy_List[Accuracy])

def shoot():
    global Accuracy
    global EnemyWounded
    global EnemyKilled
    global EnemyTroops
    Hit = (random.randrange(0,5,1)/4) # Generates a random chance between 0 to 1
    accuracyPercentChange()
    print("You fire your ",Weapon)
    Hit = Hit * Accuracy # the hit chance times by the accuracy
    if Hit == 0:
        print("Missed")
    elif 0 < Hit < 1:
        print("You Wounded a Enemy")
        EnemyWounded += 1
        EnemyTroops -= 1
    elif Hit <= 1:
        print("You Killed a Enemy")
        EnemyKilled += 1
        EnemyTroops -= 1

def enemyShoot():
    global Troops
    global TroopsDead
    global TroopsWounded
    Hit = (random.randrange(0,5,1)/4)
    print("Enemies fires the squad")
    if Hit == 0:
        print("Enemy Misses")
    elif 0 < Hit < 1:
        print("Soldier is Wounded")
        TroopsWounded -= 1
    elif Hit <= 1:
        print("Soldier is killed ")
        Troops -= 1
        TroopsDead -= 1





