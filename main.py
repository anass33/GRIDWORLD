import pygame
from world import World
from agent import Agent

def run_game(world, agent):
    pygame.init()
    clocck=pygame.time.Clock()
    wn=pygame.display.set_mode((world.box_size*world.width , world.box_size*world.hight))
    pygame.display.set_caption("GRID_WORLD")


    state=True
    while (state and world.episode<world.max_episodes):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                state=False
        display_map(wn,world)
        display_score(wn,str(world.score))
        display_episodes(wn,str(world.episode))

        
        action=agent.action(world.agent_position, world.reward)
        world.next_state(action)

        pygame.display.update()
      
        clocck.tick(10)
    print(world.score)
    pygame.quit()
    quit()
    


def display_score(wn,score):
    font=pygame.font.SysFont(None,30)
    text=font.render("Score="+score,True,(255,255,255))
    wn.blit(text,[0,0])

def display_episodes(wn,episodes):
    font=pygame.font.SysFont(None,30)
    text=font.render("Episode="+episodes,True,(255,255,255))
    wn.blit(text,[100,0])

def display_map(wn,world):
    for i in range(world.hight-1):
            for j in range(world.width-1):
                color=world.get_color_of_the_box(i,j)
                pygame.draw.rect(wn, color , (i*world.box_size,j*world.box_size,world.box_size,world.box_size))
    x=world.agent_position[0]*world.box_size+world.box_size/2
    y=world.agent_position[1]*world.box_size+world.box_size/2
    pygame.draw.circle(wn,agent.color,(x,y),world.box_size/2)
        

world=World()
agent=Agent(world.agent_position)
run_game(world,agent)



