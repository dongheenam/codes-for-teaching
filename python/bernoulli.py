""" 
calculates the chance of failing a Bernoulli trial with n-sided dice
"""
import argparse

import numpy as np

def trial(n) :
    trials = np.random.uniform(size=n)
    successes = trials < (1/n)
    return any(successes)

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("d", type=int, nargs="?", default=200, help="number of sides of the dice")
    parser.add_argument("trials", type=int, nargs="?", default=300000, help="number of trials for the simulation")
    args = parser.parse_args()

    d = args.d              # number of experiments for each trial (p = 1/n)
    trials = args.trials    # number of trials

    print(f"For each trial, a {d}-sided die is thrown {d} times.")
    print(f"The trial succeeds if 1 is rolled at least once.")
    successes = 0
    fails = 0
    for i in range(trials) :
        if (trial(d)) :
            successes += 1
        else :
            fails += 1
    print("===================================================")
    print(f"Number of trials: {trials}")
    print(f"successes       : {successes}")
    print(f"fails           : {fails}")
    print(f"P(fail)         : {fails/trials}")
    print(f"1/P(fail)       : {trials/fails}")
    print("===================================================")
