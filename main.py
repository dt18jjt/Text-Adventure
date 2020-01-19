import Action
import random
import sys
Regroup = False
Name = "You"  # string varible for the name
Decision = ""  # varible for writing decision
moveAction = ""
Outpost = 1
yes_List = ['YES', 'yes', 'Y', 'Yes', 'y']  # list of inputs for yes
no_List = ['NO', 'no', 'No', 'N', 'n']  # list of inputs for no
start_List = ['Start', 'start', 'START'] # list of inputs for start
enemyNameList = ["1.Russians", "2.North Koreans", "3.Arabs", "4.Zombie Uber-Nazis", "5.Vegans"] # list of enemy names
outpost_List = ['A', 'B', 'C', 'D'] # list for the outpost names
teamMove_List = ['Advance(a)', 'Scope(s)', 'Regroup(r)', 'Help(?)'] # list of inputs for movement actions
advance_List = ['Advance', 'advance', 'ADVANCE', 'A', 'a'] # list of inputs for advance
scope_List = ['Scope', 'scope', 'SCOPE', 'S', 's'] # list of inputs for scope
regroup_List = ['Regroup', 'regroup', 'REGROUP', 'R', 'r'] # list of inputs for regroup
help_List = ['Help', 'help', 'HELP', '?'] # list of inputs for help
teamMove_Dict = {'Day': 1, 'Distance': 4, 'Time': 600} # values for Day, Distance, Time and Turnstaken


def introChoice():
    global Decision
    global yes_List
    global no_List
    while Action.Game:
        print("Are you sure? TYPE YES OR NO")
        try:
            Decision = input("")
        except ValueError:
            continue
        if Decision in yes_List:
            break
        elif Decision in no_List:
            Decision = ""
            classChoice()
        else:
            continue
        break

def classChoice():
    global classChange
    global Class
    while Action.Game:
        print("Type the number of the class you want")
        print(Action.class_List)
        try:
            classChange = int(input(""))
        except ValueError:
            continue
        if classChange == 1:
            print("Gunner specializes in firearms so they carry more rounds 'FIREPOWER'")
            Action.Class = "Gunner"
            introChoice()
            break
        elif classChange == 2:
            print("Ranger specializes in sniping so they have better aim 'ACCURACY'")
            Action.Class = "Ranger"
            introChoice()
            break
        elif classChange == 3:
            print("Medic can heal soldiers completely on the first try 'HEALING")
            Action.Class = "Medic"
            introChoice()
            break
        else:
            continue


