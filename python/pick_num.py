import argparse

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__" :
  parser = argparse.ArgumentParser()
  parser.add_argument("n", type=int, default=100)
  args = parser.parse_args()

  sample_space = np.arange(1,11)
  n_cutoff = args.n
  n_even_sum = 0
  n_even_prod = 0

  while n_even_sum < n_cutoff :
    throw = np.random.choice(sample_space, 4, replace=False)
    if np.sum(throw) % 2 == 0 :
      n_even_sum += 1
      if np.product(throw) % 2 == 0 :
        n_even_prod += 1
      if n_even_sum % 100000 == 0 :
        print(f"{n_even_sum} throws found", end='\r')
  
  p = n_even_prod / n_even_sum
  stdev = np.sqrt(p * (1-p) / n_even_sum)
  print(f"throws with even sum    : {n_even_sum:10d}")
  print(f"throws with even product: {n_even_prod:10d}")
  print(f"P(even prod | even sum) : {n_even_prod/n_even_sum:10.4f}")
  print(f"standard error          : {stdev:10.4f}")
  