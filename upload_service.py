import os
import time
import argparse
from huggingface_hub import HfApi

def upload_files_to_huggingface(folder_path, repo_id, hf_token):
    # Initialize the Hugging Face API client
    api = HfApi()
    
    # Get the list of files already uploaded
    uploaded_files = set(api.list_repo_files(repo_id, token=hf_token))
    
    # Monitor the folder for new files
    while True:
        # List all files in the folder
        files_in_folder = set(os.listdir(folder_path))
        
        # Find new files that haven't been uploaded yet
        new_files = files_in_folder - uploaded_files
        
        for file_name in new_files:
            file_path = os.path.join(folder_path, file_name)
            print(f"Uploading {file_name} to Hugging Face...")
            
            # Upload the file to the repository
            api.upload_file(
                path_or_fileobj=file_path,
                path_in_repo=file_name,
                repo_id=repo_id,
                token=hf_token
            )
            
            print(f"Uploaded {file_name} successfully.")
        
        # Update the list of uploaded files
        uploaded_files.update(new_files)
        
        # Wait for a few seconds before checking again
        time.sleep(5)

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Upload files from a folder to Hugging Face repository.")
    parser.add_argument("folder_path", type=str, help="Path to the folder containing the files to upload.")
    parser.add_argument("repo_id", type=str, help="Hugging Face repository ID (e.g., 'username/repo_name').")
    parser.add_argument("hf_token", type=str, help="Hugging Face token for authentication.")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Call the function with the parsed arguments
    upload_files_to_huggingface(args.folder_path, args.repo_id, args.hf_token)
