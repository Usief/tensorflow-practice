import tensorflow as tf

# matrix1 = tf.constant([[3., 3.]])
#
# matrix2 = tf.constant([[2.], [2.]])
#
# product = tf.matmul(matrix1, matrix2)
#
# sess = tf.Session()
# result = sess.run(product)
#
# print (result)
#
# sess.close()


# with tf.Session as sess:
#     result = sess.run([product])
#     print (result)

# with tf.Session() as sess:
#     with tf.device("/cpu:0"):
#         matrix1 = tf.constant([[3., 3.]])
#
#         matrix2 = tf.constant([[2.], [2.]])
#
#         product = tf.matmul(matrix1, matrix2)
#         result = sess.run([product])
#         print (result)

# sess = tf.InteractiveSession()
#
# x = tf.Variable([1.0, 2.0])
# a = tf.constant([3.0, 3.0])
#
# x.initializer.run()
#
# sub = tf.subtract(x, a)
# print (sub.eval())

input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.multiply(input1, input2)

with tf.Session() as sess:
    print (sess.run([output], feed_dict={input1:[7.], input2:[2.]}))