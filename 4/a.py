import time

def surrounding_rolls(grid: list, i: int, j: int) -> int:
  above = ""
  left = ""
  right = ""
  below = ""
  if i > 0:
    above = grid[i-1][max(0,j-1):j+2]
  if j > 0:
    left = grid[i][j-1]
  if j + 1 < len(grid[i]):
    right = grid[i][j+1]
  if i + 1 < len(grid):
    below = grid[i+1][max(0,j-1):j+2]
  return (above+left+right+below).count('@')

def main():
  """Solution for Advent of Code 2025, 4A."""
  # Start timing once we're in main(). Initialization of variables is included.
  start_time = time.perf_counter()

  # Show your work here.
  # Initialize
  result = 0
  
  # Read input
  with open("a.in", 'r') as input_file:
    grid = input_file.readlines()

  # Process grid
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if '@' == grid[i][j]:
        if surrounding_rolls(grid, i, j) < 4:
          result += 1

  # End timing once we have the result.
  end_time = time.perf_counter()

  # Output result - do not include printing in time measurement.
  print(f"Result: {result}")
  calc_time = end_time - start_time
  print(f"Calculation time: {calc_time:.4f} seconds")

if __name__ == "__main__":
  main()
