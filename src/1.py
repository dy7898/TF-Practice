import tensorflow as tf

print("aa")

hello = tf.constant("Hello!")
sess = tf.Session()

print(sess.run(hello))
