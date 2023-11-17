# poc for getting eruption alerts for kilauea
import requests
from bs4 import BeautifulSoup, NavigableString

def fetch_kilauea_update():
    url = "https://www.usgs.gov/programs/VHP/volcano-updates#elevated"
    
    # fetch html content
    response = requests.get(url)
    if response.status_code != 200:
        return "Error fetching data"

    # parse html content
    soup = BeautifulSoup(response.text, 'html.parser')

    # find the section on kilaeua
    kilauea_tag = soup.find('b', string='Kilauea')
    if not kilauea_tag:
        return "Kīlauea status not found"

    # extract the summary up to the part with 'For more information'
    summary = []
    for sibling in kilauea_tag.next_siblings:
        if sibling.name == 'br' and "For more information" in str(sibling):
            break
        if isinstance(sibling, NavigableString):
            summary.append(sibling.strip())
        elif sibling.name == 'b':
            # can't bold on the device, make the bold text uppercase
            bold_text = sibling.get_text(strip=True).upper()
            summary.append(bold_text)

    update_text = ' '.join(summary)

    return update_text

# print update]
print(fetch_kilauea_update())
