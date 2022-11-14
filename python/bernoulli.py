""" meausres the chance of at least one success from (n_exp) experiments, 
    with chance of success = 1/(n_exp),
    by repeating the trial (n_trial) times """
import argparse

import numpy as np

def trial(n) :
    trials = np.random.uniform(size=n)
    successes = trials < (1/n)
    return any(successes)

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("n_exp", type=int, nargs="?", default=200)
    parser.add_argument("n_trials", type=int, nargs="?", default=30000)
    args = parser.parse_args()

    n_exp = args.n_exp          # number of experiments for each trial (p = 1/n)
    n_trials = args.n_trials    # number of trials

    print(f"For each trial, {n_exp} experiments are conducted.")
    print(f"Probability of success is 1/{n_exp}.")
    successes = 0
    fails = 0
    for i in range(n_trials) :
        if (trial(n_exp)) :
            successes += 1
        else :
            fails += 1
    print("===================================================")
    print(f"Number of trials: {n_trials}")
    print(f"successes       : {successes}")
    print(f"fails           : {fails}")
    print(f"P(fail)         : {fails/n_trials}")
    print(f"1/P(fail)       : {n_trials/fails}")
    print("===================================================")