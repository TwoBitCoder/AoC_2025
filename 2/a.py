import time

def fix_start(value: str) -> str:
  """Return smallest integer >= value with even length."""
  num_digits = len(value)
  if 0 == num_digits % 2:
    return value
  return '1'+'0'*num_digits

def fix_end(value: str) -> str:
  """Return largest integer <= value with even length."""
  num_digits = len(value)
  if 0 == num_digits % 2:
    return value
  return '9'*(num_digits-1)

def analyze_range(range_str: str) -> int:
  """Expected input is a string of the format /(\\d+)-(\\d+)/
     \\1 is the start of the range.
     \\2 is the end of the range.
     Goal is to find all values within the range that match /^(\\d+)\\1$/
     Output is the sum of all such values' integer representation."""

  # Initial conditions
  (range_start_str, range_end_str) = range_str.split('-')
  range_start = fix_start(range_start_str)
  range_end = fix_end(range_end_str)
  if int(range_end) < int(range_start):
    return 0
  result = 0

  # Find values that repeat
  starter = int(range_start[0:len(range_start)//2])
  finisher = int(range_end[0:len(range_end)//2])
  result = sum([int(str(x)*2) for x in range(starter, finisher+1)])
  first = int(str(starter)*2)
  if first < int(range_start):
    result -= first
  last = int(str(finisher)*2)
  if last > int(range_end):
    result -= last

  # Output
  return result

def main():
  """Solution for Advent of Code 2025, 2A."""

  start_time = time.perf_counter()

  # Initial conditions
  invalid_sum = 0

  # Read and process input file
  with open("a.in", 'r') as input_file:
    for input_line in input_file:
      for id_range in input_line.split(','):
        invalid_sum += analyze_range(id_range)

  end_time = time.perf_counter()

  # Output result
  print(f"Result: {invalid_sum}")
  calc_time = end_time - start_time
  print(f"Calculation time: {calc_time:.4f} seconds")

if __name__ == "__main__":
  main()
