import requests
from bs4 import BeautifulSoup

url = 'https://pikdonker.github.io/frosthaven-rule-book/'

def get_rule_book(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def get_section_content(current, next):
    content = ''
    while current and current != next:
        content += str(current)
        current = current.find_next_sibling()
    return content

def split_into_sections(soup):
    # Finding all h1 tags
    h1_tags = soup.find_all(['h1', 'h2', 'h3'])
    # Process each section and save to a separate text file
    for i in range(len(h1_tags)):
        # Get current and next h1 tag
        current_h1 = h1_tags[i]
        next_h1 = h1_tags[i+1] if i+1 < len(h1_tags) else None

        # Extract the content between the current and next h1 tags
        section_content = get_section_content(current_h1, next_h1)

        # Create a file name based on the h1 text
        file_name = f'section_{i+1}.txt'

        # Save the content to a file
        with open(f'data/{file_name}', 'w', encoding='utf-8') as file:
            file.write(section_content)

    # Provide feedback that process is complete
    "Sections extracted and saved into separate files."

soup = get_rule_book(url)
split_into_sections(soup)




