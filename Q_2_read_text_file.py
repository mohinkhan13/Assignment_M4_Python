# Write a Python program to read an entire text file.

def read_text_file(file_path):
    
     with open(file_path, 'r') as file:
        content = file.read()
     return content

file_path = 'demo_text.txt'

file_data = read_text_file(file_path)

print(file_data)