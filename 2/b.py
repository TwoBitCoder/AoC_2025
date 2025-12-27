import time

def analyze_range(range_str: str) -> int:
  """Expected input is a string of the format /(\\d+)-(\\d+)/
     \\1 is the start of the range.
     \\2 is the end of the range.
     Goal is to find all values within the range that match /^(\\d+)\\1$/
     Output is the sum of all such values' integer representation."""

  # Initial conditions
  (range_start_str, range_end_str) = range_str.split('-')
  range_start = int(range_start_str)
  range_end = int(range_end_str)
  invalids = set()


  # Find values that repeat
  start_len = len(range_start_str)
  end_len = len(range_end_str)
  # l is total str length
  for l in range(start_len, end_len+1):
    max_rep_len = l // 2
    # n is length of repeated token
    for n in [x+1 for x in range(max_rep_len)]:
      if 0 < l % n:
        continue
      starter = int('1'+'0'*(n-1))
      finisher = 10**n
      # r is number of repetitions
      for r in range(l // n, 1 + l // n):
        for v in range(starter, finisher):
          value = int(str(v)*r)
          if value >= range_start and value <= range_end:
            invalids.add(value)

  # Output
  return sum(invalids)

def main():
  """Solution for Advent of Code 2025, 2B.
     Input has not changed, but copied to b.in anyway."""

  start_time = time.perf_counter()

  # Initial conditions
  invalid_sum = 0

  # Read and process input file
  with open("b.in", 'r') as input_file:
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
