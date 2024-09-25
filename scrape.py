import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def fetch_links(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve the page: {response.status_code}")
        return []
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all the links on the page
    links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        # Check if the link matches the desired format
        if href.startswith('/papers/2') and href.count('/') == 2:
            full_url = f"https://huggingface.co{href}"
            links.append(full_url)
    
    return links

def save_links_to_file(links, filename="huggingface_papers_2024.txt"):
    with open(filename, 'a') as file:
        for link in links:
            file.write(link + '\n')
    print(f"Links saved to {filename}")

def main():
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    current_date = start_date

    while current_date <= end_date:
        url = f"https://huggingface.co/papers?date={current_date.strftime('%Y-%m-%d')}"
        print(f"Fetching links from: {url}")
        
        # Fetch the links
        links = fetch_links(url)
        
        # Save the links to a file
        save_links_to_file(links)
        
        # Increment the date by one day
        current_date += timedelta(days=1)

if __name__ == "__main__":
    main()
