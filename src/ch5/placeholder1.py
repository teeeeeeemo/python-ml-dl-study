import tensorflow as tf

a = tf.placeholder(tf.int32, [3])
b = tf.constant(2);
x2_op = a * b;

sess = tf.Session()

r1 = sess.run(x2_op, feed_dict={ a:[1, 2, 3] })
print(r1)
r2 = sess.run(x2_op, feed_dict={ a:[10, 20, 10] })
print(r2)
