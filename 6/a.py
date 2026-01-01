import time
from math import prod

def process(problem: tuple) -> int:
  """Operator as str in [0], values as ints in [1:]."""
  match problem[0]:
    case '+':
      return sum(problem[1:])
    case '*':
      return prod(problem[1:])
  return 0

def main():
  """Solution for Advent of Code 2025, 6A."""
  # Start timing once we're in main(). Initialization of variables is included.
  start_time = time.perf_counter()

  # Show your work here.

  # init
  result = 0
  numbers = []
  operators = []
  lines = []

  # read input
  with open("a.in", 'r') as input_file:
    lines = input_file.read().splitlines()

  # parse input
  numbers = [[int(x) for x in line.split()] for line in lines[:-1]]
  operators = lines[-1].split()

  # do the math
  result = sum([process(x) for x in zip(operators, *numbers)])

  # End timing once we have the result.
  end_time = time.perf_counter()

  # Output result - do not include printing in time measurement.
  print(f"Result: {result}")
  calc_time = end_time - start_time
  print(f"Calculation time: {calc_time:.4f} seconds")

if __name__ == "__main__":
  main()
