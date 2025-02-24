import time

items = [

]

rooms = [

]

def enter_house ():
   time.sleep(2)
   print ("you decide nobody is going to travel along the road, especially not at this time")
   time.sleep(2)
   print ("as you walk up to the house and step onto it's wooden porch")
   time.sleep(2)
   print ("the wood creaks and groans as though eager for it's next victim")
   time.sleep(2)
   print ("you knock on the door, the sound echoing through the empty house like thunder.")
   time.sleep(2)
   print ("the door swings open though there was nobody there")
   time.sleep(2)
   print ("reluctantly you enter the decrepid house.")
   time.sleep(2)
   print ("before you lies a long coridoor with various doors, a set of stairs along the wall heading to the top floor,")
   time.sleep(2)
   print ("and a set of stairs leading to the bowels of the house, the bottom near invisible as the darkness encases it.")
   time.sleep(2)
   print ("do you wish to go upstairs, go downstairs or walk the coridoor?")
   path_choice = input ("please enter go upstairs, go downstairs or walk coridoor")
   if path_choice == "go upstairs":
      upstairs ():
   elif path_choice == "go downstairs":

    def choice_1 ():
     path_choice = input ("please enter, enter the house or stay by car: ")
     if path_choice == "stay by car":
      time.sleep(2)
      print ("you decide to stay by your car not wanting to risk the creepy house.")
      time.sleep(2)
      print ("you wait all night with no cars passing by.")
      time.sleep(2)
      print ("when it turns to day you decide to try the forest in hopes of finding people")
      time.sleep(2)
      print ("you walk but there is nobody around.")
      time.sleep(2)
      print ("you hear a loud crash and in seconds it is over")
      time.sleep(2)
      print ("mauled by a bear you are not found, food for the wildlife.")
      time.sleep(2)
      print ("please try again. type y to try again and n to not")
      path_choice = input ("y or n: ")
      if path_choice == "y" or "Y":
        startgame()
      elif path_choice == "n" or " N":
        print ("thank you for playing")
     elif path_choice == "enter the house":
      enter_house()
     else:
      print ("please enter enter the house or stay by car: ")
      choice_1()
    
def startgame():
    time.sleep(2)
    print ("you are travelling down a road in the dead of night.")
    time.sleep(2)
    print ("besides you is a forest that stretches as far as the eye can see.")
    time.sleep(2)
    print ("suddenly your car breaks down and you quickly get out as smoke pours out of the front of the car.")
    time.sleep(2)
    print ("looking around you spot a derelict house.")
    time.sleep (2)
    print ("you see only 2 options for what to do in this situation.")
    time.sleep (2)
    print ("do you wish to enter the house in hopes of finding help for your predicament?")
    time.sleep(2)
    print ("or do you wish to stay by the car in hopes somebody travels down this rundown road?")


def print_pause(message):
    print(message)
    time.sleep(2)
 
def intro():
    print_pause("You find yourself in the dark, damp basement of an abandoned house.")
    print_pause("The air is thick with the smell of mold and rust.")
    print_pause("You hear a low growl behind you. Turning around, you see a massive bear!")
    print_pause("The bear is blocking the only exit. You need to find a way to escape!")
 
def choose_item():
    print_pause("You quickly scan the room and see two items:")
    print_pause("1. A rusty toolbox")
    print_pause("2. A crowbar")
    choice = input("Which item do you choose? (Enter 1 or 2): ")
    return choice
 
def rusty_toolbox():
    print_pause("You grab the rusty toolbox and open it.")
    print_pause("Inside, you find a set of old, but sturdy tools.")
    print_pause("You quickly fashion a makeshift weapon and prepare to defend yourself.")
    print_pause("The bear charges at you, but you manage to fend it off with your improvised weapon.")
    print_pause("With the bear momentarily stunned, you make a run for the exit and escape!")
 
def crowbar():
    print_pause("You grab the crowbar and feel its weight in your hands.")
    print_pause("The bear charges at you, and you swing the crowbar with all your might.")
    print_pause("You hit the bear square in the face, causing it to roar in pain.")
    print_pause("The bear retreats, giving you just enough time to sprint to the exit and escape!")
 
def bad_choice():
    print_pause("You hesitate and fail to choose an item in time.")
    print_pause("The bear lunges at you, and you are unable to defend yourself.")
    print_pause("Game over. You have been mauled by the bear.")
 
def play_game():
    intro()
    choice = choose_item()
    if choice == '1':
        rusty_toolbox()
    elif choice == '2':
        crowbar()
    else:
        bad_choice()
 
def play_again():
    while True:
        play_game()
        again = input("Would you like to play again? (yes/no): ").lower()
        if again != 'yes':
            print_pause("Thanks for playing! Goodbye!")
            break
 
play_again()

startgame()
