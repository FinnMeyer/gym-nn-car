import tensorflow as tf
import utils.loading_util as lu
import utils.predict_util as pu
import os
import pandas as pd
import metadata as md
import numpy as np
import matplotlib.pyplot as mp
tf.compat.v1.enable_eager_execution()
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

a,b = pu.load()
c,d,end = pu.predict(a,b,213687,1295760 - 1, model_loc="./model/checkpoint0.0001-size of net:2.0-1-25.0-6-2023_09_06_15_31_10")
print(c)
print("bbb")
print(end)
c,d  = pu.scale(c,d )
pu.plot(c,d )