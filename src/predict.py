import tensorflow as tf
import utils.predict_util as pu
import os
import gym
import gym_env.gym_car
env = gym.make('gym_car-v0')
o = env.reset()
env.set_data(on_data=True)
tf.compat.v1.enable_eager_execution()
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

input, result = pu.load("2_14.csv")
predictions,reference ,end, reward = pu.predict(env, input, result, 213687, len(result))
print("reward:" + str(reward))
predictions, reference = pu.scale(predictions, reference)
pu.plot(predictions, reference)