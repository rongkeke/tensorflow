# _*_ coding: utf-8 _*_
# !/usr/bin/env python
import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
'''
maxtrix1 = tf.constant([[3., 3.]])
maxtrix2 = tf.constant([[2.], [2.]])
product = tf.matmul(maxtrix1, maxtrix2)
sess = tf.Session()  # session 会记录上下文中执行图
result = sess.run(product)

print product
print result

sess.close()
'''
with tf.Session() as sess:
  with tf.device("/cpu:0"):
    matrix1 = tf.constant([[3., 3.]])
    matrix2 = tf.constant([[2.], [2.]])
    product = tf.matmul(matrix1, matrix2)
    result = sess.run(product)
    print result
'''

'''