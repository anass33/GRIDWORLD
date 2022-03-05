# GRIDWORLD
This is a programing game, in which every player create an agent that will be playing on his behalf, and try to maximize its score by collecting as many as possible rewards and avoiding enemies.

The project consists of three entities 
The environement (the world) : that manage the mape , the score , and the agent position.
An agent : that based on a giving position and a giving reward , should take an action by moving eather to left , right , top, or bottom.
The main: is where theas classes are implimented and where the map is drawn.

Every player should create it's own agent , that must contain the method action that return the action to take , based on two parameters , the current position and the reward collected from it.

The game will be run for a specific number of episodes ( max_episodes ), for each agent separately , and the agent who comes out with the biggest score wins the game.

The map may contain:
  - Empty box: white boxs in witch the agent may enter if it is next to it, the agent get no rewards and the episode continue.
  - Walls : they are black boxs in witch the agent may not enter, the agent position stays the same before the taken the step, and it gets no rewards and the episode continue.
  - Enemy box: red box, when the agent enters it, the episode ends, the score gets decreased by two points and the agent get relocated randomly into a new empty box.
  - Reward box: its color depends on the value of its reward, the reward varies from 1 to 5, when the agent enters a reward box the score is increased by the value of the reward, the episode ends and the agent is relocated.
 
