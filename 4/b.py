import time

def surrounding_rolls(grid: list, i: int, j: int) -> int:
  above = ""
  left = ""
  right = ""
  below = ""
  if i > 0:
    above = ''.join(grid[i-1][max(0,j-1):j+2])
  if j > 0:
    left = grid[i][j-1]
  if j + 1 < len(grid[i]):
    right = grid[i][j+1]
  if i + 1 < len(grid):
    below = ''.join(grid[i+1][max(0,j-1):j+2])
  return (above+left+right+below).count('@')

def remove_rolls(grid: list) -> int:
  """Makes a single pass of the grid.
     Removes rolls that are accessible.
     Returns the number of rolls removed."""
  result = 0
  # Process grid
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if '@' == grid[i][j]:
        if surrounding_rolls(grid, i, j) < 4:
          grid[i][j] = '.'
          result += 1
  return result

def main():
  """Solution for Advent of Code 2025, 4B.
     Input has not changed, but copied to b.in anyway."""
  # Start timing once we're in main(). Initialization of variables is included.
  start_time = time.perf_counter()

  # Show your work here.
  # Initialize
  result = 0
  last_result = -1
  grid = []

  # Read input - make it mutable
  with open("a.in", 'r') as input_file:
    for input_line in input_file:
      grid.append(list(input_line))

  # Iterate
  while last_result != result:
    last_result = result
    result += remove_rolls(grid)

  # End timing once we have the result.
  end_time = time.perf_counter()

  # Output result - do not include printing in time measurement.
  print(f"Result: {result}")
  calc_time = end_time - start_time
  print(f"Calculation time: {calc_time:.4f} seconds")

if __name__ == "__main__":
  main()
