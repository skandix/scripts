#simple module to benchmark/  see how long it takes to run a function...
import time

def benchmark(data):
  start = time.time()
  data
  return ('it took {:} Seconds').format(time.time() - start) 
