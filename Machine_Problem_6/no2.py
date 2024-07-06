def read_text_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Content of '{file_name}':\n")
            print(content)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except IOError as e:
        print(f"An IOError occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

file_name = 'helloworld.txt'
print("Reading the text file:")
read_text_file(file_name)


