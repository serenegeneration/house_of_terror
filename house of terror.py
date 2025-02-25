import time

items = [

]

rooms = [

]
#this neat little feature added by yakubu
def print_pause(message):
    print(message)
    time.sleep(2)



def coridoor():
   print_pause ("")
   print_pause ("")
   print_pause ("")
#full basement scene done by yakubu
#slight adjustments to work with main code done by rhys
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
     upstairs ()
   elif path_choice == "go downstairs" and rooms ("basement") == 0:
    basement()
   elif path_choice == "go downstairs" and rooms ("basement") == 1:
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
