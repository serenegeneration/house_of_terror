import time

items = [

]

rooms = [

]
#this neat little feature added by yakubu
def print_pause(message):
    print(message)
    time.sleep(2)
# this long pause and the box room done by paul
def long_pause(message):
    print(message)
    time.sleep(4)

def ghost(dialogue):
    print(" .-.")
    print("(o o) " + dialogue)
    print("| O \ ")
    print(" \   \ ")
    print("  `~~~'")

def ghost2(dialogue):
    print("     .-.")
    print("    (o o) " + dialogue)
    print("----\ O \ ")
    print("     \   \ ")
    print("      `~~~'")

def hide():
    print("You hide in the trunk, trembling with fear, desperately holding the lid shut")
    print_pause("Holding on tight...")
    print_pause(".")
    print_pause(".")
    print_pause(".")
    print_pause(".")
    print_pause(".")
    print_pause(".")
    print_pause("You don't know how long you've been hiding, but it feels like hours")
    print_pause(".")
    print_pause(".")
    print_pause(".")
    print("You can't hear anything outside the trunk... maybe the coast is clear")
    print_pause(".")
    print_pause(".")
    trunk_exit = input("Do you want to get out of the trunk? (YES/NO): ")
    if trunk_exit.lower() == "yes":
        print("You calm yourself down and think things through")
        print_pause("There's no such thing as ghosts! ")
        print_pause("")
        print("You open the lid of the trunk and cautiously step outside")
        print_pause("")
        print("There doesn't seem to be anyone there...")
        print_pause("")
        print("You laugh at yourself for being such a coward - what were you doing hiding in a box?!")
        print_pause("")
        print("You walk towards the door, but as you reach for the handle, you feel a presence behind you")
        long_pause("")
        print("You turn around... and see the ghost's face inches from yours")
        ghost_death()
    elif trunk_exit.lower() == "no":
        print("You're safe and warm in here. You keep the lid shut tight")
        long_pause("")
        hide_ending()
    else:
        print("You're too scared to think. Keep the lid shut!")
        long_pause("")
        hide_ending()

def ghost_death():
    print("The ghost reaches out its thin, boney, spectral hand towards you")
    print_pause("")
    ghost2("Stay with me!")
    print_pause("")
    print("You're numb with fear, and the room around you goes cold as the ghost's hand touches your heart")
    long_pause("")
    print("You feel your energy drain away as the ghost consumes your life force")
    print_pause("")
    print("You have died")
    print("")
    print("THE END")
    ####END OF GAME####

def hide_ending():
    print("You wake up. You have no idea how much time has passed")
    long_pause("")
    print("You notice that you soiled yourself during the night, and the smell is stifling")
    long_pause("")
    print("You burst out of the trunk, gasping for air")
    print_pause("")
    print("The ghost has gone, but you see three shocked faces staring back at you")
    long_pause("")
    print("An estate agent is giving a house viewing to a well-dressed couple")
    long_pause("")
    print("You try to explain about the ghost, but they just stare at you in pity and disgust")
    long_pause("")
    print("They give you a warm blanket and a cup of tea, and eventually the police arrive to take you away")
    long_pause("")
    print("You survived the night, but you vaguely wish you hadn't")
    print("")
    print("THE END")
    ####END OF GAME####

def ghost_encounter():
    ghost("You left me here to die!")
    print_pause("")
    ghost_run = input("Do you run away from the ghost? (YES/NO): ")
    print_pause("")

    if ghost_run.lower() == "yes":
        print("You turn and run for the door, but it slams shut as you run towards it")
        print_pause("")
        print("You look around the room frantically and notice a large trunk by the side of the bed")
        print_pause("")
        trunk = input("Do you get into the trunk and hide from the ghost? (Yes/No?): ")
        if trunk.lower() == "yes":
            hide()
        elif trunk.lower() == "no":
            print("You give up trying to escape, and you turn to face the ghost")
            long_pause("")
            ghost_death()
        else:
            print("This is no time for indecision. You stand frozen in fear as the ghost moves towards you")
            long_pause("")
            ghost_death()
    elif ghost_run.lower() == "no":
        print("You stand your ground and face the ghost")
        long_pause("")
        ghost_death()
    else:
        print("You're paralysed by fear and indecision")
        long_pause("")
        ghost_death()

