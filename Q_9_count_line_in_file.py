# Write a Python program to count the number of lines in a text file.

def count_lines_in_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return len(lines)
    
file_path = 'demo.txt'  # Replace with your file path
line_count = count_lines_in_file(file_path)

print(f'The number of lines in the file is: {line_count}')
