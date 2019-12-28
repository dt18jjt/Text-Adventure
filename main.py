import Action
Name = "You"
Decision = ""
yes_List = ['YES', 'yes', 'Y', 'Yes', 'y']
no_List = ['NO', 'no', 'No', 'N', 'n']
Intro = True


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
            classChoice()
        else:
            continue


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
            print("Gunner specializes in firearms but bad with explosives 'INCREASED DAMAGE'")
            Class = "Gunner"
            introChoice()
            break
        elif classChange == 2:
            print("Ranger specializes in sniping but less health'INCREASED ACCURACY")
            Class = "Ranger"
            introChoice()
            break
        elif classChange == 3:
            print("Medic can heal themselves at any time but do little damage 'INCREASED HEALTH")
            Class = "Medic"
            introChoice()
            break
        elif classChange == 4:
            print("Demolition can carry more bombs but has bad aim 'INCREASED EXPLOSIVES")
            Class = "Demolition"
            introChoice()
            break
        else:
            continue

# Intro Sequence
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
print("Capt.Rock: Now onto weapons and fighting enemi-")
print("KABOOOM!!!!")
print("Random Soldier: EXPLOSION AT THE SOUTH SIDE!")
print("Capt.Rock: Damn they found us! ", Name, " grab a weapon bag and start shooting!")
print("Type 'Equip or e' to equip a weapon and choose one ")
print("Type 'Shoot or s' to use it!")
print("Type 'Help or h' if forget the commands you can type")
Action.introCombat()
print("Capt.Rock: WAIT STOP!")
print("Capt.Rock: NO ENEMIES IN SIGHT! WHAT'S GOING ON HERE!")
print("Random Soldier: Sir! It seems to be a explosives malfunction false alarm!")
print("Capt.Rock: Damn we're not even in battle yet and already wasting ammo")
print("Capt.Rock: Hey",Name,"what was I talking about earlier?")
print(Name,": Sir! You were talking about wep-")
print("Capt.Rock: Ah yes weapons and battling! Well you just did some of that just now.")
print("Capt.Rock: BUT! Battling isn't just about spraying and praying")
print("Capt.Rock: 'Accuracy' needs to be taken into account ")
print("Capt.Rock: Your Class, Weapon and distance from enemy affects 'Accuracy'")
print("Capt.Rock: Type 'Aim' or a' to see your chance of hitting a enemy")
print("Capt.Rock: 'Healing' can Heal you or a teammate. If you're not a medic you have to ask for healing from a medic")
print("Capt.Rock: Type 'Medkit or m' to heal or ask for healing")
print("Capt.Rock: 'Cover' will decrease your chance of getting shot but the enemy will push forward")
print("Capt.Rock: Type 'Cover or c' to get behind cover")
print("Capt.Rock: All the actions will be shown whenever you type 'Help or h'")
print("Capt.Rock: Now onto the mission briefing. EVERYONE GATHER UP!")
