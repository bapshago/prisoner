#original author alex apshago january 15 2023
#prisoner author bapshago January 29 2023
#Alex's Dad's version of her original code for choose your own adventure game
#v1.2


#global constants
debug=0
global currentloc_x 
currentloc_x = int(50)
global currentloc_y 
currentloc_y = int(50)
global radiationsuiton
radiationsuiton = 0

#imports
from constants import *
from os import system, name
from time import sleep
from room import Location
from player import Player

#core functions
def clear():
        if name =='nt':
                _ = system('cls')
        else:
                _ = system('clear')

def startingscreen():
        print("")
        print("If you want to learn more about the game controls, please type 'Help'")
        print("---------------------------------------------------------------------")
        print(introduction)
        controls(1)

def createplayer():
        player = Player(username, 50,50,0,["rope"],100,111,0,0,0,0,0)
        return(player)

def controls(updatelocation):
        global currentloc_y
        global currentloc_x
        global movecounter
        global radiationsuiton
        #control when and how a player dies
        movecounter +=1
        movescheck(movecounter)
       
        combinedlocation_var = "location" + str(currentloc_x) + str(currentloc_y)
        currentroommove = combinedlocation_var + ".move"
        currentroomdescribe_long = combinedlocation_var + ".describe_long"
        currentroomdescribe = combinedlocation_var + ".decribe"
        currentroomdig = combinedlocation_var + ".dig"
        currentroommultichoice = combinedlocation_var + ".multienable"
        currentroommultichoiceopt = combinedlocation_var + ".multioptions"
        currentroomprize = combinedlocation_var + ".prize"

        if updatelocation==1 or str(eval(combinedlocation_var + ".unhide")) == "1":
                print("")
                print(f"-----------   {(eval(currentroomdescribe))}   ----------")
                print("")
                print(eval(currentroomdescribe_long))
                print("")
                #if room has special functions display those
                if eval(currentroommultichoice):
                        print("The following are special actions for this area " , *eval(currentroommultichoiceopt), sep = " : ")
                        print("")
                #if room has objects display those
                if len(eval(currentroomprize)) != 0:
                        print("The following items are in this room " , *eval(currentroomprize),sep =" : ")
                        print("")

        
        #monitors player health and will warn then kill the player
        healthcheck()
        
        airlockcheck(radiationsuiton)
        if player.rad==3:
                gameover(3)
        if player.rad==4:
                gameover(5)
        if player.heatshield==3:
                gameover(6)
        if player.drouge==(1):
                gameover(7)
        if player.heatshield==4:
                gameover(8)
        if player.rad==5:
                gameover(9)

                
        if debug == 1:print(f"This room has {currentroomdebloons} dabloons in it.")
        if debug == 1:print(f"debug: {currentloc_x, currentloc_y}")

        control=input('? ')
        control=control.lower()

        if control=="inventory":
                print(f"Your current items are:")
                print(*player.bag,sep='\n')
                controls(0)
        elif control == 'map':
                print(f'Current location is {currentloc_x, currentloc_y}.')
                showmap()
                controls(0)
        elif control == "up": 
                newcurrentloc_y = eval(currentroommove)('N', currentloc_y) 
                currentloc_y = newcurrentloc_y
                controls(1)
        elif control == "down": 
                newcurrentloc_y = eval(currentroommove)('S', currentloc_y) 
                currentloc_y = newcurrentloc_y
                controls(1)      
        elif control == "left": 
                newcurrentloc_x = eval(currentroommove)('E', currentloc_x) 
                currentloc_x = newcurrentloc_x
                controls(1)      
        elif control == "right": 
                newcurrentloc_x = eval(currentroommove)('W', currentloc_x) 
                currentloc_x = newcurrentloc_x
                controls(1)              

        elif control=='help':
                print("")
                print("Commonly used commands")
                print("'Inventory' - shows you your items in your bag")
                print("'Health' - shows you your health status")
                print("'Moves' - shows your remaining moves")
                print("'Fire' - fires the weapon")
                print("'Map' -  a map that gives you your x and y coordinates")
                print("'Pick' - allows player to pick up item")
                print("'Drop' - allows player to drop an item")
                print("'Eat' - allows player to eat an item from bag")
                print("'Sleep' - allows player to rest")
                print("'Don' - allows player to put on clothing")
                print("'Remove' - allows a playee to remove a item of clothing")
                print("'Enablebeacon' - activates your emergency beacon.")
                print("'Up' - moves player up") 
                print("'Down' -  moves player down")
                print("'Left' - moves player left")
                print("'Right' - moves player right")   
                print("'Help' - shows player list of commands")
                controls(0)
                
        elif control=='health':
                print("")
                print(f"Your Current Health Status is {player.health}")
                controls(0)

        elif control=='moves':
                remainingmoves = deathtime - movecounter
                print(f".............Remaining Moves {remainingmoves}...............")
                controls(0)

        elif control=='pick':
                if len(player.bag)>7:
                        print("Your bag is too full.  Nothing more will fit!")
                        controls(0)
                else:
                        print("")
                        if len(eval(currentroomprize)) == 0:
                                print("Nothing to pick.")
                                controls(0)                       
                        else:
                                itemtopick = input("What would you like to pickup?")
                                if itemtopick.lower() in eval(currentroomprize):
                                        if itemtopick.lower()=="heatshield":
                                                print(f"The {itemtopick} is way to large for your bag.")
                                                controls(0)
                                        else:
                                                player.bag.append(itemtopick)
                                                eval(currentroomprize).remove(itemtopick)
                                                print(f"The {itemtopick} is now in your bag.")
                                                controls(0)
                                else:
                                        print("Sorry that item is not in this room.")
                                        controls(0)

        elif control=='eat':
                print("")
                if len(player.bag) == 0:
                        print("Nothing to eat.")
                        controls(0)                       
                else:
                        print(*player.bag,sep='\n')
                        print("")
                        itemtoeat = input("What would you like to eat?")
                        if itemtoeat.lower() in player.bag and itemtoeat.lower() == "food":
                                player.bag.remove(itemtoeat)
                                player.health = player.health + 10
                                print("That was tasty and you feel a little better.")
                                controls(0)
                        elif itemtoeat.lower() in player.bag:
                                player.health = player.health - 10
                                print(f"That was nasty and you couldn't get any of the {itemtoeat} down.  You feel worse then before.")
                                controls(0)

                        else:
                                print("Sorry that item is not in your bag.")
                                controls(0)
        elif control=='sleep':
                 player.health = player.health + 10
                 movecounter = movecounter + 5
                 print("You wake up rested but some time has past.")
                 controls(0)
                 
        elif control=='enablebeacon':
                 if "emergency beacon" in player.bag:
                         if player.beaconenable > 0:
                                 print(f"Your emergency beacon has already been enabled.  The screen reads 'Enabled At {player.beaconenabled}'")
                                 controls(0)
                         elif movecounter <= 60:
                                 print("The screen on the beacon reads 'Base Station Out of Range. Please try again later'")
                                 controls(0)
                         elif movecounter > 60:
                                 print("The screen on the beacon reads 'You Have Activated Your Emergency Beacon.'")
                                 player.beaconenable = movecounter
                                 controls(0)
                 print("You dont have an emergency beacon in your bag.")
                 controls(0)
                                
        elif control=='drop':
                print("")
                if len(player.bag) == 0:
                        print("Nothing to drop.")
                        controls(0)                       
                else:
                        print("Here is what is in your bag:")
                        print(*player.bag,sep='\n')
                        print("")
                        itemtodrop = input("What would you like to drop?")
                        if itemtodrop.lower() in player.bag:
                                player.bag.remove(itemtodrop)
                                eval(currentroomprize).append(itemtodrop)
                                print(f"The {itemtodrop} has been removed from your bag.")
                                controls(0)
                        else:
                                print("Sorry that item is not in your bag.")
                                controls(0)
        elif control=='fire':
                print("")
                if len(player.bag) == 0:
                        print("Bag is empty")
                        controls(0)                       
                else:
                        if "weapon" in player.bag and currentloc_x == 49 and currentloc_y == 50:
                                print(f"The weapon damaged the port engine reactors.  The ship has stopped motion.")
                                controls(0)
                        if "weapon" in player.bag and currentloc_x == 48 and currentloc_y == 50:
                                gameover(4)
                        elif "weapon" in player.bag:
                                print(f"The weapon fired, but did not cause damage.  You can feel a slight tingle in your ears.")
                                player.health = player.health - 10
                                controls(0)
                        else:
                                print("No weapon in your bag.")
                                controls(0)
        elif control=='don':
                print("")
                if len(player.bag) == 0:
                        print("Nothing to wear.")
                        controls(0)                       
                else:
                        print(*player.bag,sep='\n')
                        print("")
                        itemtowear = input("What would you like to wear?")
                        if itemtowear.lower() in player.bag and itemtowear.lower() == "helmet" and player.helmet == 0:
                                player.bag.remove(itemtowear)
                                player.helmet = 1
                                print("The helmet is now on your head.")
                                controls(0)
                        
                        elif itemtowear.lower() in player.bag and itemtowear.lower() == "helmet" and player.helmet == 1:
                                print("The helmet is already on.")
                                controls(0)
                                
                        elif itemtowear.lower() in player.bag and itemtowear.lower() == "radiation suit" and radiationsuiton == 0:
                                player.bag.remove(itemtowear)
                                radiationsuiton = 1
                                player.rad = 1
                                player.health = player.health + 40
                                print("The suit is heavy but it feels safe.")
                                controls(0)

                        elif itemtowear.lower()=="radiation suit" and radiationsuiton == 1:
                                print("The suit is already on.")
                                controls(0)
                                
                        elif itemtowear.lower() in player.bag:
                                player.health = player.health - 10
                                print(f"You can't wear a {itemtowear}")
                                controls(0)

                        else:
                                print("Sorry that item is not in your bag.")
                                controls(0)
        elif control=='remove':
                print("")
                if player.helmet == 0 and radiationsuiton == 0:
                        print("Nothing to remove.")
                        controls(0)                       
                else:
                        itemtoremove = input("What would you like to remove?")
                        if itemtoremove.lower() == "helmet" and player.helmet==1:
                                player.bag.append(itemtoremove)
                                player.helmet = 0
                                print("The helmet is now in your bag.")
                                controls(0)
                                
                        elif itemtoremove.lower() == "radiation suit" and player.rad ==1:
                                player.bag.append(itemtoremove)
                                radiationsuiton = 0
                                player.rad = 0
                                player.health = player.health - 40
                                print("Your don't feel as well as you did with the suit on.  Your suit is in your bag.")
                                controls(0)

                        else:
                                print(f"You do not have a {itemtoremove} on.")
                                controls(0)

        #this statement must be the last elif please do not put choices below this or they won't work
        #this will allow additional room specific functions if available.  
        elif eval(currentroommultichoice):
                for options in (eval(currentroommultichoiceopt)):
                        if options == control:
                                currentroommultichoiceoptchoice = ("location" + str(currentloc_x) + str(currentloc_y) + "." + str(options))
                                execution,movecounter,currentloc_x,currentloc_y = eval(currentroommultichoiceoptchoice)(player,movecounter,currentloc_x,currentloc_y)
                                print(execution)
                                controls(0)
                                
                print('This is not a valid command!')
                controls(0)
        else:
                print("")
                print("This is not a valid command!")
                controls(0)


