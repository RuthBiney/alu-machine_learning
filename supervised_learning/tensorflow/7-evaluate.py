#!/usr/bin/env python3
'''
    function def evaluate(X, Y, save_path):
    that evaluates the output of a neural network:
'''


import tensorflow as tf


def evaluate(X, Y, save_path):
    '''
        that evaluates the output of a neural network:
    '''
    with tf.Session() as sess:
        saver = tf.train.import_meta_graph(save_path + '.meta')
        saver.restore(sess, save_path)
        Y_pred = tf.get_collection('y_pred')[0]
        accuracy = tf.get_collection('accuracy')[0]
        cost = tf.get_collection('cost')[0]
        accuracy = sess.run(accuracy, feed_dict={
            'x': X, 'y': Y, 'keep_prob': 1.0
        })
        cost = sess.run(cost, feed_dict={
            'x': X, 'y': Y, 'keep_prob': 1.0
        })
        Y_pred = sess.run(Y_pred, feed_dict={
            'x': X, 'keep_prob': 1.0
        })
        return Y_pred, accuracy, cost
