import gym
from gym import spaces
import numpy as np
import tensorflow as tf

import collections
class gym_car(gym.Env):
    """
    environment for a car
    """
    def __init__(self, on_data = False):
        self.episode_over = False
        self.action_space = gym.spaces.Box( low=np.array([0,0,0]),
                                            high=np.array([1,1,1]),
                                            dtype=np.float32)
        self.state = gym.spaces.Box(low=np.array([0,0,0,0,0,0,0]),
                                    high=np.array([1,1,1,1,1,1,1]),
                                    dtype=np.float32)
        self.observation_space = self.state
        self.reward_range = (-1, 1000)
        self.enviroment = [0,0,0,0]
        self.start = 0
        self.end = 20
        self.on_data = on_data
        self.prediction_result = []
        self.episode_over = False

        self.features_list = np.tile([0.57734869, 0.32467532, 0.0, 0.83006539, 0.37298294, 0.51479288, 0.47725798, 0.05580889, 0.16785174, 0.31493331, 0.28172293],6)
        self.action_list = np.tile([0.56341327, 0.17049577, 0.0],14)


        self.features_list = np.expand_dims(self.features_list, axis=0)
        self.action_list = np.expand_dims(self.action_list, axis=0)
        self.model = tf.keras.models.load_model("./model/checkpoint0.0001-size of net:2.0-1-25.0-6-2023_09_06_15_31_10")
        self.model.summary()

    #one prediction step
    def step(self, action):
        #if not run on real data the correct formating has to be done by the environment
        if self.on_data == False:
            if self.start != 0:
                self.features_list = np.roll(self.features_list, 11)
                pos = 55
                np.put(self.features_list, [pos + 0,pos + 1,pos + 2,pos + 3], self.enviroment)
                np.put(self.features_list, [pos + 4,pos + 5,pos + 6,pos + 7,pos + 8,pos + 9,pos + 10], self.prediction_result)

            self.action_list = np.roll(self.action_list, 3)
            np.put(self.features_list, [0,1,2], action)
        # if run on data the formating is already done by the data loader
        else:
            self.action_list = action
        #run the tensorflow model
        self.prediction_result = self.model([self.features_list,self.action_list])[0].numpy()

        # end episode after reaching goal state
        self.start = self.start + 1
        if self.start == self.end:
            self.episode_over = True

        # get reward
        reward =  np.random.random()

        # observation is state plus random noise
        # Note, only first entry in the state vector is actually informative
        ob = self.prediction_result
        return ob, reward, False, {}

        
    def set_data(self,on_data = False):
        """
        define if prediction should be on real data
        """
        self.on_data = on_data

    def set_features(self,features):
        """
        set the features if run on real data
        """
        self.features_list = features

    def reset(self,):
        """
        reset environment
        """
        self.state = np.zeros(7)
        self.state[0] = self.start
        return self.state

    def render(self, mode='human', close=False):
        pass

    def close(self):
        pass

    def seed(self, seed=None):
        pass
