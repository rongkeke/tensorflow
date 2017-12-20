# _*_ coding: utf-8 _*_
# !/usr/bin/env python
import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# 创建一个变量, 初始化为标量 0.
state = tf.Variable(0, name="counter")

# 创建一个 op, 其作用是使 state 增加 1

one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)  # assign()操作是图所绘制的表达式的一部分，和add()方法一样，在调用run()执行表达式之前，
# 它并不会真正执行复制操作

# 启动图后, 变量必须先经过`初始化` (init) op 初始化,
# 首先必须增加一个`初始化` op 到图中.
init_op = tf.global_variables_initializer()

# 启动图, 运行 op
with tf.Session() as sess:
  # 运行 'init' op
  sess.run(init_op)
  # 打印 'state' 的初始值
  print sess.run(state)
  # 运行 op, 更新 'state', 并打印 'state'
  for _ in range(3):  #对初始的state状态循环增加三次1
    sess.run(update)
    print sess.run(state)
print '========下图是第二个程序========='
input1 = tf.constant(3.0)
input2 = tf.constant(2.0)
input3 = tf.constant(5.0)
intermed = tf.add(input2, input3)
mul = tf.multiply(input1, intermed)

with tf.Session() as sess:
  result = sess.run([mul, intermed])
  print result

# 输出:
# [array([ 21.], dtype=float32), array([ 7.], dtype=float32)]
print '======最后一个程序======='
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.multiply(input1, input2)
print input1
print input2
with tf.Session() as sess:
  print sess.run([output], feed_dict={input1: [7.], input2: [2.]})

# 输出:
# [array([ 14.], dtype=float32)]