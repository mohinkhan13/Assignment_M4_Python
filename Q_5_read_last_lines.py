# Write a Python program to read last n lines of a fil

def read_last_n_lines(file_path, n):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if n >= len(lines):
            return lines
        else:
            return lines[-n:]

file_path = 'Assignment\source file\python\M4\demo.txt' 
n = 5
last_lines = read_last_n_lines(file_path, n)

for line in last_lines:
    print(line, end='')

