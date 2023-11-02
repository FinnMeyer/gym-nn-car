import gym
import gym_env.gym_car
import matplotlib.pyplot as mp
max_steps = 25
scaling_max = [4.035e+03, 8.200e-01, 6.428e+01, 1.372e+03, 3.313e+02, 1.598e+02, 7.308e+01]
scaling_min = [-2.472e+03, -8.700e-01, -5.884e+01,  0.000e+00,  0.000e+00, -2.462e+01, -3.000e+01]

observation_list = []
results = [[],[],[],[],[],[],[]]
env = gym.make('gym_car-v0')
o = env.reset()
total_reward = 0
for t in range(max_steps):
    #action = env.action_space.sample()
    action = [0.57734869, 0.57, 0.3]
    observation, reward, done, info = env.step(action)
    observation_list.append(observation)
    
    total_reward += reward
    if done or t + 1 == max_steps:
        for j in range(0,len(observation_list)):

            for i in range(0,7):
                scaled = (observation_list[j][i] * (scaling_max[i]-scaling_min[i])) + scaling_min[i]
                results[i].append(scaled)
        print("Episode finished after {:3} timesteps with total reward {:3.1f}".format(t+1, total_reward))
        
title = ["Torque", "Lat. acceleration", "Yaw rate", "Temp front left", "Temp rear left", "Velocity", "Acceleration"]
for i in range(0,7):
    mp.subplot(2, 4, i+1)
    mp.plot(results[i])
    mp.gca().set_title(title[i]) 
mp.show()