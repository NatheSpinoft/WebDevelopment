import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

def scrape_ottawa_senators_players():
    url = 'https://www.tsn.ca/nhl/team/ottawa-senators/roster'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        players = soup.find_all('tr', {'class': 'PlayerRow'})
        if players:
            root = ET.Element("OttawaSenatorsRoster")

            for player in players:
                player_info = player.find_all('td')
                if len(player_info) >= 3:  # Ensure the row has the required columns
                    player_name = player_info[1].text.strip()
                    player_position = player_info[2].text.strip()

                    player_element = ET.SubElement(root, "Player")
                    player_name_elem = ET.SubElement(player_element, "Name")
                    player_name_elem.text = player_name
                    player_position_elem = ET.SubElement(player_element, "Position")
                    player_position_elem.text = player_position
                else:
                    print("Incomplete data for a player.")

            tree = ET.ElementTree(root)
            tree.write("OttawaSenatorsRoster.xml")
            print("Data written to OttawaSenatorsRoster.xml")
        else:
            print("No player information found.")
    else:
        print("Failed to fetch data.")

if __name__ == '__main__':
    scrape_ottawa_senators_players()
