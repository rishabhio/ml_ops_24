import requests
from bs4 import BeautifulSoup

def extract_company_info(url):
    # Send a GET request to the Wikipedia page
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Find the infobox element
        infobox = soup.find("table", class_="infobox")
        
        # Extract data from the infobox
        if infobox:
            company_info = {}
            rows = infobox.find_all("tr")
            for row in rows:
                # Extract key-value pairs
                cells = row.find_all(["th", "td"])
                if len(cells) == 2:
                    key = cells[0].get_text(strip=True)
                    value = cells[1].get_text(strip=True)
                    company_info[key] = value
            
            return company_info
        else:
            print("Infobox not found on the page")
    else:
        print("Failed to retrieve the Wikipedia page")

# URL of the Wikipedia page of the company
wiki_url = "https://en.wikipedia.org/wiki/Tesla,_Inc."

# Call the function to extract company info
company_info = extract_company_info(wiki_url)

# Print the extracted company info
if company_info:
    for key, value in company_info.items():
        print(f"{key}: {value}")
else:
    print("No company info extracted")
