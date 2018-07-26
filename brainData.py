#!/usr/bin/env python3
# -*- coding: <utf-8> -*-

from numpy import exp, random, dot, save, load
from os import system
import sys
import configparser
from src import utils

#  output debug data
config = configparser.ConfigParser()
config.read('database/neuralNetwork.ini')

debug = config.getboolean('debug', 'debug')
display = config.getboolean('graph', 'display')

if display is True:
    import matplotlib.pyplot as plt

class NeuronLayer():
    def __init__(self, number_of_neurons, number_of_inputs_per_neuron):
        self.synaptic_weights = 2 * random.random((number_of_inputs_per_neuron, number_of_neurons)) - 1


class NeuralNetwork():
    def __init__(self, layer1, layer2, guess, limit):
        self.layer1 = layer1
        self.layer2 = layer2
        self.arrGuess = guess
        self.trainAmount = limit

    # The Sigmoid function, which describes an S shaped curve.
    # We pass the weighted sum of the inputs through this function to
    # normalise them between 0 and 1.
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    # The derivative of the Sigmoid function.
    # This is the gradient of the Sigmoid curve.
    # It indicates how confident we are about the existing weight.
    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    # We train the neural network through a process of trial and error.
    # Adjusting the synaptic weights each time.
    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for self.iteration in range(number_of_training_iterations):
            # Pass the training set through our neural network
            output_from_layer_1, output_from_layer_2 = self.think(training_set_inputs)

            # Calculate the error for layer 2 (The difference between the desired output
            # and the predicted output).
            layer2_error = training_set_outputs - output_from_layer_2
            layer2_delta = layer2_error * self.__sigmoid_derivative(output_from_layer_2)

            # Calculate the error for layer 1 (By looking at the weights in layer 1,
            # we can determine by how much layer 1 contributed to the error in layer 2).
            layer1_error = layer2_delta.dot(self.layer2.synaptic_weights.T)
            layer1_delta = layer1_error * self.__sigmoid_derivative(output_from_layer_1)

            # Calculate how much to adjust the weights byFalse
            layer1_adjustment = training_set_inputs.T.dot(layer1_delta)
            layer2_adjustment = output_from_layer_1.T.dot(layer2_delta)

            # Adjust the weights.
            self.layer1.synaptic_weights += layer1_adjustment
            self.layer2.synaptic_weights += layer2_adjustment
            
            outputs = self.iteration % 5000 == 0 and self.iteration != 0
            if outputs is True:
            
                #  output weights and a guess at current iteration
                self.print_weights(self.iteration)
                hidden_state, output = self.think(self.arrGuess)
                print("\u001b[33m"+str(output)+"\u001b[0m\n")
            
                #  Display weight information for all layers, and make an estimate at this stage
                if (outputs and debug and display) is True:

                    #  add current guess to graph
                    plt.plot(self.iteration, output, '-o')
                    plt.show()
                    plt.pause(0.001)

            utils.progress(self.iteration, number_of_training_iterations, status="I'm thinking...")

    #  Saves the current neurons of the system and other critical information
    def saveNeurons(self):
        save('database/layer1', self.layer1.synaptic_weights)
        save('database/layer2', self.layer2.synaptic_weights)
        config.set('main.py', 'trainDepth', str(self.iteration))
        print(self.iteration)
        config.write(open('database.neuralNetwork.ini','w'))

    #  Uses numpy to load the files back into the neurons
    def readNeurons(self):
        self.layer1.synaptic_weights = load('database/layer1.npy')
        self.layer2.synaptic_weights = load('database/layer2.npy')

    # The neural network thinks.
    def think(self, inputs):
        output_from_layer1 = self.__sigmoid(dot(inputs, self.layer1.synaptic_weights))
        output_from_layer2 = self.__sigmoid(dot(output_from_layer1, self.layer2.synaptic_weights))
        return output_from_layer1, output_from_layer2

    # The neural network prints its weights
    def print_weights(self,iteration):
        system('clear')
        sys.stdout.write("\u001b[33mSynaptic weights after " + str(iteration) + " iterations\u001b[0m")
        sys.stdout.write("\u001b[36m\nLayer 1 (5 neurons, each with 4 inputs): \n")
        sys.stdout.write(str(self.layer1.synaptic_weights) + '\n')
        sys.stdout.write("\nLayer 2 (1 neuron, with 5 inputs):\n")
        sys.stdout.write(str(self.layer2.synaptic_weights) + '\n')
        sys.stdout.write('\u001b[0m\n')
