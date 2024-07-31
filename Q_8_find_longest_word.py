# Write a python program to find the longest words.

def find_longest_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
    
    longest_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == longest_length]
    
    return longest_words

file_path = 'demo.txt'  # Replace with your file path
longest_words = find_longest_words(file_path)

print("The longest words are:")
for word in longest_words:
    print(word)

