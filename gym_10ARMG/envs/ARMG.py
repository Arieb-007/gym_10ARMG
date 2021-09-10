from gym import spaces
import numpy as np
from gym.utils import seeding
import gym

class Ten_ARMG(gym.Env):
    
    def __init__(self,sigma,bandits):
        self.sigma = sigma               #standard deviation
        self.bandits = bandits
        self.action_space = np.arange(bandits)
        
    
    def prob_dist(self,no_samples_per_arm,bandit):
        p_dist = []         
        for n in range(no_samples_per_arm):
            seed_ = n + bandit
            self.seed(seed_)
            p_dist.append(np.random.normal(0,self.sigma))
        return p_dist
    
    def rew_dist(self,q_mean,seed):
        rew_dist = []
        np.random.seed(seed)
        return np.random.normal(q_mean,self.sigma)

    def step(self,action):
      return np.random.normal(r_dist[action],self.sigma)
        
            
            
    def seed(self,seed):
        np.random.seed(seed)
        