def teamMove():
    global Regroup
    global moveAction
    encounter = 0
    while teamMove_Dict['Day'] <= 9 and Outpost < 4:
        outpostCheck()
        if teamMove_Dict['Time'] > 2200:
            teamMove_Dict['Time'] = 200
            teamMove_Dict['Day'] += 1
        if teamMove_Dict['Day'] >= 9:
            print("Run out time to capture Outpost D mission failure")
            sys.exit(0)
        encounter = random.randrange(1,4,1)
        print("Day", teamMove_Dict['Day'])
        print("The Time is",str(teamMove_Dict['Time']).zfill(4))
        print("Outpost", outpost_List[Outpost], "is", teamMove_Dict['Distance'], "KM away")
        print("How should we proceed?")
        print(teamMove_List)
        try:
            moveAction = input("")
        except ValueError:
            continue
        if moveAction in advance_List:
            # Outpost Battles
            if Outpost == 1 and teamMove_Dict['Distance'] == 1:
                print("Defeat the", Action.enemyName, "squad to capture Outpost", outpost_List[Outpost])
                Action.playerTurn()
                teamMove_Dict['Time'] += 400  # Time Advances
                teamMove_Dict['Distance'] -= 1  # Distance gets shorter
                print("Team Bravo advances")
            elif Outpost == 2 and teamMove_Dict['Distance'] == 1:
                print("Defeat the", Action.enemyName, "squad to capture Outpost", outpost_List[Outpost])
                Action.playerTurn()
                teamMove_Dict['Time'] += 400  # Time Advances
                teamMove_Dict['Distance'] -= 1  # Distance gets shorter
                print("Team Bravo advances")
            elif Outpost == 3 and teamMove_Dict['Distance'] == 1:
                finalBattle()
            else:
                teamMove_Dict['Time'] += 400 # Time Advances
                teamMove_Dict['Distance'] -= 1 # Distance gets shorter
                print("Team Bravo advances")
                if encounter == 1 and not Action.battlePass:
                    Action.playerTurn()
                    continue
                else:
                    Action.battlePass = False # turn the battlepass to false so can be encountered next turn
                    continue
        elif moveAction in scope_List:
            teamMove_Dict['Time'] += 400
            print("Scoping out the area...")
            if encounter == 1:
                print("Enemy Found!")
                print("A", Action.enemyName, "squad were ambushed and defeated")
                Action.battlePass = True
                continue
            else:
                print("No enemies were spotted")
                continue
        elif moveAction in regroup_List and Regroup != True:
            if Action.Troops <= 25:
                Action.Troops = 30
                Regroup = True
                teamMove_Dict['Day'] += 1
                teamMove_List.remove('Regroup(r)')
                print("Backup has arrived, Troops back to max")
                continue
            else:
                print("It isn't the right time to regroup yet")
                continue
        elif moveAction in help_List:
            print("TYPE 'Advance or a' FOR THE TEAM TO PROCEED FORWARD")
            print("TYPE 'Scope or s' TO SCOPE OUT A AREA FOR A CHANCE TO AMBUSH A ENEMY")
            print("TYPE 'Regroup or r' WHEN TROOPS ARE LOW REGROUP TO GAIN MORE TROOPS")
            print("TYPE 'Help' or '?' IF YOU FORGET THE COMMANDS YOU CAN TYPE")
            continue


def outpostCheck():
    global Outpost
    if Outpost == 1 and teamMove_Dict['Distance'] == 0:
        Outpost += 1
        # Goes to next outpost
        teamMove_Dict['Distance'] = 8
    elif Outpost == 2 and teamMove_Dict['Distance'] == 0:
        Outpost += 1
        teamMove_Dict['Distance'] = 12
    elif Outpost == 3 and teamMove_Dict['Distance'] == 0:
        Outpost += 1


def finalBattle():
    # final battle sequence
    print("Defeat the", Action.enemyName, "squad to capture Outpost", outpost_List[Outpost])
    print("Sgt.Cold: Finally boys we're at Outpost D good work", Name)
    print(Name, ": Thank you sir.")
    print("Sgt.Cold: Wait a second! Where is the enemy they should be he-")
    print("BOOOOOOOOOM")
    print("Sgt.Cold: Dammit the", Action.enemyName, "ambushed us!")
    print("Sgt.Cold: MEN DON'T THINK JUST SHOOT!")
    Action.outroCombat()
    print("BAAAAANG")
    print("Capt.Rock: CAN YOUR SMELL WHAT THE ROCK IS COOKING?")
    print("Sgt.Cold: Rock you son of a bitch!")
    print("Capt.Rock: In trouble again Cold? I guess that why you're in the B-Team.")
    print("Capt.Rock: Alright lets finish this fight!")
    print("TROOPS HAVE INCREASED")
    Action.Troops = 40
    Action.playerTurn()
    print("Sgt.Cold: We did it!")
    print("Everyone: YEAAAAAAAAAAAAAAAAAAAAAH")
    print(Name, ": Hey Captain Rock sorry")
    print("Capt.Rock: For what?")
    print(Name, ": You told me to tell you that if I ever made it out of here alive")
    print("Capt.Rock: HAHAHA I guess I did tell you did tell you that.")
    print("You defeated the", Action.enemyName, "TIME TO PARTY!")
    sys.exit(0)


