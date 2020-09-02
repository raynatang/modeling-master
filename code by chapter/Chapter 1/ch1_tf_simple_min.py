#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 09:25:08 2020

@author: tom verguts
simple function minimization with TensorFlow
"""

import tensorflow as tf
import numpy as np

epochs = 10
learning_rate = 0.1
initial_value = 3

X = tf.Variable(np.random.randn(1, 1).astype(np.float32), name="X")

cost = tf.reduce_sum((X-3)**2)
opt  = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)
init = tf.global_variables_initializer()
init_val= tf.compat.v1.assign(X, [[initial_value]]) # choose initial value


with tf.Session() as sess:
    sess.run(init)
    sess.run(init_val)
    for epoch in range(epochs):
        sess.run(opt, feed_dict = {})
        x = sess.run(X)
        print("x = {:.2f}".format(x[0][0]))