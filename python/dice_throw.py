import argparse

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__" :
  parser = argparse.ArgumentParser()
  parser.add_argument("-d", type=int, default=6)
  parser.add_argument("n", type=int, default=100)
  args = parser.parse_args()

  N = args.n          # number of throws
  faces = args.d      # number of faces

  throws = np.random.randint(1, high=faces+1, size=N)
  print("Roll | Frequency | Probability")
  for i in range(1, faces+1) :
    count = (throws == i).sum()
    print(f"{i:4d} | {count:9d} | {count/N*100:10.2f}%")