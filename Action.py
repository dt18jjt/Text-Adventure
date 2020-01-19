import random
import sys
Game = True
battlePass = False
combatAction = ""
baseAction = ""
Class = ""
classChange = ""
Weapon = 0
enemyName = ""  # string varible for title of the enemies
Accuracy = 0
enemyDistance = 1
turnCounter = 0
Troops = 30
enemyTroops = 0
shoot_List = ['Shoot', 'shoot', 'shot', 'fire', 'SHOOT', 'S', 's']
equip_List = ['Equip', 'equip', 'EQUIP', 'E', 'e']
aim_List = ['Aim', 'aim', 'AIM', 'A', 'a']
check_List = ['Check', 'check', 'CHECK', 'C', 'c']
heal_List = ['Heal', 'heal', 'HEAL', 'H', 'h']
go_List = ['Go', 'go', 'GO', 'G', 'g']
help_List = ['Help', 'help', 'HELP', '?']
reload_List = ['Reload', 'reload', 'RELOAD', 'R', 'r']
introAction_List = ['Shoot(s)', 'Equip(e)', 'Help(?)']
combatAction_List = ['Shoot(s)', 'Equip(e)', 'Aim(a)', 'Check(c)', 'Heal(h)', 'Go(g)', 'Reload(r)', 'Help(?)']
WepEquip_List = ['1.Machine Gun', '2.Shotgun', '3.Pistol', '4.Sniper Rifle']
weapon_List = ['Machine Gun', 'Shotgun', 'Pistol', 'Sniper Rifle']
class_List = ['1.Gunner', '2.Ranger', '3.Medic']
distance_List = ['Close', 'Mid-range', 'Far']
accuracy_List = ['0%', '25%', '50%', '75%', '100%']
ammo_Dict = {'MachineGun': 6, 'Shotgun': 2, 'Pistol': 4, 'SniperRifle': 1}
troops_Dict = {'TroopsWounded': 0, 'TroopsDead': 0}
enemy_Dict = {'EnemyWounded': 0, 'EnemyKilled': 0}


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
            if Weapon > 0:
                print("You fire your", weapon_List[Weapon - 1])
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
    global enemyTroops
    global Troops
    global enemyName
    global battlePass
    enemyTroops = random.randrange(8,14,1)
    troops_Dict['TroopsWounded'] = 0
    troops_Dict['TroopsDead'] = 0
    print("Team Bravo has encountered a", enemyName, "squad")
    while Troops > 0 or enemyTroops > 0:
        if Troops <= 0 :
            print("All Soldiers are dead, Mission Failure")
            sys.exit(0)
        elif enemyTroops == 0:
            battlePass = True
            Troops += troops_Dict['TroopsWounded']
            print(enemyName," Neutralized")
            print(troops_Dict['TroopsDead'], "Troops lost")
            print("All wounded troops are healed")
            break
        accuracyPercentChange() # Check the class, weapon and distance for accuracy
        print("What will you do?")
        print(combatAction_List) # shows a list of combat commands
        try:
            combatAction = input("") # input for a combat action
        except ValueError:
            continue
        if combatAction in equip_List:
            equip() # Goes to equip function
            enemyShoot() # enemy shoots at team
            continue
        elif combatAction in shoot_List:
            if Weapon > 0:
                shoot() # shoots at enemy
                enemyShoot()
                enemyMove() # enemy distance variable changes
                continue
            else:
                print("You don't have a weapon equipped!")
                enemyShoot()
                continue
        elif combatAction in aim_List:
            aim() # shows aim percentage
            continue
        elif combatAction in reload_List:
            reload() # resets ammo
            enemyShoot()
            continue
        elif combatAction in go_List:
            go() # enemy distance variable changes
            enemyShoot()
            continue
        elif combatAction in heal_List:
            heal() # goes to heal function
            enemyMove()
            continue
        elif combatAction in check_List:
            check() # displays battle infomation
            continue
        elif combatAction in help_List:
            help() # show explinations for commands
            continue


