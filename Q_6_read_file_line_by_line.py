# Write a Python program to read a file line by line and store it into a list

def read_file_to_list(file_path):
    lines_list = []
    with open(file_path, 'r') as file:
        for line in file:
            lines_list.append(line.strip())
    return lines_list

file_path = 'demo.txt'  # Replace with your file path
lines = read_file_to_list(file_path)

for line in lines:
    print(line)


