# Write a Python program to write a list to a file.

def write_list_to_file(file_path, lst):
    with open(file_path, 'w') as file:
        for item in lst:
            file.write(f"{item}\n")

file_path = 'demo.txt'  # Replace with your desired file path
my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']  # Replace with your list

write_list_to_file(file_path, my_list)
print(f"List has been written to {file_path}")