def wardrobe_choice(): 
      wardrobe = input("Do you walk over to the wardrobe? (Yes/No): ")
      print_pause("")

      if wardrobe.lower() == "no":
        print("You walk back out of the room and quietly close the door behind you. Something's not right in here")
        print_pause("as you walk out of the room you forgot about the hungry bear.")
        print_pause("unfortunately the bear did not forgot about you.")
        print_pause ("within moments it is over as the bear mauls and eats you.")

      elif wardrobe.lower() == "yes":
        print("You open the wardrobe and peer inside")
        print_pause("")
        print("At first it seems empty, but as your eyes adjust to the light, a cold, blank pair of eyes meets yours")
        print_pause(":o")
        print("A horrifying spectral figure emerges from the wardrobe and moves towards you")
        print_pause("")
        ghost("RAAAAAARghgh!")
        long_pause("")
        print("A ghost screams at you in a familiar voice")
        ghost_encounter()


      else: 
          print("Make your mind up "), print_pause(""), wardrobe_choice()
        
def box_room():
    print("You find yourself in an old bedroom, lit by a flickering candle on the bedside table")
    print_pause("")
    print("The room is meticulously neat and tidy, but there's a layer of dust over every surface")
    long_pause("")
    print("You get the distinct sense that nothing in this room has been touched in years, and yet you feel like there's someone in here with you...")
    long_pause("")
    print("As you look around the room, you notice a wardrobe door slightly ajar...")
    print_pause("")
    print("that door was definitely closed when you walked in... wasn't it??")
    print_pause("")

    wardrobe_choice()

def play_again():
    while True:
        again = input("Would you like to play again? (yes/no): ").lower()
        if again == 'yes':
            startgame()
        elif again == "no":
            print ("thank you for playing. goodbye")
            break


def bad_room():
   print_pause ("you open the door and quickly shut it behind you.")
   print_pause ("looking around swiftly you see nothing that can help you.")
   print_pause ("within moments the bear breaks down the door.")
   print_pause ("you struggle as the bear lands upon you but it is open in a short time.")
   print_pause ("unfortunately you are food for this ravenous bear.")
   play_again()

def box_room():
   print_pause("")


# Carlos
def window_room():
   print_pause("You enter a room with a large, boarded-up window.")
   print_pause("You see a small gap in the boards, and a faint light shines through.")
   print_pause("With some effort, you pry the boards loose.")
   print_pause("You jump out the window! escaping the house but breaking your legs because you fell at a weird angle...")
   print_pause("You find yourself in a overgrown garden hurt and afraid, but free from the house.")
   play_again()

def upstairs_choice():
    path_choice = input ("please type left or right: ")
    if path_choice == "left":
       bad_room()
    elif path_choice == "right":
       window_room()

def stairs():
   if rooms.count ("basement") == 0:
    print_pause ("as you walk up the stairs there is a loud crash as a bear slams through the door")
    print_pause("you quickly charge up the stairs barely thinking. before you are two doors")
    print_pause("do you pick the left or right?")
    upstairs_choice()

   elif rooms.count ("basement") == 1:
     print_pause ("as you walk up the stairs you hear a loud roar from the angry bear you hurt")
     print_pause("it charges up from the basement and starts to come up the stairs.")
     print_pause("you quickly charge up the stairs and see two doors")
     print_pause("do you pick left or right?")
     upstairs_choice()

def gf_choice():
   path_choice = input ("please choose left or right")
   if path_choice == "left":
      box_room()

   elif path_choice == "right":
      bad_room()

def coridoor():
   if rooms.count ("basement") == 0:
    print_pause ("as you walk along the coridoor you hear a loud crash from behind you!")
    print_pause ("a bear comes crashing through the front door and charges towards you!")
    print_pause ("before you are two doors. no time to react which door do you choose!")
    gf_choice()

   elif rooms.count ("basement") == 1:
     print_pause("as you walk along the coridoor you hear a loud roar from the basement!")
     print_pause("the bear you hurt's heavy footstps can be heard barreling up the stairs!")
     print_pause("before you are two rooms. no time to pick which room do you pick?")
     gf_choice()


#full basement scene done by yakubu
#slight adjustments to defines and calling those defines back work with main code done by rhys