def outroCombat():
    global turnCounter
    global combatAction
    turnCounter = 0
    while turnCounter < 10:
        print("Shoot(s)")
        try:
            combatAction = input("")
        except ValueError:
            continue
        if combatAction in shoot_List:
            print("You fire your weapon blindly")
            print("Missed")
            print("Enemy guns down a soldier")
            turnCounter += 1
            continue
        elif turnCounter == 0:
            break


def equip():
    global Weapon
    weaponchoice = 0
    while Game:
        print(WepEquip_List)
        print("Type the number.")
        try:
            weaponchoice = int(input("")) # Changes the value of weapon
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
    print("TYPE 'Check' or 'c' TO SEE STATUS")
    print("TYPE 'Go' or 'g' TO MOVE LOCATION")
    print("TYPE 'Help' or '?' IF YOU FORGET THE COMMANDS YOU CAN TYPE")


def accuracyPercentChange():
    global Accuracy
    global enemyDistance
    global Weapon
    global Class
    # Gunner and Medic Accuracy
    # Machine gun
    if enemyDistance == 0 and Weapon == 1 and Class != "Ranger":
        Accuracy = 2
    elif enemyDistance == 1 and Weapon == 1 and Class != "Ranger":
        Accuracy = 2
    elif enemyDistance == 2 and Weapon == 1 and Class != "Ranger":
        Accuracy = 1
    # Shotgun
    elif enemyDistance == 0 and Weapon == 2 and Class != "Ranger":
        Accuracy = 3
    elif enemyDistance == 1 and Weapon == 2 and Class != "Ranger":
        Accuracy = 1
    elif enemyDistance == 2 and Weapon == 2 and Class != "Ranger":
        Accuracy = 0
    # Pistol
    elif enemyDistance == 0 and Weapon == 3 and Class != "Ranger":
        Accuracy = 3
    elif enemyDistance == 1 and Weapon == 3 and Class != "Ranger":
        Accuracy = 2
    elif enemyDistance == 2 and Weapon == 3 and Class != "Ranger":
        Accuracy = 1
    # Sniper Rifle
    elif enemyDistance == 0 and Weapon == 4 and Class != "Ranger":
        Accuracy = 0
    elif enemyDistance == 1 and Weapon == 4 and Class != "Ranger":
        Accuracy = 2
    elif enemyDistance == 2 and Weapon == 4 and Class != "Ranger":
        Accuracy = 3
    # Ranger Accuracy
    # Machine gun
    elif enemyDistance == 0 and Weapon == 1 and Class == "Ranger":
        Accuracy = 3
    elif enemyDistance == 1 and Weapon == 1 and Class == "Ranger":
        Accuracy = 3
    elif enemyDistance == 2 and Weapon == 1 and Class == "Ranger":
        Accuracy = 2
    # Shotgun
    elif enemyDistance == 0 and Weapon == 2 and Class == "Ranger":
        Accuracy = 4
    elif enemyDistance == 1 and Weapon == 2 and Class == "Ranger":
        Accuracy = 3
    elif enemyDistance == 2 and Weapon == 2 and Class == "Ranger":
        Accuracy = 0
    # Pistol
    elif enemyDistance == 0 and Weapon == 3 and Class == "Ranger":
        Accuracy = 3
    elif enemyDistance == 1 and Weapon == 3 and Class == "Ranger":
        Accuracy = 2
    elif enemyDistance == 2 and Weapon == 3 and Class == "Ranger":
        Accuracy = 1
    # Sniper Rifle
    elif enemyDistance == 0 and Weapon == 4 and Class == "Ranger":
        Accuracy = 0
    elif enemyDistance == 1 and Weapon == 4 and Class == "Ranger":
        Accuracy = 3
    elif enemyDistance == 2 and Weapon == 4 and Class == "Ranger":
        Accuracy = 4


