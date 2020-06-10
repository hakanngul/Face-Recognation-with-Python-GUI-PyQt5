import os
import tensorflow as tf
import numpy as np

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

a = tf.Variable(np.array([0, 1, 2]))

print(a)