import requests
from bs4 import BeautifulSoup
from docx import Document
import argparse

def main(urls):
    # Create a new Word document
    doc = Document()

    # Loop through each URL and scrape its links
    for url in urls:
        # Send a request to the URL and get its HTML content
        response = requests.get(url)
        html_content = response.text

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all the links in the HTML content
        links = soup.find_all('a')

        # Create a list to hold the links
        link_list = []

        # Loop through each link and add it to the list
        for link in links:
            href = link.get('href')
            if href is not None:
                if href.startswith("http"):
                    full_url = href
                else:
                    full_url = url + href
                link_list.append(full_url)

        # Print the links in a single paragraph separated by commas
        doc.add_paragraph(', '.join(link_list))

    # Save the document
    doc.save('links.docx')

if __name__ == '__main__':
    # Parse the command line arguments
    parser = argparse.ArgumentParser(description='Scrape links from a list of URLs.')
    parser.add_argument('urls', metavar='URL', type=str, nargs='+', help='a list of URLs to scrape')
    args = parser.parse_args()

    try:
        main(args.urls)
    except Exception as e:
        print(f"An error occurred: {e}")
