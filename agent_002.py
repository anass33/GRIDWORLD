import random
import numpy as np
import pandas as pd 

class Agent:
    def __init__(self,pose,map_dimensions):
        self.map_dimensions=map_dimensions
        self.curent_position=pose
        self.latest_position=pose
        self.latest_move=(0,0,0,0)
        self.color=(0, 98, 255)
        self.score=0
        self.reward=0
        #self.Q_table=np.zeros((map_dimensions[0],map_dimensions[1] , 4))
        self.Q_table=self.read_Q_table()
        self.learning_rate=0.2
        self.discount_rate=0.99
        self.exploration_trashold=0.001
        self.episodes=0
        


        self.moves=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
    
  
    def action(self,position,reward):
        print("===========================================")
        print("state= ")
        print(position)
        print("reward=")
        print(reward)
        print("exploration_trashold=")
        print(self.exploration_trashold)

        self.curent_position=position
        self.reward=reward
        self.score+=reward
        
        if(self.latest_move!=(0,0,0,0)):
   
                print("q-table-last-position avant modif")
                print(self.Q_table[self.latest_position[0],self.latest_position[1]])

                self.Q_table[self.latest_position[0],self.latest_position[1],self.get_move_index(self.latest_move)]= self.Q_table[self.latest_position[0],self.latest_position[1],self.get_move_index(self.latest_move)]*(1-self.learning_rate)\
                    +self.learning_rate*(reward+ self.discount_rate*np.max(self.Q_table[self.the_expected_position(self.latest_move,self.latest_position[0],self.latest_position[1])[0],self.the_expected_position(self.latest_move,self.latest_position[0],self.latest_position[1])[1],:]))

                print("q-table-last-position apres modif")
                print(self.Q_table[self.latest_position[0],self.latest_position[1]])
                
        if(self.is_exploring()):
                    move=random.choice(self.moves)
        else:
                    move=self.moves[np.argmax( self.Q_table[position[0],position[1],:])]
                    print("q-table-courante-position")
                    print(self.Q_table[position[0],position[1]])
                    
        print("the move selected is:")
        print(move)
        self.latest_position=position
        self.latest_move=move


        if(reward>0 or reward< -1.5):
            self.episodes+=1
            self.exploration_trashold=1-np.exp(1- self.episodes/300)
            self.latest_position=(0,0)
            self.latest_move=(0,0,0,0)
        return move
    

    def is_exploring(self):
        if(random.uniform(0,1)>self.exploration_trashold):
            return True
        else: 
            return False


    def get_move_index(self,move):
        if(move==(1,0,0,0)):
           return 0
        if(move==(0,1,0,0)):
           return 1
        if(move==(0,0,1,0)):
            return 2
        if(move==(0,0,0,1)):
            return 3

    def the_expected_position(self,move,x,y):
        return (x-move[0]+move[2], y+move[1]-move[3])
    

    def export_Q_table(self):
        a=np.resize(self.Q_table,(self.map_dimensions[0]*self.map_dimensions[1] , 4))
        pd.DataFrame(a).to_csv("Qtable.csv",header=False, index=False)
    
    def read_Q_table(self):
        df=pd.read_csv("Qtable.csv")
        a=df.to_numpy()
        a=np.resize(a,(self.map_dimensions[0],self.map_dimensions[1] , 4))
        return a

   