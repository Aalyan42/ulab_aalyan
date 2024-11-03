#Nuclear Radioactive Decay Simulator

import numpy as np


def decay_amount(initial_amount, decay_constant, time):

    #using the exponential decay formula to find the amount substance left given the initial amount, time passed, and decay constant
    substance_left = initial_amount * np.exp(-1 * decay_constant * time)
    
    return substance_left

def find_half_life (decay_constant):

    #finding the half-life of a substance, where the half life is defined as ln(2) / decay constant

    half_life = np.log(2) / decay_constant

    return half_life


def decay_simulator(isotopes, time_ints):

    #here, we're gonna take a list of isotopes (2D-array), and see how they decay over time

    #initialize emtpy results list
    results = []

    for time in time_ints:
        for isotope in isotopes:

            #had to do this to get the index to start from one, couldnt see if it was doing multiple indexes and which was which 
            isotope_index = isotopes.tolist().index(list(isotope)) + 1 
            

            initial_amount, decay_constant = isotope 
            #basically saying each isotope is a list of 2 elements 
            remaining_substance = decay_amount(initial_amount, decay_constant, time)
            if remaining_substance <= 0.01 * initial_amount:
                remaining_substance = 0
            #checking if amount left is 1% or less, if it is saying its all gone. in this case 1% is our threshold

            results.append([f"Time: {time} years, Isotope {isotope_index}: {remaining_substance} units remaining"])

            results.append([time, remaining_substance])
            #adding the amount left after each time int
    return (results)

#defining function to help split results into readable lines, lots of nested 4 loops
def print_results(results):
    for result in results:
        for line in result:
            print(line)
        print()