# Intro Sequence
print("Capt.Rock:WAKE UP SOLDIER! YOU THINK YOU CAN SLEEP WHILE ON DUTY!")
print(Name, ": No sir! Sor-")
print("Capt.Rock: Save your apologies if you're still alive after this!")
print("Capt.Rock: What is your name?")
Name = input("") # player inserts name
print(Name, ":My name is", Name[0], "-") # player's name get cutoff
print("Capt.Rock:It doesn't matter what your name is!")
print("Capt.Rock:Matter of fact I'll give you a new name. You've got two choices")
print("Capt.Rock: Option 1 - 'Bedtime' because you love to sleep so much")
print("Capt.Rock: Option 2 - 'Baby' because you probably going to be first to piss themselves")
# Name change for player
while Action.Game:
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
print("Capt.Rock: Hear that everybody meet our new recruit", Name, "!")
print("Everyone: HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA")
print("Everyone:", Name * 6)
print("Capt.Rock: Alright shut up this isn't playtime back to positions!")
print("Capt.Rock:", Name, "come with me!")
print(Name, ":o-okay sir")
print("Capt.Rock: You've been here for a while now and I'm glad to say your training is done")
print("Capt.Rock: DON'T CELEBRATE NOW! This is only the start, Each solider has their own class")
print("Capt.Rock: A class is a area of expertise and you only have choice of 3")
print("Capt.Rock: You can choose only one. Just like your name type the number of the class you want")
classChoice()
# If class equals gunner ammo is doubled
if Action.Class == "Gunner":
    for i in Action.ammo_Dict:
        Action.ammo_Dict[i] *= 2
print("Capt.Rock: So you choose", Action.Class, "very well.")
print("Capt.Rock: Now onto weapons and fighting enemi-")
print("(KABOOOM!!!!)")
print("Random Soldier: EXPLOSION AT THE SOUTH SIDE!")
print("Capt.Rock: Damn they found us! ", Name, " grab a weapon bag and start shooting!")
print("TYPE 'Equip or e' TO EQUIP A WEAPON.")
print("TYPE 'Shoot or s' TO FIRE YOUR WEAPON")
print("TYPE 'Help or h' IF YOU FORGET THE COMMANDS YOU CAN TYPE")
Action.introCombat()
print("Capt.Rock: WAIT STOP!")
print("Capt.Rock: NO ENEMIES IN SIGHT! WHAT'S GOING ON HERE!")
print("Random Soldier: Sir! It seems to be a explosives malfunction false alarm!")
print("Capt.Rock: EVERYONE BACK TO POSTIONS!")
print("Capt.Rock: Hey", Name, "what was I talking about earlier?")
print(Name, ": Sir! You were talking about wep-")
print("Capt.Rock: Ah yes weapons and battling! Well you just did some of that just now.")
print("Capt.Rock: BUT! Battling isn't just about spraying and praying")
print("Capt.Rock: 'Accuracy' needs to be taken into account ")
print("Capt.Rock: Your Class, Weapon and distance from enemy affects 'Accuracy'")
print("Capt.Rock: Type 'Aim' or a' to see your chance of hitting a enemy")
print("Capt.Rock: 'Healing' can Heal a wounded teammate but there's a chance of failing unless it's a medic ")
print("Capt.Rock: Type 'Heal or h' to heal a teamate")
print("Capt.Rock: 'Check' will show the status of your: troops, weapons and enemy use it for tactical advantage ")
print("Capt.Rock: Type 'Check or c' to look at status")
print("Capt.Rock: 'Go' will change the teams location to be closer or further from the enemy")
print("Capt.Rock: Type 'Go or g' to move location")
print("Capt.Rock Type 'Reload or r' when low on rounds")
print("Capt.Rock: All the actions will be shown whenever you type 'Help or ?'")
print("Capt.Rock: Now onto the mission briefing. EVERYONE GATHER UP!")
print("Capt.Rock: This it men we're finally going to fight the-, the-, ......")
print("Capt.Rock: ............")
print(Name, ": Sir, did you forget who our enemy i-")
print("Capt Rock: ABSOLUTELY NOT! Seeing as your such a smartass how about you tell everyone enemy is")
print("Capt.Rock: Just in case anyone forgot, not including me")
# Name change for enemies
while Action.Game:
    print(Name, ": S-Sir our enemy is the: ")
    print(enemyNameList)
    print("Type a number")
    try:
        enemyNameChange = int(input(""))
    except ValueError:
        continue
    if enemyNameChange == 1:
        Action.enemyName = "Russians"
        break
    elif enemyNameChange == 2:
        Action.enemyName = "North Koreans"
        break
    elif enemyNameChange == 3:
        Action.enemyName = "Arabs"
        break
    elif enemyNameChange == 4:
        Action.enemyName = "Zombie Uber-Nazis"
        break
    elif enemyNameChange == 5:
        Action.enemyName = "Vegans"
        break
    else:
        continue
