import random
class Agent:
    def __init__(self,pose):
        self.curent_position=pose
        self.color=(151,79,171)
        self.score=0
        self.reward=0
        self.avoid_list=[]
        self.latest_position=pose
    
  
    def action(self,position,reward):
        moves=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
        self.curent_position=position
        if(reward<-1):
            self.avoid_list.append(self.latest_position)
        not_valid = True
        while not_valid:

            move=random.choice(moves)

            if(move==(1,0,0,0)):
                next_position=(position[0]-1, position[1])
            if(move==(0,1,0,0)):
                next_position=(position[0], position[1]+1)
            if(move==(0,0,1,0)):
                next_position=(position[0]+1, position[1])
            if(move==(0,0,0,1)):
                next_position=(position[0], position[1]-1)

            not_valid = next_position in self.avoid_list
        
        self.latest_position=next_position
        return move