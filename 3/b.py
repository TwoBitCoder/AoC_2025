import time

def max_joltage(input_str: str, num_digits: int) -> int:
  batteries = [int(v) for v in input_str]
  result = ''
  for i in range(num_digits):
    next_digit = max(batteries[:len(batteries)-num_digits+len(result)+1])
    result += str(next_digit)
    next_location = batteries.index(next_digit)
    batteries = batteries[next_location+1:]
  return int(result)

def main():
  """Solution for Advent of Code 2025, 3B.
     Input has not changed, but copied to b.in anyway."""
  # Start timing once we're in main(). Initialization of variables is included.
  start_time = time.perf_counter()

  # Show your work here.
  result = 0
  
  with open("b.in", 'r') as input_file:
    for input_line in input_file:
      result += max_joltage(input_line.strip(), 12)

  # End timing once we have the result.
  end_time = time.perf_counter()

  # Output result - do not include printing in time measurement.
  print(f"Result: {result}")
  calc_time = end_time - start_time
  print(f"Calculation time: {calc_time:.4f} seconds")

if __name__ == "__main__":
  main()
