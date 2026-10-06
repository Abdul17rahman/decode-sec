import requests

from bs4 import BeautifulSoup


def decode_sec(url):
    response = requests.get(url)

    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table')

    rows = table.find_all('tr')

    data = {}

    for row in table.find_all("tr")[1:]:
        cols = [cell.get_text(strip=True)
                for cell in row.find_all(["td", "th"])]

        if len(cols) >= 3:
            x = int(cols[0])
            character = cols[1]
            y = int(cols[2])

            data[(x, y)] = character

    max_x = max(x for x, y in data)
    max_y = max(y for x, y in data)

    for y in range(max_y, -1, -1):
        text = ""

        for x in range(max_x + 1):
            text += data.get((x, y), " ")

        print(text.rstrip())


if __name__ == "__main__":
    url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
    decode_sec(url)