print(Name, ": It's the ", Action.enemyName[0:-2], "-")
print("Capt.Rock: YES! The ", Action.enemyName, " damn those bastards!")
print("Capt.Rock: Our mission is to secure the area around outpost D and currently we're at outpost A.")
print("Capt.Rock: However we'll stick out like a sore thumb all together like so we'll split up.")
print("Capt.Rock: Two teams, Team Alpha and Team Bravo the team each of you are on is on the board other there")
print("Capt.Rock: Once you know your team get some rest and we move out at 0600. ")
print("Capt.Rock: If we don't secure the outpost in 9 days it's a mission failure. Everyone clear?")
print("Everyone: SIR YES SIR!")
print(Name, "is on Team Bravo")
print("THE NIGHT PASSES GET READY FOR BATTLE!")
# Introduction end
print("TYPE 'Start' TO BEGIN YOUR MISSION")
while Action.Game:
    try:
        Start = input("")
    except ValueError:
        continue
    if Start in start_List:
        break
    else:
        continue
# type start to begin the game
print("Sgt.Cold: ALRIGHT EVERYBODY LINE YOUR CANDY ASSES UP.")
print("Sgt.Cold: Damn look at all of you looking like you just came out of your mother!")
print("Sgt.Cold: With this lineup we should rename 'Team BRAVO' to 'Team BITCH'.")
print("Sgt.Cold: I'd much rather be back in Texas enjoying a cold one but I'm here babysitting you pissheads.")
print("Sgt.Cold: Let me give you a lowdown of what's gonna happen while I'm in command.")
print("Sgt.Cold: If I tell you to kill, you kill.")
print("Sgt.Cold: If I tell you to die, you die.")
print("Sgt Cold: If I tell you to jump, you don't ask 'how high' I expect you to do a double jump")
print("Sgt.Cold: AND THAT'S THE BOTTOM LINE CUZ SERGENT COLD SAID SO! ")
print(Name, "(whispering): Man this guy is over the top.")
print("Sgt.Cold: What do you say you shit?")
print(Name, ": N-N-NOTHING SIR SORRY SIR.")
print("Sgt.Cold: Sorry may on that pansy Capt.Rock but not on me.")
print("Sgt.Cold: If you think you can talk over me then I guess you can be in charge of me and while squad.")
print("Everyone &", Name, "WHHAAAAAAAAAAAAAT!")
print("Random Soldier: But sir!", Name, "is just a rookie!")
print("Sgt.Cold: Well then I guess", Name, "will the first rookie to lead Team Bravo.")
print("Sgt.Cold: Okay kid let's see what you got and don't get us killed.")
print("MOVE MAKES THE TEAM ADVANCE CLOSER TO THE OUTPOST")
print("SCOPE WILL SCAN FOR ENEMIES IF FOUND THE TEAM WILL AMBUSH THEM")
print("REGROUP WHEN TROOPS ARE LOW REGROUP TO GAIN MORE TROOPS BUT TAKES A ENTIRE DAY AND CAN BE ONLY USED ONCE")
teamMove()
# Main game start