import random
Game = True
combatAction = ""
baseAction = ""
Class = ""
classChange = ""
Weapon = 0
enemyName = ""  # string varible for title of the enemies
Accuracy = 0
EnemyDistance = 1
turnCounter = 0
Troops = 20
EnemyTroops = 0
shoot_List = ['Shoot', 'shoot', 'shot', 'fire', 'SHOOT', 'S', 's']
equip_List = ['Equip', 'equip', 'EQUIP', 'E', 'e']
aim_List = ['Aim', 'aim', 'AIM', 'A', 'a']
cover_List = ['Cover', 'cover', 'COVER', 'C', 'c']
heal_List = ['Heal', 'heal', 'HEAL', 'H', 'h']
go_List = ['Go', 'go', 'GO', 'G', 'g']
help_List = ['Help', 'help', 'HELP', 'H', 'h']
reload_List = ['Reload', 'reload', 'RELOAD', 'R', 'r']
introAction_List = ['Shoot(s)', 'Equip(e)', 'Help(h)']
combatAction_List = ['Shoot(s)', 'Equip(e)', 'Aim(a)', 'Cover(c)', 'Heal(h)', 'Go(g)', 'Reload(r)', 'Help(?)']
WepEquip_List = ['1.Machine Gun', '2.Shotgun', '3.Pistol', '4.Sniper Rifle']
weapon_List = ['Machine Gun', 'Shotgun', 'Pistol', 'Sniper Rifle']
class_List = ['1.Gunner', '2.Ranger', '3.Medic']
distance_List = ['Close', 'Mid-range', 'Far']
accuracy_List = ['0%', '25%', '50%', '75%', '100%']
ammo_Dict = {'MachineGun': 6, 'Shotgun': 2, 'Pistol': 4, 'SniperRifle': 1}
troops_Dict = {'TroopsWounded': 0, 'TroopsDead': 0}
enemy_Dict = {'EnemyWounded': 0, 'EnemyKilled':0}

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
            if 0 < Weapon > 5:
                print("You fire your", weapon_List[Weapon])
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
    global troops_Dict
    global EnemyTroops
    global enemyName
    EnemyTroops = random.randrange(10,15,1)
    print("Team Bravo has encountered the ",enemyName)
    while Troops > 0 or EnemyTroops > 0:
        accuracyPercentChange()
        print("What will you do?")
        print(combatAction_List)
        try:
            combatAction = input("")
        except ValueError:
            continue
        if combatAction in equip_List:
            equip()
            continue
        elif combatAction in shoot_List:
            if Weapon > 0:
                shoot()
                enemyShoot()
                continue
            else:
                print("You don't have a weapon equipped!")
                enemyShoot()
                continue
        elif combatAction in aim_List:
            aim()
        elif combatAction in reload_List:
            reload()
        elif combatAction in go_List:
            go()
            enemyShoot()
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
            Weapon = 1
            print("Machine Gun is equipped")
            break
            # Machine gun
        elif weaponchoice == 2:
            Weapon = 2
            print("Shotgun is equipped")
            break
            # Shotgun
        elif weaponchoice == 3:
            Weapon = 3
            print("Pistol is equipped")
            break
            # Pistol
        elif weaponchoice == 4:
            Weapon = 4
            print("Sniper Rifle is equipped")
            break
            # Sniper Rifle
        else:
            continue


def help():
    print("TYPE 'Equip or e' TO EQUIP A WEAPON.")
    print("TYPE 'Shoot or s' TO FIRE YOUR WEAPON")
    print("TYPE 'Aim' or a' TO SEE YOUR CHANCE OF HITTING A ENEMY")
    print("TYPE 'Heal' or 'm' TO HEAL A WOUNDED TEAMMATE")
    print("TYPE 'Cover' or 'c' TO GET BEHIND COVER")
    print("TYPE 'Go' or 'g' TO MOVE LOCATION")
    print("TYPE 'Help' or 'h' IF YOU FORGET THE COMMANDS YOU CAN TYPE")


