#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 12:11:57 2018

@author: tom
estimate the optimal value function using dynamic programming
in particular, equation (3.19) from S&B
note: all p() are deterministic in this case
"""
import numpy as np
np.set_printoptions(precision=4, suppress = True)

def state2rc(state_pass = 1):  # state to (row, column)
    return state_pass // 5, state_pass % 5

def succ(state_pass = 1, action_pass = 1): # successor function
    row, column = state2rc(state_pass)
    if action_pass == 0:
        row -= 1
    elif action_pass == 1:
        column += 1
    elif action_pass == 2:
        row += 1
    else:
        column -= 1
    return row, column    
    
nstates = 25
value = np.random.random((5,5))
ntrials = 100
gamma = 0.9
stop, converge, threshold, max_iteration = False, False, 0.005, 100

# start to iterate
#print(value)
iteration = 0
while stop == False:
    previous_value = value + 0
    iteration += 1
    for state in range(nstates):
        row, column = state2rc(state)
        total_v = []
        for action in range(4):
            action_prob = 1/4 # random policy
            if (row==0) & (column==1):
                action_v = 10+gamma*previous_value[state2rc(21)]
            elif (row==0) & (column==3):
                action_v = 5+gamma*previous_value[state2rc(13)]
            elif (column==0) & (action==3):
                action_v = -1+gamma*previous_value[state2rc(state)]
            elif (column==4) & (action==1):
                action_v = -1+gamma*previous_value[state2rc(state)]
            elif (row==0) & (action==0):
                action_v = -1+gamma*previous_value[state2rc(state)]
            elif (row==4) & (action==2):
                action_v = -1+gamma*previous_value[state2rc(state)]
            else:
                action_v = 0+gamma*previous_value[succ(state,action)]
            total_v.append(action_v)
        value[row,column] = max(total_v)
    if np.mean(np.abs(value-previous_value))<threshold:
        converge = True
        stop = True
    elif iteration>max_iteration:
        stop = True
    else:
        pass
    
# show what you did
print("n iterations = {0}; stopping criterion was{1}reached".format(iteration, [" not ", " "][converge]))
print(value)