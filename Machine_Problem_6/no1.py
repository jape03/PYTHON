def open_file(file_name):
    try:
        with open(file_name, 'r') as file:
            print(f"Successfully opened {file_name}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except IOError as e:
        print(f"An IOError occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

print("File Exists")
open_file("exist.txt")

print("\nFile Does Not Exist")
open_file("notexist.txt")
