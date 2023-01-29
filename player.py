class Player:
        def __init__(self,  username, loc_x, loc_y, starting_dabloon,bag,health,cord,rad,heatshield,beaconenable,drouge,helmet):
                self.username = username
                self.loc_x = loc_x
                self.loc_y = loc_y
                self.starting_dabloon = starting_dabloon
                self.bag = bag
                self.health = health
                self.cord=cord
                self.rad=rad
                self.heatshield=heatshield
                self.beaconenable=beaconenable
                self.drouge=drouge
                self.helmet=helmet

        def addprize(self,prize):
                self.bag.append(prize)
                

        



