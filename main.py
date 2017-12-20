#!/usr/bin/env python3
# -*- coding: <utf-8> -*-
#  required commands
#  pip3 install numpy
#  pip3 install matplotlib


try:
    from numpy import exp, array, random, dot
    import numpy as np
except:
    print('Missing import\npip3 install numpy')
    
try:
    import matplotlib.pyplot as plt
except:
    print('Missing import\npip3 install matplotlib')
    print('sudo apt install python3-tk')
    
    
import utils
import sys
import brainData as BD
from os import system


#  Amount of learning iterations
#  50000 for a decent result
#  100000 for a 0.0001% offset result
trainAmount = 1000000  

#  matplotlib setup
#  uncomment for a fixed axis
#  may need to adapt axis values
##  plt.axis([0,trainAmount,0,1])
plt.xlabel('iteration')
plt.ylabel('guess')
plt.ion()

#  Quantity of training data to generate
#  100 is stable at 50000 iterations
#  200 is questionable at 50000 iterations
dataAmount = 100  

#  guess array
arrGuess = array([1, 0, 0, 1])
        
if __name__ == "__main__":
    try:
        utils.maker(dataAmount)
    
        #Seed the random number generator
        #random.seed(1)

        # Create layer 1 (5 neurons, each with 3 inputs)
        layer1 = BD.NeuronLayer(5, 4)

        # Create layer 2 (a single neuron with 4 inputs)
        # Output layer
        layer2 = BD.NeuronLayer(1, 5)

        # Combine the layers to create a neural network
        neural_network = BD.NeuralNetwork(layer1, layer2, arrGuess, trainAmount)

        print("\u001b[33mStage 1) Random starting synaptic weights: \u001b[0m")
        neural_network.print_weights(0)

        # The training set. We have 100 examples, each consisting of 3 input values
        # and 1 output value.
        training_set_inputs = array(utils.getData())
        training_set_outputs = array([utils.getAns()]).T

        # Train the neural network using the training set.
        # Do it X times and make small adjustments each time.
        neural_network.train(training_set_inputs, training_set_outputs, trainAmount)

        print("\u001b[33mStage 2) New synaptic weights after training: \u001b[0m")
        BD.neural_network.print_weights(trainAmount)
    
        print("Iterating " + str(trainAmount) + " times!!\n") 
    
        # Test the neural network with a new situation.
        print("\u001b[33mStage 3) Considering a new situation [1, 1, 0] -> ?: \u001b[0m")
        hidden_state, output = BD.neural_network.think(arrGuess)
        print("\u001b[33m"+str(output)+"\u001b[0m")
        
    except KeyboardInterrupt:
        system('clear')
        print('ZZZZZZZ AI Sleepy time')
