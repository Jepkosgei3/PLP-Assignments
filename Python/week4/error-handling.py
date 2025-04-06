def open_file():
    # Ask the user for a filename
    filename = input("Please enter the filename: ")

    try:
        # Try to open the file
        with open(filename, 'r', encoding='utf-8') as file:
            # If successful, read and print the file content
            content = file.read()
            print("File content:")
            print(content)
    
    except FileNotFoundError:
        # Handle the case where the file doesn't exist
        print(f"Error: The file '{filename}' does not exist.")
    
    except PermissionError:
        # Handle the case where the file can't be read due to permission issues
        print(f"Error: You do not have permission to read the file '{filename}'.")
    
    except Exception as e:
        # Handle any other unforeseen errors
        print(f"An unexpected error occurred: {e}")

# Call the function to test error handling
open_file()
