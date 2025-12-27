def main():
  """Solution for Advent of Code 2025, 1B.
     Input has not changed, but copied to b.in anyway."""

  # Initial conditions.
  current_value = 50
  zero_count = 0

  # Process input
  with open("b.in", 'r') as input_file:
    for input_line in input_file:
      rotate_distance = int(input_line[1:])
      if 0 == rotate_distance:
        continue
      match input_line[0]:
        case 'L':
          # current_value will always be >= 0 before subtracting, but == 0 will cause a miscount.
          if 0 == current_value:
            zero_count -= 1
          current_value -= rotate_distance
          # The // operator returns floor, so -1 // 100 == -1 counts a single crossing.
          # We need == 0 to count as +1, so subtract 1 first.
          zero_count -= (current_value - 1) // 100
        case 'R':
          current_value += rotate_distance
          zero_count += current_value // 100
      current_value %= 100

  # Show result
  print(zero_count)

if __name__ == "__main__":
  main()
