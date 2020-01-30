# p635
# 2020-01-30

import sys
import queue

def series():
  last = 1983
  yield last % 10000 + 1
  while True:
    last = (last*214013+2531011) % (2**32)
    yield last % 10000 + 1

def ITES(k, n):
  q = queue.Queue()
  s = series()
  sum = 0
  count = 0
  
  for head in range(0, n):
    signal = s.__next__() 
    sum += signal
    q.put(signal)
    while sum > k:
      sum -= q.get()
    if sum == k:
      count += 1
  return count

if __name__ == '__main__':
  print(ITES(int(sys.argv[1]), int(sys.argv[2])))