from player import Player
from constants import *

class Location:
        def __init__(self, decribe, describe_long, loc_x, loc_y, unhide, north, south, west, east, digenable ,prize, multienable, multioptions):
                self.decribe = decribe 
                self.loc_x = loc_x
                self.loc_y = loc_y
                self.unhide = unhide
                self.north = north
                self.south = south
                self.west = west
                self.east = east 
                self.digenable = digenable
                self.prize = prize
                self.multienable = multienable
                self.multioptions = multioptions
                self.describe_long = describe_long
                

        def move(self, direction, currentloc):
                if direction == ('N')   and self.north == 1:
                        currentloc = currentloc + 1
                        return (currentloc)
                elif direction == ('S') and self.south == 1:
                        currentloc = currentloc - 1
                        return (currentloc)
                elif direction == ('E') and self.west == 1:
                        currentloc = currentloc - 1
                        return (currentloc)     
                elif direction == ('W') and self.east == 1:
                        currentloc = currentloc + 1
                        return (currentloc)
                else: 
                        print("You can not move in this direction!")
                        return (currentloc)     
                        
        def multichoice(self):
                if multienable:
                        print(multioptions)
                else:
                        print('No multiable choice')
        def jump(self,player,movecount,x,y):
                if x==50 and y==52:
                        player.bag.append("blue orb")
                        return('On top of the shelf you found a blue orb.  You put it in your bag for safekeeping',movecount,x,y)
                else:
                        if player.helmet==1:
                                return('You hit your head on the top of the ship but your helmet protected you.',movecount,x,y)
                        else:
                                player.health -= 10
                                return('You hit your head on the top of the ship and lost 10 healh points.',movecount,x,y)
        
        def openbox(self,player,movecount,x,y):
                        player.rad=4
                        return("You opened the cryosleep chamber and exposed yourself to deadly radiation!",movecount,x,y)
 
        def dig(self,player,movecount,x,y):
                if self.digenable == "yes" and self.prize != "none":
                        player.addprize(self.prize)
                        prizemessage = (f"You found a {self.prize}!!")
                        self.prize = "none"
                        return(prizemessage,movecount,x,y)
                elif self.digenable == "yes" and self.prize == "none":
                        return("Someone already dug in this spot!",movecount,x,y)
                else:
                        return("The ground is too hard to dig!",movecount,x,y)

        def insert_control_card(self,player,movecount,x,y):
                if "control card" in player.bag and "translator" in player.bag:
                        return("A message appears in the center of the bowl. It says 'We understand you have the prisoner on board.  Please be prepared to drop him off at prison planet zeta-3a.  We see you have set a course that brings you past the twin star system and through deep space.  We will monitor your progres while you are in cryosleep.",movecount,x,y)
                elif "control card" in player.bag:
                        return("A message appears in the center of the bowl. It says 'fh fhuirfherife fieiurhf hfih feiurhe hurie hhhih. foerfojij reofjieof oerifjf erofijerfoeijf   fjeri i.",movecount,x,y)
                else:
                        return("You don't have a control card.",movecount,x,y)
                
        def type_message(self,player,movecount,x,y):

                if "control card" in player.bag and "translator" in player.bag:
                        textmessage = input("A message appears in the center of the bowl.  It reads 'Respond To Central Command - '")
                        return(f"You communication reading '{textmessage}' failed.  The deep space communication network is currently offline",movecount,x,y)
                elif "control card" in player.bag:
                        textmessage = input("Text appears in the center of the bowl. The text reads 'jwefh hfur wuhfiuhf pjfoeur - '")
                        return(textmessage,movecount,x,y)
                else:
                        return("It appears you do not have the access to type on the screen",movecount,x,y)
        def look(self,player,movecount,x,y):
                if movecount >0 and movecount <10:
                        if x==50 and y ==55:
                                print(f"heads up diplay shows: {planetred}")
                        return("You see a red planet outside the window",movecount,x,y)
                elif movecount >=10 and movecount <20:
                        if x==50 and y ==55:
                                print(f"heads up diplay shows: {planetwhitestar}")
                        return("You see a white star outside the window",movecount,x,y)
                elif movecount >=20 and movecount <30:
                        if x==50 and y ==55:
                                print(f"heads up diplay shows: {planettwinstars}")
                        return("You see twin stars outside the window",movecount,x,y)
                elif movecount >=30 and movecount <40:
                        if x==50 and y ==55:
                                print(f"heads up diplay shows: {planetdeepspace}")
                        return("You see nothing but deep space outside the window",movecount,x,y)
                elif movecount >=40 and movecount <50:
                        if x==50 and y ==55:
                                print(f"heads up diplay shows: {planetdeepspace}")
                        return("You see nothing but deep space outside the window",movecount,x,y)
                elif movecount >=50 and movecount<60:
                        if x==50 and y ==55:
                                print(f"heads up diplay shows: {planetblueandwhite}")
                        return("You seem to be approaching a blue and white planet",movecount,x,y)
                elif movecount >=60 and movecount<70:
                        if x==50 and y ==55:
                                print(f"heads up diplay shows: {planetblueandwhite}")
                        return("You see a blue and white planet outside the window",movecount,x,y)
                elif movecount >=70 and movecount<80:
                        if x==50 and y ==55:
                                print(f"heads up diplay shows: {planetblueandwhite}")
                        return("You seem to be heading away from a blue and white planet",movecount,x,y)
                elif movecount >=90 and movecount<100:
                        return("You see many Audacians ships outside the window",movecount,x,y)
                        if x==50 and y ==55:
                                print(f"heads up diplay shows: {planetaudacian}")
                else: 
                        return("You see many Audacians ships outside the window",movecount,x,y)
                


        def press_green_button(self,player,movecount,x,y):
                if x==54:
                        x=46
                        player.health = player.health - 10
                        return ("You see a bright flash of white light and your head feel light",movecount,x,y)
                        
                if x==46:
                        x=54
                        player.health = player.health - 10
                        return ("You see a bright flash of white light and your head feel light",movecount,x,y)
        
        def press_red_button(self,player,movecount,x,y):
                if "blue orb" in player.bag:
                        x=10
                        y=10
                        return ("You have activated the escapepod",movecount,x,y)
                else:
                        return ("You hear a loud horn and the green button flashes blue for a moment.",movecount,x,y)

        def set_coordinates(self,player,movecount,x,y):
                selected=input("Please enter three digit Cord:")
                if movecount >50 and movecount <90 and selected =="413":
                        x=10
                        y=11
                        return("You have set a course for the white and blue planet",movecount,x,y)
                elif selected =="413":
                        return("The Screen Reads 'This planet is too far away.'",movecount,x,y)
                else:
                        movement=100
                        return("The screen indicates 'The cord you have selected will take over 100 years, location no possible.'",movecount,x,y)
                
        def open_airlock(self,player,movecount,x,y):
                if player.rad==1:
                        x=50
                        y=45
                        return("The airlock opens and you step out.",movecount,x,y)
                else:
                        player.rad=3
                        return("You have left the ship without a radiation suit.",movecount,x,y)

        def move_heatshield(self,player,movecount,x,y):
                player.heatshield=1
                return("You have successfully moved the heatshield to the escape pod.",movecount,x,y)

        def jettison_heat_shield(self,player,movecount,x,y):
                if x==10 and y==11 and player.heatshield==1:
                        x=10
                        y=12
                        return("You have successfully jettisoned the heatshield",movecount,x,y)
                elif player.heatshield==0:
                        player.heatshield=4
                        return("No heatshield was attached to the ecscape pod.  The lever does nothing.",movecount,x,y)

                else:
                        player.heatshield=3
                        return("You have jettisoned the heatshield too early.  The tempature begins to rise.",movecount,x,y)
        def deploy_drouge(self,player,movecount,x,y):
                if x==10 and y==12:
                        x=10
                        y=13
                        return("You have successfully deployed the drouge.  Your speed slows.",movecount,x,y)
                else:
                        player.drouge=1
                        return("Drouge deployed without heatshield removal.",movecount,x,y)
        def open_hatch(self,player,movecount,x,y):
                if player.rad==0:
                        player.rad=5
                        return("The Hatch Opens.",movecount,x,y)
                if player.beaconenable > 50 and player.health > 70:
                        x=10
                        y=14
                        return("The Hatch Opens.",movecount,x,y)
                else:
                        player.health=0
                        player.rad=4
                        return("You have waited several days but it appears noone is coming to rescue you and your health is too low.",movecount,x,y)
                        
