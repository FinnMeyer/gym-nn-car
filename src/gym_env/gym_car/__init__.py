from gym.envs.registration import register

register(
    id='gym_car-v0',
    entry_point='gym_car.envs:gym_car',
)
