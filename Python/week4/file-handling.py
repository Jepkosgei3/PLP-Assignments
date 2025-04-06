def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            # Read the contents of the file
            content = input_file.read()
        
        # Modify the content (for example, converting text to uppercase)
        modified_content = content.upper()

        # Write the modified content to the output file
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(modified_content)

        print(f"File has been successfully modified and saved as '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError:
        print(f"Error: There was an issue reading or writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    # Ask the user for the input filename
    input_filename = "file.txt"
    
    # Ask the user for the output filename
    output_filename = "modified.txt"

    # Call the function to read, modify and save the file
    read_and_modify_file(input_filename, output_filename)

# Run the main function
if __name__ == "__main__":
    main()
