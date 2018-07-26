#!/usr/bin/env python3
# -*- coding: <utf-8> -*-

import configparser
config = configparser.ConfigParser()
config.read('database/neuralNetwork.ini')

try:
    from numpy import exp, array, random, dot
    import numpy as np
except:
    print('Missing import\npip3 install numpy')

display = config.getboolean('graph', 'display')

if display is True:
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print('Missing import\npip3 install matplotlib')
        print('sudo apt install python3-tk')

import brainData as BD
from os import system
from src import utils

#  Amount of learning iterations
#  50000 for a decent result
#  100000 for a 0.0001% offset result
trainAmount = config.getint('main.py', 'trainAmount')

#  matplotlib setup
#  change ini for a fixed axis
#  may need to adapt axis values
if display is True:
    #  more graph setup
    plt.xlabel('iteration')
    plt.ylabel('guess')
    plt.ion()

if config.getboolean('main.py', 'seeding') is True:
    # Seed the random number generator
    random.seed(config.getint('main.py', 'seedvalue'))

#  retrain will mean the old neuron data
#  will be used, training in advance is possible
retrain = config.getboolean('main.py', 'retrain')

#  Quantity of training data to generate
#  100 is stable at 50000 iterations
#  200 is questionable at 50000 iterations
dataAmount = config.getint('main.py', 'dataAmount')

#  guess array
arrGuess = array([0, 0, 0, 1])

if __name__ == "__main__":
    try:
        utils.maker(dataAmount)

        # Create layer 1 (5 neurons, each with 4 inputs)
        layer1 = BD.NeuronLayer(5, 4)

        # Create layer 2 (a single neuron with 5 inputs)
        # Output layer
        layer2 = BD.NeuronLayer(1, 5)

        # Combine the layers to create a neural network
        neural_network = BD.NeuralNetwork(layer1, layer2, arrGuess, trainAmount)

        if retrain is False:
            neural_network.readNeurons()

        print("\u001b[33mStage 1) Random starting synaptic weights: \u001b[0m")
        neural_network.print_weights(0)

        # The training set. We have 100 examples, each consisting of 3 input values
        # and 1 output value.
        training_set_inputs = array(utils.getData())
        training_set_outputs = array([utils.getAns()]).T

        # Train the neural network using the training set.
        # Do it X times and make small adjustments each time.
        neural_network.train(training_set_inputs, training_set_outputs, trainAmount)

        print("\u001b[33mNew synaptic weights after training: \u001b[0m")
        neural_network.print_weights(trainAmount)
    
        print("Iterating " + str(trainAmount) + " times!!\n") 
    
        # Test the neural network with a new situation.
        print("\u001b[33mFinished! Considering a new situation " + str(arrGuess) + "\u001b[0m")
        hidden_state, output = neural_network.think(arrGuess)
        print("\u001b[33m"+str(output)+"\u001b[0m")
        
    except KeyboardInterrupt:
        system('clear')
        print('ZZZZZZZ AI Sleepy time')
        neural_network.saveNeurons()

