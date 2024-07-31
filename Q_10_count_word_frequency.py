# Write a Python program to count the frequency of words in a file.

def count_word_frequency(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower() 
    
    words = text.split()
    word_frequency = {}
    
    for word in words:
        word = word.strip('.,!?";:()[]{}') 
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    
    return word_frequency


file_path = 'demo.txt'  # Replace with your file path
word_frequency = count_word_frequency(file_path)

print("Word frequencies:")
for word, count in word_frequency.items():
    print(f'{word}: {count}')

