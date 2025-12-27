import time

def max_joltage(input_str: str) -> int:
  batteries = [int(v) for v in input_str]
  left_digit = max(batteries[:len(batteries)-1])
  left_location = batteries.index(left_digit)
  right_digit = max(batteries[left_location+1:])
  return int(str(left_digit)+str(right_digit))

def main():
  """Solution for Advent of Code 2025, XX."""
  # Start timing once we're in main(). Initialization of variables is included.
  start_time = time.perf_counter()

  # Show your work here.
  result = 0
  
  with open("a.in", 'r') as input_file:
    for input_line in input_file:
      result += max_joltage(input_line.strip())

  # End timing once we have the result.
  end_time = time.perf_counter()

  # Output result - do not include printing in time measurement.
  print(f"Result: {result}")
  calc_time = end_time - start_time
  print(f"Calculation time: {calc_time:.4f} seconds")

if __name__ == "__main__":
  main()
