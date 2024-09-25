import re

# Function to deduplicate and filter out links ending with #community
def deduplicate_and_filter_links(links):
    unique_links = set()
    for link in links:
        if not re.search(r'#community$', link):
            unique_links.add(link)
    return list(unique_links)

# Function to read links from a file and return a list of links
def read_links_from_file(file_path):
    with open(file_path, 'r') as file:
        links = file.readlines()
    # Strip newline characters and return a list of links
    return [link.strip() for link in links]

# Function to write links to a file
def write_links_to_file(file_path, links):
    with open(file_path, 'w') as file:
        for link in links:
            file.write(link + '\n')

# Function to modify URLs to https://arxiv.org/pdf/*.pdf and remove /papers
def modify_urls(links):
    modified_links = []
    for link in links:
        # Extract the path after the domain and remove /papers segment
        path = re.sub(r'https?://[^/]+(.*)', r'\1', link)
        path = re.sub(r'/papers', '', path)
        # Construct the new URL
        new_url = f"https://arxiv.org/pdf{path}.pdf"
        modified_links.append(new_url)
    return modified_links

# Path to the input file
input_file_path = 'web_links.txt'

# Read links from the input file
web_links = read_links_from_file(input_file_path)

# Process the links
filtered_links = deduplicate_and_filter_links(web_links)

# Modify the URLs
modified_links = modify_urls(filtered_links)

# Path to the output file
output_file_path = 'modified_web_links.txt'

# Write the modified links to the output file
write_links_to_file(output_file_path, modified_links)

# Print the result
print("Modified links have been written to", output_file_path)
