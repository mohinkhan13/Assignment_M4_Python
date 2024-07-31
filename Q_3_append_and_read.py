# Write a Python program to append text to a file and display the text

def append_and_display(file_path, text_to_append):
  try:
    with open(file_path, 'a') as file:
      file.write(text_to_append + '\n')

    with open(file_path, 'r') as file:
      content = file.read()
      print(content)

  except FileNotFoundError:
    print(f"File '{file_path}' not found.")

  file_path = "Assignment\source file\python\M4\demo.txt"
  text_to_append = "This text will be appended."

  append_and_display(file_path, text_to_append)