def ammoCheck():
    global Weapon
    if Weapon == 1:
        print(ammo_Dict['MachineGun'], " Machine gun rounds left")
    # Machine Gun rounds
    elif Weapon == 2:
        print(ammo_Dict['Shotgun'], " Shotgun rounds left")
    # Shotgun rounds
    elif Weapon == 3:
        print(ammo_Dict['Pistol'], " Pistol rounds left")
    # Pistol rounds
    elif Weapon == 4:
        print(ammo_Dict['SniperRifle'], " Sniper Rifle rounds left")
    # Sniper rounds


def aim():
    global Accuracy
    global accuracy_List
    print("Your chance of hitting is ", accuracy_List[Accuracy])
    # Shows accuracy percentage chance from list


def check():
    global Troops
    global enemyTroops
    global enemyDistance
    print("Ammo: ", ammo_Dict)
    print("Troop(s) left: ", Troops)
    print("Wounded Troops: ", troops_Dict['TroopsWounded'])
    print("Dead Troops: ", troops_Dict['TroopsDead'])
    print("Enemies left: ", enemyTroops)
    print("Enemy postion is ", distance_List[enemyDistance])
    # Displays battle info: Ammo, Troops, Enemies


def shoot():
    global Accuracy
    global enemyTroops
    global Weapon
    Hit = (random.randrange(1,5,1)/4) # Generates a random chance between 0 to 1
    accuracyPercentChange()
    print("You fire your ", weapon_List[Weapon - 1])
    # Which weapon equipped takes ammo type away
    # Machine Gun
    if Weapon == 1 and ammo_Dict['MachineGun'] > 0:
        ammo_Dict['MachineGun'] -= 1 # Ammo of weapon subtracted
        Hit = Hit * Accuracy # the hit chance times by the accuracy
        if Hit <= 0.25:
            print("Missed")
        elif 0.25 < Hit < 1:
            enemy_Dict['EnemyWounded'] += 1
            enemyTroops -= 1
            print("You Wounded a Enemy. ", enemyTroops, " Hostile(s) left")
        elif Hit >= 1:
            enemy_Dict['EnemyKilled'] += 1
            enemyTroops -= 1
            print("You Killed a Enemy.", enemyTroops, " Hostile(s) left")
        ammoCheck() # Shows how many rounds are left
    # Shotgun
    elif Weapon == 2 and ammo_Dict['Shotgun'] > 0:
        ammo_Dict['Shotgun'] -= 1
        Hit = Hit * Accuracy
        if Hit <= 0.25:
            print("Missed")
        elif 0.25 < Hit < 1:
            enemy_Dict['EnemyWounded'] += 1
            enemyTroops -= 1
            print("You Wounded a Enemy.", enemyTroops, " Hostile(s) left")
        elif Hit >= 1:
            enemy_Dict['EnemyKilled'] += 1
            enemyTroops -= 1
            print("You Killed a Enemy.", enemyTroops, " Hostile(s) left")
        ammoCheck()
    # Pistol
    elif Weapon == 3 and ammo_Dict['Pistol'] > 0:
        ammo_Dict['Pistol'] -= 1
        Hit = Hit * Accuracy
        if Hit <= 0.25:
            print("Missed")
        elif 0 < Hit < 1:
            enemy_Dict['EnemyWounded'] += 1
            enemyTroops -= 1
            print("You Wounded a Enemy.", enemyTroops, " Hostile(s) left")
        elif Hit >= 1:
            enemy_Dict['EnemyKilled'] += 1
            enemyTroops -= 1
            print("You Killed a Enemy.", enemyTroops, " Hostile(s) left")
        ammoCheck()
    # Sniper Rifle
    elif Weapon == 4 and ammo_Dict['SniperRifle'] > 0:
        ammo_Dict['SniperRifle'] -= 1
        Hit = Hit * Accuracy
        if Hit <= 0.25:
            print("Missed")
        elif 0 < Hit < 1:
            enemy_Dict['EnemyWounded'] += 1
            enemyTroops -= 1
            print("You Wounded a Enemy.", enemyTroops, " Hostile(s) left")
        elif Hit >= 1:
            enemy_Dict['EnemyKilled'] += 1
            enemyTroops -= 1
            print("You Killed a Enemy.", enemyTroops, " Hostile(s) left")
        ammoCheck()
    else:
        print("Weapon has no rounds")


