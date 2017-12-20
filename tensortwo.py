# _*_ coding: utf-8 _*_
# !/usr/bin/env python
import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
sess = tf.InteractiveSession()

x = tf.Variable([1.0, 2.0])
a = tf.constant([3.0, 3.0])

x.initializer.run()  # 使用初始化器的run方法初始化x
sub = tf.subtract(x, a)  # 用x矩阵检出a矩阵

print sub.eval()
