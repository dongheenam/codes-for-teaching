import argparse

import numpy as np

if __name__ == "__main__" :
  parser = argparse.ArgumentParser()
  parser.add_argument("n", type=int, default=1000)
  args = parser.parse_args()

  N = args.n  # number of trials
  faces = 8   # number of different colours
  packet_size = 13 # size of a single packet

  count = 0
  for i in range(N) :
    throw = np.random.randint(1, high=faces+1, size=packet_size)
    if all(np.isin(np.arange(1,faces+1), throw)) :
      count += 1
  print(f"throws: {N}")
  print(f"hits  : {count}")
  print(f"prob  : {count/N:.2e}")
