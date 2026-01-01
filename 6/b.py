import time
from math import prod

def process(problem: tuple) -> int:
  """Operator as str in [0], values as list in [1].
     Small modification from 6A due to alternate input format."""
  match problem[0]:
    case '+':
      return sum(problem[1])
    case '*':
      return prod(problem[1])
  return 0

def main():
  """Solution for Advent of Code 2025, 6B.
     Input has not changed, but copied to b.in anyway."""
  # Start timing once we're in main(). Initialization of variables is included.
  start_time = time.perf_counter()

  # Show your work here.

  # init
  result = 0
  numbers = []
  operators = []
  lines = []

  # read input
  with open("b.in", 'r') as input_file:
    lines = input_file.read().splitlines()

  # parse input
  # Effectively need a matrix transpose operator for the lines containing the numbers, then groups are split by lines that are entirely whitespace.
  number_lines = lines[:-1]
  number_strs = [''.join(x).strip() for x in zip(*number_lines)]
  number_group = []
  for num in number_strs:
    if num == "":
      numbers.append(number_group)
      number_group = []
    else:
      number_group.append(int(num))
  numbers.append(number_group)
  operators = lines[-1].split()

  # do the math
  # don't expand the numbers list for this problem - the numbers are already grouped
  result = sum([process(x) for x in zip(operators, numbers)])

  # End timing once we have the result.
  end_time = time.perf_counter()

  # Output result - do not include printing in time measurement.
  print(f"Result: {result}")
  calc_time = end_time - start_time
  print(f"Calculation time: {calc_time:.4f} seconds")

if __name__ == "__main__":
  main()