def showmap():
        print("     45  46  47  48  49  50  51  52  53  54  55")
        print("56                       ")
        print("55                      [FS]")
        print("54                      [ST]")
        print("53                      [ST]")
        print("52                      [ST]")
        print("51                      [WT]")
        print("50  {EP}[TR][SR][AR][PE][CR][SE][KT][CC][SE]")
        print("49                      [SH]")
        print("48                      [LQ]")
        print("47                      [SE]")
        print("46                      [AL]")
        print("45")
        print(f"moves: {movecounter}")
        
def checkdablooninput(input_str):
        if input_str.strip().isdigit():
                return True
        else:
                return False


def movescheck(moves):
        if moves >= deathtime:
                gameover(1)

def healthcheck():
                if player.health < 0:
                        gameover(2)
                elif player.health < 15:
                        print("Your health is very low, seek health points as soon as possible")
                else:
                        return()

def gameover(reason):
        if reason==1:
                print("You didn't make it.  You ran out of time.  The Audacians made it to there home planet and you have been imprisoned for life.")
        elif reason==2:
                print("You didn't make it.  You health was too low.")
        elif reason==3:
                print("You didn't make it.  Opening the airlock exposed you to the harsh space environment and you couldn't survive.")
        elif reason==4:
                print("You didn't make it.  Firing the weapon in the airlock caused an explosion and destoryed the ship.")
        elif reason==5:
                print("You didn't make it.")
        elif reason==6:
                print("You didn't make it. The heatshield was jettisoned too early and you died in a firey crash!")
        elif reason==7:
                print("You didn't make it. The drouge was deployed too early and you died when you hit the ground.")
        elif reason==8:
                print("You didn't make it. The escape pod did not have a heatshield and you died in a firey crash!")
        elif reason==9:
                print("You didn't make it. The planet surface containd too much radiation.")
                
        else:
                print("You didn't make it.  You died from unknown causes")

        sleep(5)     
        quit()