def bad_choice():
    print_pause("You hesitate and fail to choose an item in time.")
    print_pause("The bear lunges at you, and you are unable to defend yourself.")
    print_pause("Game over. You have been mauled by the bear.")
    play_again()

def crowbar():
    print_pause("You grab the crowbar and feel its weight in your hands.")
    print_pause("The bear charges at you, and you swing the crowbar with all your might.")
    print_pause("You hit the bear square in the face, causing it to roar in pain.")
    print_pause("The bear retreats, giving you just enough time to sprint to the exit and escape!")
    rooms.append("basement")
    house_gf()
 
def rusty_toolbox():
    print_pause("You grab the rusty toolbox and open it.")
    print_pause("Inside, you find a set of old, but sturdy tools.")
    print_pause("You quickly fashion a makeshift weapon and prepare to defend yourself.")
    print_pause("The bear charges at you, but you manage to fend it off with your improvised weapon.")
    print_pause("With the bear momentarily stunned, you make a run for the exit and escape!")
    rooms.append("basement")
    house_gf()

def choose_item():
    print_pause("You quickly scan the room and see two items:")
    print_pause("1. A rusty toolbox")
    print_pause("2. A crowbar")
    choice_basement = input("Which item do you choose? (Enter 1 or 2): ")
    if choice_basement == '1':
        rusty_toolbox()
    elif choice_basement == '2':
        crowbar()
    else:
        bad_choice()

def basement():
    print_pause("You find yourself in the dark, damp basement of an abandoned house.")
    print_pause("The air is thick with the smell of mold and rust.")
    print_pause("You hear a low growl behind you. Turning around, you see a massive bear!")
    print_pause("The bear is blocking the only exit. You need to find a way to escape!")
    choose_item()

#main coding done by rhys, i:e into, choice for if you stay by car, entering house, coridoors
def house_gf():
   print_pause ("before you lies a long coridoor with various doors, a set of stairs along the wall heading to the top floor,")
   print_pause ("and a set of stairs leading to the bowels of the house, the bottom near invisible as the darkness encases it.")
   print_pause ("do you wish to go upstairs, go downstairs or walk the coridoor?")
   path_choice = input ("please enter go upstairs, go downstairs or walk coridoor: ")
   if path_choice == "go upstairs":
     stairs()
   elif path_choice == "go downstairs" and rooms.count ("basement") == 0:
    basement()
   elif path_choice == "go downstairs" and rooms.count ("basement") == 1:
      print_pause ("it would be unwise to go downstairs right now")
      house_gf()
   elif path_choice == "walk coridoor":
      coridoor()

def enter_house ():
   print_pause ("you decide nobody is going to travel along the road, especially not at this time")
   print_pause ("as you walk up to the house and step onto it's wooden porch")
   print_pause ("the wood creaks and groans as though eager for it's next victim")
   print_pause ("you knock on the door, the sound echoing through the empty house like thunder.")
   print_pause ("the door swings open though there was nobody there")
   print_pause ("reluctantly you enter the decrepid house.")
   house_gf()

def choice_1 ():
     path_choice = input ("please enter, enter the house or stay by car: ")
     if path_choice == "stay by car":
      print_pause ("you decide to stay by your car not wanting to risk the creepy house.")
      print_pause ("you wait all night with no cars passing by.")
      print_pause ("when it turns to day you decide to try the forest in hopes of finding people")
      print_pause ("you walk but there is nobody around.")
      print_pause ("you hear a loud crash and in seconds it is over")
      print_pause ("mauled by a bear you are not found, food for the wildlife.")
      play_again()
     elif path_choice == "enter the house":
      enter_house()
     else:
      print ("please enter, enter the house or stay by car: ")
      choice_1()   

def startgame():
    print_pause ("you are travelling down a road in the dead of night.")
    print_pause ("besides you is a forest that stretches as far as the eye can see.")
    print_pause ("suddenly your car breaks down and you quickly get out as smoke pours out of the front of the car.")
    print_pause ("looking around you spot a derelict house.")
    print_pause ("you see only 2 options for what to do in this situation.")
    print_pause ("do you wish to enter the house in hopes of finding help for your predicament?")
    print_pause ("or do you wish to stay by the car in hopes somebody travels down this rundown road?")
    choice_1()
 
startgame()
