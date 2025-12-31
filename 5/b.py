import time

def combine_ranges(range_list: list) -> list:
  """Merge overlapping ranges. Input must be sorted.
     Returns the list of merged ranges, which will still be sorted."""
  result = [range_list[0]]
  for i in range(1, len(range_list)):
    new_range = range_list[i]
    last_range = result[-1]
    if new_range[0] <= last_range[1]:
      result[-1][1] = max(last_range[1], new_range[1])
    else:
      result.append(new_range)
  return result

def main():
  """Solution for Advent of Code 2025, 5B.
     Input has not changed, but copied to b.in anyway."""
  # Start timing once we're in main(). Initialization of variables is included.
  start_time = time.perf_counter()

  # Show your work here.

  # init
  result = 0
  ranges = []

  # parse input
  with open("b.in", 'r') as input_file:
    input_line = input_file.readline()
    while "\n" != input_line:
      ranges.append([int(x) for x in input_line.split('-')])
      input_line = input_file.readline()

    ranges.sort() # A little surprised this Just Works
    ranges = combine_ranges(ranges)

    for r in ranges:
      result += r[1]-r[0]+1

  # End timing once we have the result.
  end_time = time.perf_counter()

  # Output result - do not include printing in time measurement.
  print(f"Result: {result}")
  calc_time = end_time - start_time
  print(f"Calculation time: {calc_time:.4f} seconds")

if __name__ == "__main__":
  main()