def airlockcheck(rad):
        if rad == 0 and currentloc_x == 50 and currentloc_y == 45:
                gameover(3)

                
#all functions defined above this line

#main program function

if __name__ == "__main__":

        clear()
        print('Hello user! Welcome to the game.')
        username=input('What is your name? ' )
        print(f'Welcome {username}.')

        #center hub
        location5050=Location('Control Room',loc5050_describe ,50,50,0,1,1,1,1,"no",[],1,['insert_control_card', 'type_message','jump'])

        #port spoke
        location4950=Location('Port Engine Room', loc4950_describe,49,50,0, 0, 0, 1, 1,"no",["control card"],1,['jump'])
        location4850=Location('Armory', loc4850_describe,48,50,0, 0, 0, 1, 1,"no",["weapon"],1,['jump'])
        location4750=Location('Storage Room Alpha', loc4750_describe,49,50,0, 0, 0, 1, 1,"no",["translator","helmet","id badge","toolkit","emergency beacon"],1,['jump'])
        location4650=Location('Transporter Room P', loc4650_describe,46,50,0, 0, 0, 1, 1,"no",[],1,['press_green_button','jump'])
        location4550=Location('Escape Pod', loc4550_describe, 45,50,0, 0, 0, 0, 1,"no",[],1,['look','press_red_button'])
                              

        #starboard spoke
        location5150=Location('Starboard Engine Room', loc5150_describe,51,50,0, 0, 0, 1, 1,'yes',['gem'],1, ['jump'])
        location5250=Location('Kitchen',loc5250_describe,51,50,0, 0, 0, 1, 1,'yes',['food'],1, ['jump'])
        location5350=Location('Cryosleep Chamber', loc5350_describe,51,50,0, 0, 0, 1, 1,'yes',[],1, ['openbox'])
        location5450=Location('Transporter Room S', loc5450_describe,51,50,0, 0, 0, 1, 0,'yes',[],1, ['press_green_button',"jump"])


        #Top spoke
        location5051=Location('Water Tank Room',loc5051_describe,50,51,0, 1, 1, 0, 0,"no",[], 1,['jump'])
        location5052=Location('Ship Tunnel',loc5052_describe,50,51,0, 1, 1, 0, 0,"no",[], 1,["jump"])
        location5053=Location('Ship Tunnel',loc5053_describe,50,51,0, 1, 1, 0, 0,"no",[], 1,["jump"])
        location5054=Location('Ship Tunnel',loc5054_describe,50,51,0, 1, 1, 0, 0,"no",[], 1,["jump"])
        location5055=Location('Front Of Ship',loc5055_describe,50,51,0, 0, 1, 0, 0,"no",[], 1,["look","jump"])
                              

        #Bottom spoke
        location5049=Location('Shop',loc5049_describe,50,49,0, 1, 1, 0, 0,"yes",['axe','locked tool box','hammer','project parts'],1,"")
        location5048=Location('Living Quarters', loc5048_describe,50,48,0, 1, 1, 0, 0,"yes",["key"],1, ['jump','look'])
        location5047=Location('Spacewalk Equipment Room',loc5047_describe,50,47,0, 1, 1, 0, 0,"no",["radiation suit"],1,['jump'])
        location5046=Location('Air Lock',loc5046_describe,50,46,0, 1, 0, 0, 0,"no",[], 1, ['open_airlock'])
        location5045=Location('Outside Airlock',loc5045_describe,50,45,1, 1, 0, 0, 0,"no",['heatshield'], 1, ['move_heatshield','look'])

        #escape pod
        location1010=Location('Traveling In Escape Pod',loc1010_describe,10,10,1, 0, 0, 0, 0,"no",[], 1, ['set_coordinates','jettison_heat_shield','deploy_drouge'])

        #white and blueplanet
        location1011=Location('White and Blue Planet - On Route',loc1011_describe,10,10,1, 0, 0, 0, 0,"no",[], 1, ['jettison_heat_shield','deploy_drouge'])
        location1012=Location('White and Blue Planet - Throught Atmosphere',loc1012_describe,10,10,1, 0, 0, 0, 0,"no",[], 1, ['deploy_drouge'])
        location1013=Location('White and Blue Planet - On Surface',loc1013_describe,10,10,1, 0, 0, 0, 0,"no",[], 1, ['open_hatch'])
        location1014=Location('Back On Earth',username + " " + loc1014_describe,10,10,1, 0, 0, 0, 0,"no",[], 0, [])
        
        player = createplayer()
        startingscreen()
