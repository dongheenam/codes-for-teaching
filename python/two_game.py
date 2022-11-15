""" counts the average number of rolls it takes to roll a 2 from a (d)-sided die 
    repeats the experiment (n) times """
import argparse
import os

import numpy as np

def trial(faces) :
    rounds = 0
    roll = 0
    while (roll != 2):
        roll = np.random.randint(1, high=faces+1)
        rounds += 1
    return rounds

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int, default=1000)
    parser.add_argument("-d", type=int, default=6)
    args = parser.parse_args()

    N = args.n          # number of throws
    faces = args.d      # number of faces

    hist = dict()
    for i in range(N) :
        rounds = trial(faces)
        if (rounds in hist) :
            hist[rounds] += 1
        else :
            hist[rounds] = 1

    rounds_max = np.max(list(hist.keys()))
    counts_max = np.max(list(hist.values()))
    terminal_width = os.get_terminal_size().columns
    BAR_LENGTH = np.min([terminal_width - 20, 50])

    i_med = N // 2
    cum_count = 0
    found_med = False

    print(f"rounds | prob (%) | histogram")
    for i in range(1, rounds_max+1) :
        count = hist[i] if i in hist else 0
        cum_count += count
        
        med_tick = " "
        if cum_count > i_med and not found_med :
            med_tick = "*"
            found_med = True

        prob = count / N
        bar = "*" * int(np.round(count / counts_max * BAR_LENGTH))
        print(f"{i:>6d}{med_tick}| {prob*100:>8.2f} | {bar}")
    
    total_trials = np.sum(np.array(list(hist.keys())) * np.array(list(hist.values())))

    print("=" * terminal_width)
    print(f"P(2) = {N/total_trials*100:.2f}%")
