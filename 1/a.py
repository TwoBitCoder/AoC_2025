def main():
  """Solution for Advent of Code 2025, 1A."""

  # Initial conditions.
  current_value = 50
  zero_count = 0

  # Process input
  with open("a.in", 'r') as input_file:
    for input_line in input_file:
      rotate_distance = int(input_line[1:])
      match input_line[0]:
        case 'L':
          current_value -= rotate_distance
        case 'R':
          current_value += rotate_distance
      current_value %= 100
      if 0 == current_value:
        zero_count += 1

  # Show result
  print(zero_count)

if __name__ == "__main__":
  main()
