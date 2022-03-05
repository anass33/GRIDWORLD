import random
class Agent:
    def __init__(self,pose):
        self.x=pose[0]
        self.y=pose[1]
        self.color=(151,79,171)
        self.score=0
        self.reward=0
    
  
    def action(self,position,reward):
        moves=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
        return random.choice(moves)