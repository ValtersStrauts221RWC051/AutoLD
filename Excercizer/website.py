import requests
from bs4 import BeautifulSoup

def SiteToCharList(site="https://greatist.com/fitness/50-bodyweight-exercises-you-can-do-anywhere#bodyweight-moves-for-beginners"):
    page = requests.get(site)

    # pārraksta mājaslapau uz html tekstu
    page = page.text

    # pārveido html tekstu skaidri saprotamā tekstā
    soup = BeautifulSoup(page, "html.parser")
    plaintext = soup.get_text()

    # Izņem tekstu kas traucē
    plaintext = plaintext.replace("Share on Pinterest", "")

    # pārveido no String uz char list, un atgriež
    return list(plaintext)
