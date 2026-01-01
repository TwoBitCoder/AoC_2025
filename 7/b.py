import time

def main():
  """Solution for Advent of Code 2025, 7B.
     Input has not changed, but copied to b.in anyway."""
  # Start timing once we're in main(). Initialization of variables is included.
  start_time = time.perf_counter()

  # Show your work here.

  # init
  result = 0

  # process input
  with open("b.in", 'r') as input_file:
    # Assume the start is in the first line.
    first_line = input_file.readline()
    beams = [0] * len(first_line)
    beams[first_line.find('S')] = 1
    # Assume no more starts.
    for input_line in input_file:
      next_beams = beams # Working with a copy may not be necessary, but is a simple safeguard against unexpected combinations.
      splitter = -1
      while True:
        splitter = input_line.find('^', splitter+1)
        if -1 == splitter:
          break
        next_beams[splitter-1] += beams[splitter]
        next_beams[splitter+1] += beams[splitter]
        next_beams[splitter] = 0
        #print(next_beams)
      beams = next_beams
  result = sum(beams)

  # End timing once we have the result.
  end_time = time.perf_counter()

  # Output result - do not include printing in time measurement.
  print(f"Result: {result}")
  calc_time = end_time - start_time
  print(f"Calculation time: {calc_time:.4f} seconds")

if __name__ == "__main__":
  main()