def accuracyPercentChange():
    global Accuracy
    global EnemyDistance
    global Weapon
    global Class
    # Gunner and Medic Accuracy
    # Machine gun
    if EnemyDistance == 0 and Weapon == 1 and Class != "Ranger":
        Accuracy = 2
    elif EnemyDistance == 1 and Weapon == 1 and Class != "Ranger":
        Accuracy = 2
    elif EnemyDistance == 2 and Weapon == 1 and Class != "Ranger":
        Accuracy = 1
    # Shotgun
    elif EnemyDistance == 0 and Weapon == 2 and Class != "Ranger":
        Accuracy = 3
    elif EnemyDistance == 1 and Weapon == 2 and Class != "Ranger":
        Accuracy = 1
    elif EnemyDistance == 2 and Weapon == 2 and Class != "Ranger":
        Accuracy = 0
    # Pistol
    elif EnemyDistance == 0 and Weapon == 3 and Class != "Ranger":
        Accuracy = 3
    elif EnemyDistance == 1 and Weapon == 3 and Class != "Ranger":
        Accuracy = 2
    elif EnemyDistance == 2 and Weapon == 3 and Class != "Ranger":
        Accuracy = 1
    # Sniper Rifle
    elif EnemyDistance == 0 and Weapon == 4 and Class != "Ranger":
        Accuracy = 0
    elif EnemyDistance == 1 and Weapon == 4 and Class != "Ranger":
        Accuracy = 2
    elif EnemyDistance == 2 and Weapon == 4 and Class != "Ranger":
        Accuracy = 3
    # Ranger Accuracy
    # Machine gun
    elif EnemyDistance == 0 and Weapon == 1 and Class == "Ranger":
        Accuracy = 3
    elif EnemyDistance == 1 and Weapon == 1 and Class == "Ranger":
        Accuracy = 3
    elif EnemyDistance == 2 and Weapon == 1 and Class == "Ranger":
        Accuracy = 2
    # Shotgun
    elif EnemyDistance == 0 and Weapon == 2 and Class == "Ranger":
        Accuracy = 4
    elif EnemyDistance == 1 and Weapon == 2 and Class == "Ranger":
        Accuracy = 3
    elif EnemyDistance == 2 and Weapon == 2 and Class == "Ranger":
        Accuracy = 0
    # Pistol
    elif EnemyDistance == 0 and Weapon == 3 and Class == "Ranger":
        Accuracy = 3
    elif EnemyDistance == 1 and Weapon == 3 and Class == "Ranger":
        Accuracy = 2
    elif EnemyDistance == 2 and Weapon == 3 and Class == "Ranger":
        Accuracy = 1
    # Sniper Rifle
    elif EnemyDistance == 0 and Weapon == 4 and Class == "Ranger":
        Accuracy = 0
    elif EnemyDistance == 1 and Weapon == 4 and Class == "Ranger":
        Accuracy = 3
    elif EnemyDistance == 2 and Weapon == 4 and Class == "Ranger":
        Accuracy = 4
    print("Enemy postion is ", distance_List[EnemyDistance])


def ammoCheck():
    global Weapon
    if Weapon == 1:
        print(ammo_Dict['MachineGun'], " Machine gun rounds left")
    elif Weapon == 2:
        print(ammo_Dict['Shotgun'], " Shotgun rounds left")
    elif Weapon == 3:
        print(ammo_Dict['Pistol'], " Pistol rounds left")
    elif Weapon == 4:
        print(ammo_Dict['SniperRifle'], " Sniper Rifle rounds left")


def aim():
    global Accuracy
    global accuracy_List
    print("Your chance of hitting is ",accuracy_List[Accuracy])


def shoot():
    global Accuracy
    global EnemyWounded
    global EnemyKilled
    global EnemyTroops
    global Weapon
    Hit = (random.randrange(0,5,1)/4) # Generates a random chance between 0 to 1
    accuracyPercentChange()
    print("You fire your ", weapon_List[Weapon - 1])
    # Which weapon equipped takes ammo type away
    # Machine Gun
    if Weapon == 1 and ammo_Dict['MachineGun'] > 0:
        ammo_Dict['MachineGun'] -= 1 # Ammo of weapon subtracted
        Hit = Hit * Accuracy # the hit chance times by the accuracy
        if Hit == 0:
            print("Missed")
        elif 0 < Hit < 1:
            print("You Wounded a Enemy")
            enemy_Dict['EnemyWounded'] += 1
            EnemyTroops -= 1
        elif Hit >= 1:
            print("You Killed a Enemy")
            enemy_Dict['EnemyKilled'] += 1
            EnemyTroops -= 1
        ammoCheck() # Shows how many rounds are left
    # Shotgun
    elif Weapon == 2 and ammo_Dict['Shotgun'] > 0:
        ammo_Dict['Shotgun'] -= 1
        Hit = Hit * Accuracy
        if Hit == 0:
            print("Missed")
        elif 0 < Hit < 1:
            print("You Wounded a Enemy")
            enemy_Dict['EnemyWounded'] += 1
            EnemyTroops -= 1
        elif Hit >= 1:
            print("You Killed a Enemy")
            enemy_Dict['EnemyKilled'] += 1
            EnemyTroops -= 1
        ammoCheck()
    # Pistol
    elif Weapon == 3 and ammo_Dict['Pistol'] > 0:
        ammo_Dict['Pistol'] -= 1
        Hit = Hit * Accuracy
        if Hit == 0:
            print("Missed")
        elif 0 < Hit < 1:
            print("You Wounded a Enemy")
            enemy_Dict['EnemyWounded'] += 1
            EnemyTroops -= 1
        elif Hit >= 1:
            print("You Killed a Enemy")
            enemy_Dict['EnemyKilled'] += 1
            EnemyTroops -= 1
        ammoCheck()
    # Sniper Rifle
    elif Weapon == 4 and ammo_Dict['SniperRifle'] > 0:
        ammo_Dict['SniperRifle'] -= 1
        Hit = Hit * Accuracy
        if Hit == 0:
            print("Missed")
        elif 0 < Hit < 1:
            print("You Wounded a Enemy")
            enemy_Dict['EnemyWounded'] += 1
            EnemyTroops -= 1
        elif Hit >= 1:
            print("You Killed a Enemy")
            enemy_Dict['EnemyKilled'] += 1
            EnemyTroops -= 1
        ammoCheck()
    else:
        print("Weapon has no rounds")

