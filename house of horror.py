import time

items = [

]

rooms = [

]
#this neat little feature added by yakubu
def print_pause(message):
    print(message)
    time.sleep(2)

def bad_room():
   print_pause ("")

def window_room():
   print_pause("")

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

   elif rooms.count (basement) == 1:
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

   elif rooms.count (basement) == 1:
     print_pause("as you walk along the coridoor you hear a loud roar from the basement!")
     print_pause("the bear you hurt's heavy footstps can be heard barreling up the stairs!")
     print_pause("before you are two rooms. no time to pick which room do you pick?")
     gf_choice()


#full basement scene done by yakubu
#slight adjustments to defines and calling those defines back work with main code done by rhys
def play_again():
    while True:
        again = input("Would you like to play again? (yes/no): ").lower()
        if again != 'yes':
            startgame()
            break
        else:
            print ("thank you for playing. goodbye")
            break

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
    enter_house()
 
def rusty_toolbox():
    print_pause("You grab the rusty toolbox and open it.")
    print_pause("Inside, you find a set of old, but sturdy tools.")
    print_pause("You quickly fashion a makeshift weapon and prepare to defend yourself.")
    print_pause("The bear charges at you, but you manage to fend it off with your improvised weapon.")
    print_pause("With the bear momentarily stunned, you make a run for the exit and escape!")
    enter_house()

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
   path_choice = input ("please enter go upstairs, go downstairs or walk coridoor")
   if path_choice == "go upstairs":
     stairs ()
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
