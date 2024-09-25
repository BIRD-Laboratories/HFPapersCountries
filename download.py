import os
import requests

# Function to download a PDF from a given URL and save it to a specified folder
def download_pdf(url, save_folder):
    # Extract the filename from the URL
    filename = os.path.join(save_folder, os.path.basename(url))
    
    # Ensure the save folder exists
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Save the content to a file
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download {url}")

# Function to read links from a file and return a list of links
def read_links_from_file(file_path):
    with open(file_path, 'r') as file:
        links = file.readlines()
    # Strip newline characters and return a list of links
    return [link.strip() for link in links]

# Path to the input file containing the modified URLs
input_file_path = 'modified_web_links.txt'

# Folder to save the downloaded PDFs
save_folder = 'downloaded_pdfs'

# Read links from the input file
pdf_links = read_links_from_file(input_file_path)

# Download each PDF
for link in pdf_links:
    download_pdf(link, save_folder)
