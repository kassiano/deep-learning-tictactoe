import numpy as np


def sigmoid(x, deriv =False):
    if(deriv == True):
        return (x*(1-x))

    return 1/( 1 + np.exp(-x))


def forward_pass(x, weights, bias):
    return bias + np.dot(x, weights)


def train_network(inputs, targets , learn_rate, n_epoch):
    weights = [0.0 for i in range(len(inputs[0]))]
    bias = 0

    for e in range(n_epoch):
        sum_error = 0.0

        for X, y in zip(inputs, targets):

            h = forward_pass(X, weights, bias)
            #output = activation(h)
            output = sigmoid(h)

            error = y - output
            sum_error += error**2
            bias = bias + learn_rate * error

            for i in range(len(X)):
                weights[i] = weights[i] + learn_rate * error * X[i]


        if e % (epochs / 10) == 0:
            print('>epoch=%d, lrate=%.3f, error=%.3f' % (e, learn_rate, sum_error))

    return weights, bias


def load_dataset():
    dataset = [  [[1,1,1],[0,0,0],[0,0,0]] ]
