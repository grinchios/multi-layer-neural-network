#!/usr/bin/env python3
# -*- coding: <utf-8> -*-
#  required commands
#  pip3 install numpy
from numpy import exp, array, random, dot
import obtainer
import sys

trainAmount = 1000000  #  Amount of learning iterations
dataAmount = 100  #  Quantity of training data to generate

class NeuronLayer():
    def __init__(self, number_of_neurons, number_of_inputs_per_neuron):
        self.synaptic_weights = 2 * random.random((number_of_inputs_per_neuron, number_of_neurons)) - 1


class NeuralNetwork():
    def __init__(self, layer1, layer2):
        self.layer1 = layer1
        self.layer2 = layer2

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
        for iteration in range(number_of_training_iterations):
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

            # Calculate how much to adjust the weights by
            layer1_adjustment = training_set_inputs.T.dot(layer1_delta)
            layer2_adjustment = output_from_layer_1.T.dot(layer2_delta)

            # Adjust the weights.
            self.layer1.synaptic_weights += layer1_adjustment
            self.layer2.synaptic_weights += layer2_adjustment
            
            #  Display weight information for all layers, and make an estimate at this stage
            if iteration % 5000 == 0 and iteration != 0:
                #self.print_weights(iteration)
                hidden_state, output = neural_network.think(array([1, 1, 0]))
                print("\u001b[33m"+str(output)+"\u001b[0m\n")
                
    # The neural network thinks.
    def think(self, inputs):
        output_from_layer1 = self.__sigmoid(dot(inputs, self.layer1.synaptic_weights))
        output_from_layer2 = self.__sigmoid(dot(output_from_layer1, self.layer2.synaptic_weights))
        return output_from_layer1, output_from_layer2

    # The neural network prints its weights
    def print_weights(self,iteration):
        print("\u001b[33mSynaptic weights after "+ str(iteration) +" iterations\u001b[0m")
        sys.stdout.write("\u001b[36m    Layer 1 (4 neurons, each with 3 inputs): \n")
        sys.stdout.write(str(self.layer1.synaptic_weights)+('\n'))
        sys.stdout.write("    Layer 2 (1 neuron, with 4 inputs):\n")
        sys.stdout.write(str(self.layer2.synaptic_weights)+'\n')
        sys.stdout.write('\u001b[0m\n')

if __name__ == "__main__":

    obtainer.maker(dataAmount)
    
    #Seed the random number generator
    #random.seed(1)

    # Create layer 1 (4 neurons, each with 3 inputs)
    layer1 = NeuronLayer(4, 3)

    # Create layer 2 (a single neuron with 4 inputs)
    layer2 = NeuronLayer(1, 4)

    # Combine the layers to create a neural network
    neural_network = NeuralNetwork(layer1, layer2)

    print("\u001b[33mStage 1) Random starting synaptic weights: \u001b[0m")
    neural_network.print_weights(0)

    # The training set. We have 100 examples, each consisting of 3 input values
    # and 1 output value.
    training_set_inputs = array(obtainer.getData())
    training_set_outputs = array([obtainer.getAns()]).T

    # Train the neural network using the training set.
    # Do it X times and make small adjustments each time.
    neural_network.train(training_set_inputs, training_set_outputs, trainAmount)

    print("\u001b[33mStage 2) New synaptic weights after training: \u001b[0m")
    neural_network.print_weights(trainAmount)
    
    print("Training " + str(trainAmount) + " times!!\n") 
    
    # Test the neural network with a new situation.
    print("\u001b[33mStage 3) Considering a new situation [1, 1, 0] -> ?: \u001b[0m")
    hidden_state, output = neural_network.think(array([1, 1, 0]))
    print("\u001b[33m"+str(output)+"\u001b[0m")
