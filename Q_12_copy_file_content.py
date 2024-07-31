# Write a Python program to copy the contents of a file to another file

def copy_file_contents(source_file_path, destination_file_path):
    with open(source_file_path, 'r') as source_file:
        contents = source_file.read()
        
    with open(destination_file_path, 'w') as destination_file:
        destination_file.write(contents)

source_file_path = 'demo.txt' 
destination_file_path = 'destination.txt'  

copy_file_contents(source_file_path, destination_file_path)
print(f"Contents have been copied from {source_file_path} to {destination_file_path}")
