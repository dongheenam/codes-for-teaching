import argparse

import numpy as np
from scipy.special import factorial

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("n_max", type=int, default=5)
    args = parser.parse_args()

    n_max = args.n_max          # upper limit of n for the sum

    print(f"calculating Sum of 1/n! from n=0 to {n_max}")
    e_sum = np.sum([1/factorial(n) for n in range(n_max)])
    print(f"result: {e_sum}")
    