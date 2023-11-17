import requests
import re

def fetch_kilauea_update():
    url = "https://www.usgs.gov/programs/VHP/volcano-updates#elevated"
    
    # fetch html content
    response = requests.get(url)
    if response.status_code != 200:
        return "Error fetching data"

    # regex to find the latest Kilauea update
    html_text = response.text
    kilauea_match = re.search(r'<b>Kilauea</b>(.*?)For more information', html_text, re.DOTALL | re.IGNORECASE)
    
    if not kilauea_match:
        return "Kīlauea status not found"

    update_text = kilauea_match.group(1).strip()
    
    return update_text

# print update
print(fetch_kilauea_update())
