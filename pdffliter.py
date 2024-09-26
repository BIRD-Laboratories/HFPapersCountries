import os
import PyPDF2
import argparse

def check_pdf_files(directory):
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            file_path = os.path.join(directory, filename)
            try:
                # Attempt to open the PDF file
                with open(file_path, 'rb') as file:
                    reader = PyPDF2.PdfReader(file)
                    # If the file opens successfully, print a success message
                    print(f"File {filename} opened successfully.")
            except Exception as e:
                # If the file fails to open, print an error message and delete the file
                print(f"Error opening file {filename}: {e}")
                os.remove(file_path)
                print(f"File {filename} has been deleted.")

if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Check and delete corrupted PDF files in a directory.")
    parser.add_argument('directory', type=str, help='The directory containing the PDF files')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the function with the provided directory
    check_pdf_files(args.directory)