def heal():
    global Troops
    heal = 0
    if Class == "Medic" and troops_Dict['TroopsWounded'] > 0:
        print("You try to heal your teammate")
        print("Healing successful")
        troops_Dict['TroopsWounded'] += 1
        Troops += 1
        # When Class is medic healing chance is 100%
    elif Class != "Medic" and troops_Dict['TroopsWounded'] > 0:
        heal = random.randrange(1, 4, 1)
        print("You try to heal your teammate")
        if heal == 3:
            print("Healing successful")
            troops_Dict['TroopsWounded'] += 1
            Troops += 1
        else:
            print("Healing unsuccessful")
        # Healing is a random chance
    else:
        print("No one needs healing")
        # When no soldiers are wounded


def go():
    global enemyDistance
    go = 0
    print("Where would you like to move to")
    while Game:
        print("1.Forward, 2.Backward, 3.Stay here")
        try:
            go = int(input(""))
        except ValueError:
            continue
        if go == 1 and enemyDistance > 0:
            enemyDistance -= 1
            break
            # Moves closer to the enemy
        elif go == 1 and enemyDistance == 0 :
            print("CANT GO ANY CLOSER!")
            break
            # When the player can't move any closer to enemy
        elif go == 2 and enemyDistance < 2:
            enemyDistance += 1
            break
            # Moves further from the enemy
        elif go == 2 and enemyDistance == 2:
            print("CANT GO ANY FURTHER")
            break
            # When the player can't move any further away from enemy
        elif go == 3:
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
    global enemyTroops
    Hit = (random.randrange(0, 5, 1)/4) # Hit chance is random
    print("Enemies fires at the squad")
    # Enemy accuracy is affected by distance
    if enemyTroops > 0:
        if enemyDistance == 0:
            if Hit == 0:
                print("Enemy Misses")
            elif 0 < Hit < 1:
                troops_Dict['TroopsWounded'] += 1
                Troops -= 1
                print("Soldier is Wounded. ", Troops, " Troop(s) left on the field.")
            elif Hit <= 1:
                Troops -= 1
                troops_Dict['TroopsDead'] += 1
                print("Soldier is killed. ", Troops, " Troop(s) left on the field.")
        elif enemyDistance == 1:
            if 0 <= Hit < 0.5:
                print("Enemy Misses")
            elif 0.5 <= Hit < 1:
                troops_Dict['TroopsWounded'] += 1
                Troops -= 1
                print("Soldier is Wounded. ", Troops, " Troop(s) left on the field.")
            elif Hit <= 1:
                Troops -= 1
                troops_Dict['TroopsDead'] += 1
                print("Soldier is killed. ", Troops, " Troop(s) left on the field.")
        elif enemyDistance == 2:
            if 0 <= Hit < 0.75:
                print("Enemy Misses")
            elif 0.75 <= Hit < 1:
                troops_Dict['TroopsWounded'] += 1
                Troops -= 1
                print("Soldier is Wounded. ", Troops, " Troop(s) left on the field.")
            elif Hit <= 1:
                Troops -= 1
                troops_Dict['TroopsDead'] += 1
                print("Soldier is killed. ", Troops, " Troop(s) left on the field.")


def enemyMove():
    global enemyDistance
    move = random.randrange(1, 4, 1) # Moving a random chance
    if enemyDistance > 0 and move == 1:
        enemyDistance -= 1
        print("Enemy advances forward down the field")
        # Moves closer to player
    elif enemyDistance < 2 and move == 2:
        enemyDistance += 1
        print("Enemy retreats backward down the field ")
        # Moves away from  player
    else:
        print("Enemy holds position")