def go():
    global EnemyDistance
    goChoice = 0
    print("Where would you like to move to")
    while Game:
        print("1.Forward, 2.Backward, 3.Stay here")
        try:
            goChoice = int(input(""))
        except ValueError:
            continue
        if goChoice == 1 and EnemyDistance > 0:
            EnemyDistance -= 1
            break
        elif goChoice == 1 and EnemyDistance >= 2:
            print("CANT GO ANY CLOSER!")
            break
        elif goChoice == 2 and EnemyDistance < 2:
            EnemyDistance += 1
            break
        elif goChoice == 2 and EnemyDistance == 2:
            print("CANT GO ANY FURTHER")
            break
        elif goChoice == 3:
            break
        else:
            continue



def reload():
    # Resets the ammo's values
    # if the class is not a Gunner
    if Weapon == 1 and Class != "Gunner":
        ammo_Dict['MachineGun'] = 6
        print("Machine gun reloaded")
    elif Weapon == 2 and Class != "Gunner":
        ammo_Dict['Shotgun'] = 2
        print("Shotgun reloaded")
    elif Weapon == 3 and Class != "Gunner":
        ammo_Dict['Pistol'] = 4
        print("Pistol reloaded")
    elif Weapon == 4 and Class != "Gunner":
        ammo_Dict['SniperRifle'] = 1
        print("Sniper rifle reloaded")
    # if the class is Gunner
    elif Weapon == 1 and Class == "Gunner":
        ammo_Dict['MachineGun'] = 12
        print("Machine gun reloaded")
    elif Weapon == 2 and Class == "Gunner":
        ammo_Dict['Shotgun'] = 4
        print("Shotgun reloaded")
    elif Weapon == 3 and Class == "Gunner":
        ammo_Dict['Pistol'] = 8
        print("Pistol reloaded")
    elif Weapon == 4 and Class == "Gunner":
        ammo_Dict['SniperRifle'] = 2
        print("Sniper rifle reloaded")


def enemyShoot():
    global Troops
    global TroopsDead
    global TroopsWounded
    Hit = (random.randrange(0,5,1)/4)
    print("Enemies fires the squad")
    if EnemyDistance == 0:
        if Hit == 0:
            print("Enemy Misses")
        elif 0 < Hit < 1:
            print("Soldier is Wounded")
            troops_Dict['TroopsWounded'] += 1
            Troops -= 1
        elif Hit <= 1:
            print("Soldier is killed ")
            Troops -= 1
            troops_Dict['TroopsDead'] += 1
    elif EnemyDistance == 1:
        if 0 <= Hit < 0.5:
            print("Enemy Misses")
        elif 0.5 <= Hit < 1:
            print("Soldier is Wounded")
            troops_Dict['TroopsWounded'] += 1
            Troops -= 1
        elif Hit <= 1:
            print("Soldier is killed ")
            Troops -= 1
            troops_Dict['TroopsDead'] += 1
    elif EnemyDistance == 2:
        if 0 <= Hit < 0.75:
            print("Enemy Misses")
        elif 0.75 <= Hit < 1:
            print("Soldier is Wounded")
            troops_Dict['TroopsWounded'] += 1
            Troops -= 1
        elif Hit <= 1:
            print("Soldier is killed ")
            Troops -= 1
            troops_Dict['TroopsDead'] += 1







