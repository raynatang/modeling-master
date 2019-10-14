#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
@author: Pieter
Pieter.Huycke@UGent.be

- - - - - - - - - - - - 

Stuck using a function?
No idea about the arguments that should be defined?

Type:
help(module_name)
help(function_name)
to let Python help you!
"""


#%%

# -------------- #
# IMPORT MODULES #
# -------------- #

import ch0_delta_learning as delta_learning
import numpy              as np

# alter print options for numpy: suppress scientific printing 
np.set_printoptions(suppress=True)

#%%

# ------------------------------------------ #
# LEARN ASSOCIATION BETWEEN LIGHT AND CHEESE #
# ------------------------------------------ #

# define inputs
light          = np.array([1, 0])
light_and_tone = np.array([1, 1])
salivating     = np.array([1])

# define a weight matrix exclusively filled with zeros
weight_matrix = delta_learning.initialise_weights(light, 
                                                  salivating, 
                                                  zeros      = True,
                                                  predefined = False, 
                                                  verbose    = False)
   
# actual learning
loops = 1000
alpha = 1.5
    
for loop_var in np.arange(1, loops + 1):
    weights_after_learning = delta_learning.weight_change(alpha,
                                                          light,
                                                          salivating,
                                                          weight_matrix)
    weight_matrix = weights_after_learning
    
# show that the light leads to the desired response
activation_after_learning = delta_learning.internal_input(light,
                                                          weight_matrix)[0]
print('\nActivation of output unit after {} trials of delta learning:\n'.format(loops), 
      np.round(activation_after_learning, 3))

#%%

# make a copy of the original weight matrix
weight_matrix_light = np.copy(weight_matrix)

# ------------------------------------------------- #
# LEARN ASSOCIATION BETWEEN LIGHT + TONE AND CHEESE #
# ------------------------------------------------- #
  
# actual learning
loops = 1000
alpha = 1.5
    
for loop_var in np.arange(1, loops + 1):
    weights_after_learning = delta_learning.weight_change(alpha,
                                                          light_and_tone,
                                                          salivating,
                                                          weight_matrix)
    weight_matrix = weights_after_learning
    
# show that the light leads to the desired response
activation_after_learning = delta_learning.internal_input(light,
                                                          weight_matrix)[0]
print('\nActivation levels at output after {} trials of delta learning:\n'.format(loops), 
      np.round(activation_after_learning, 3))