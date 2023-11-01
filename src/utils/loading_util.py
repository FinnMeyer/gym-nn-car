import tensorflow as tf
import numpy as np
import os
from os import listdir
from os.path import isfile, join
from numpy import genfromtxt
import metadata as md
tf.compat.v1.enable_eager_execution()


def load_scaling():
    onlyfiles = [f for f in listdir("./min_max_for_tf_record/") if isfile(join("./min_max_for_tf_record/", f))]
    listData= []
    for f in onlyfiles:
        e = "./min_max_for_tf_record/" + f
        listData.append(e)
    for count, file in enumerate(listData):
        if count == 0:
            my_data1 = genfromtxt(file,delimiter=' ',dtype=None)
        else:
            my_data = genfromtxt(file, delimiter=',')
            my_data1 = np.vstack((my_data1, my_data))

    my_data1 = my_data1[~np.isnan(my_data1).any(axis=1)]
    min_value = my_data1.min(axis=0)
    min_value[13] = -30.0
    scaling_max = tf.constant(my_data1.max(axis=0), dtype=tf.float32)   
    scaling_min = tf.constant(min_value, dtype=tf.float32)
    return scaling_min, scaling_max
