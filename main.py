import pygame
from world import World
from agent_002 import Agent

def run_game(world, agent):
    pygame.init()
    clocck=pygame.time.Clock()
    wn=pygame.display.set_mode((world.box_size*world.width , world.box_size*world.hight))
    pygame.display.set_caption("GRID_WORLD")

    state=True
    pause=False
    tick=80
    while (state and world.episode<world.max_episodes):
        if(world.episode==World.learning_episodes): 
            tick=1
            agent.exploration_trashold=0.9
            world.score=0
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                state=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p: pause = True
                if event.key == pygame.K_s: pause = False
        if(not pause):
                display_map(wn,world)
                display_score(wn,str(world.score))
                display_episodes(wn,str(world.episode))


                action=agent.action(world.agent_position, world.reward)
                world.next_state(action)
            
                if(world.is_end_of_episode):
                    pygame.display.update()
                    clocck.tick(tick)
                    display_map(wn,world)
                    display_score(wn,str(world.score))
                    display_episodes(wn,str(world.episode))
                    world.agent_position=world.get_first_position()
        else:
            agent.export_Q_table()
  

        pygame.display.update()
        clocck.tick(tick)
    print(world.score)
    agent.export_Q_table()
    pygame.quit()
    quit()
    


def display_score(wn,score):
    font=pygame.font.SysFont(None,30)
    text=font.render("Score="+score,True,(255,255,255))
    wn.blit(text,[0,0])

def display_episodes(wn,episodes):
    font=pygame.font.SysFont(None,30)
    text=font.render("Episode="+episodes,True,(255,255,255))
    wn.blit(text,[300,0])

def display_map(wn,world):
    for i in range(world.hight-1):
            for j in range(world.width-1):
                color=world.get_color_of_the_box(i,j)
                pygame.draw.rect(wn, color , (i*world.box_size,j*world.box_size,world.box_size,world.box_size))
    x=world.agent_position[0]*world.box_size+world.box_size/2
    y=world.agent_position[1]*world.box_size+world.box_size/2
    pygame.draw.circle(wn,agent.color,(x,y),world.box_size/2)
        

world=World()
agent=Agent(world.agent_position,(World.width,World.hight))
run_game(world,agent)



