#   Write a Python program to read first n lines of a file.

def read_first_line(file_path):
  try:
    with open(file_path, 'r') as file:
      return file.readline().strip()
  except FileNotFoundError:
    print(f"File '{file_path}' not found.")
    return None

file_path = "Assignment\source file\python\M4\demo.txt"  # Replace with the actual file path
first_line = read_first_line(file_path)
print(first_line)

