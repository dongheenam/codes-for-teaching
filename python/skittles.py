""" measures the chance of having all (n_colors) colors of skittles
    in a packet of (packet_size) skittles by opening up (n) packets """
import argparse

import numpy as np

if __name__ == "__main__" :
  parser = argparse.ArgumentParser()
  parser.add_argument("n", type=int, default=1000)
  args = parser.parse_args()

  N = args.n  # number of trials
  n_colors = 8   # number of different colours
  packet_size = 13 # size of a single packet

  count = 0
  for i in range(N) :
    throw = np.random.randint(1, high=n_colors+1, size=packet_size)
    if all(np.isin(np.arange(1,n_colors+1), throw)) :
      count += 1
  print(f"number of packets        : {N}")
  print(f"packets with all colours : {count}")
  print(f"probability              : {count/N*100:.2f}%")
