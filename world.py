import random


class World:
    width=12
    hight=12
    map=[[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,5,0,0,0,-1,0,0,4,0,0,-1],
    [-1,-2,-1,0,-1,-1,-1,-1,-1,-1,0,-1],
    [-1,0,0,0,-1,0,0,0,-2,0,0,-1],
    [-1,0,-1,-1,-1,0,-1,0,0,0,0,-1],
    [-1,0,0,0,-1,0,-1,0,-1,-1,0,-1],
    [-1,-1,-1,0,-1,0,-1,0,0,0,0,-1],
    [-1,0,0,0,0,0,-1,-2,0,-1,0,-1],
    [-1,0,0,-1,-2,0,0,0,0,-1,2,-1],
    [-1,0,0,-1,0,0,0,1,0,-1,0,-1],
    [-1,3,0,0,0,0,0,0,0,0,0,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]
    max_episodes=4000
    learning_episodes=1200
    the_cost_of_action=0.2

    def __init__(self):
        self.flor_color=(255,255,255)
        self.wall_color=(0,0,0)
        self.reward_color_1=(175,219,195)
        self.reward_color_2=(50,168,74)
        self.reward_color_3=(1,56,12)
        self.reward_color_4=(158,156,152)
        self.reward_color_5=(235,174,52)
        self.enemy_color=(255,1,1)
        self.box_size=50
        self.agent_position=self.get_first_position()
        self.score=0
        self.reward=0
        self.episode=0
        self.is_end_of_episode=False
        self.moves=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
    
  



    def get_first_position(self):
        valid_x_y=False
        while valid_x_y==False:
            agent_x=random.randint(1,10)
            agent_y=random.randint(1,10)
            if(World.map[agent_x][agent_y]==0):
                valid_x_y=True
        return (agent_x , agent_y)

    def get_color_of_the_box(self,x,y):
        box_value=World.map[x][y]
        if( box_value==0): return self.flor_color
        if( box_value==-1):return self.wall_color
        if( box_value==-2): return self.enemy_color
        if( box_value==1): return self.reward_color_1
        if( box_value==2): return self.reward_color_2
        if( box_value==3): return self.reward_color_3
        if( box_value==4): return self.reward_color_4
        if( box_value==5): return self.reward_color_5

    def next_state(self,action):
        if(action in self.moves):
            reward=self.map[self.agent_position[0]-action[0]+action[2]][self.agent_position[1]-action[3]+action[1]]
            if(reward!=-1 ):
                self.agent_position=(self.agent_position[0]-action[0]+action[2],self.agent_position[1]-action[3]+action[1])
            if(reward!=-1 and reward!=0):
                 self.episode=self.episode+1
                 self.is_end_of_episode=True
            else:
                 self.is_end_of_episode=False
            reward=reward-World.the_cost_of_action
            self.reward=reward            
            self.score+=self.reward
            
    
            
    