# gym_10ARMG
This is question 2 of assignment 1 of CS698R course of IIT kanpur. </br>
In OpenAI Gym create the environment for 10-armed Gaussian Bandit. Make sure it is executing
as expected by creating certain test cases, e.g., by playing with σ. Report about your test cases and how
they point towards the correct implementation. You can also report about your general observations.


```
gym_10ARMG/
  README.md
  setup.py
  gym_10ARMG/
    __init__.py
    envs/
      __init__.py
      ARMG.py
      
```

```
from gym_10ARMG.ARMG import Ten_ARMG
import numpy as np
import matplotlib.pyplot as plt
episodes = 1000
bandits = 10
no_samples = 100        #no_of samples_per_bandit 
sigma = 1
p_dist = []              # propbablity distribution
r_dist = []              #reward distribution
Q = np.zeros([bandits])
N = np.zeros([bandits])
env = Ten_ARMG(sigma,bandits)
for i in range(bandits):
    p = env.prob_dist(no_samples,i)   # using i as a seed
    r_dist.append(env.rew_dist(np.mean(p),i))
for e in range(episodes):
    env.seed(e)                 #using episode as seed
    arm = np.random.randint(10)
    N[arm]+=1
    env.seed(e)
    reward = env.step(arm)
    Q[arm] = Q[arm] + (1/N[arm])*(reward-Q[arm])
    
#test plot

#sigma 0.1
import matplotlib.pyplot as plt
arms= np.arange(0,10,1)
plt.figure(figsize=(10,8))
plt.xlabel('arms')
plt.ylabel('Average reward over all episodes')
plt.ylim(-2,2)
plt.bar(arms,Q)

    
 ```
