from urllib.parse import urlparse
from bs4 import BeautifulSoup
import dateutil
import requests
import card
import tqdm


class Set:
    def __init__(self, url: str) -> None:
        """
        Initialize the Set object.

        Args:
            - url (str): The URL of the set.

        Returns:
            - None
        """
        self.url = url

        response = requests.get(url)
        response.raise_for_status()
        self.soup = BeautifulSoup(response.content, "html.parser")

        self.setAll()

    def setAll(self) -> None:
        """
        Set all attributes of the Set class based on the URL.

        Args:
            - None

        Returns:
            - None
        """
        self.setName()
        self.setReleaseDate()
        self.setCardCount()
        self.setCardInfo()

    def setName(self) -> None:
        """
        Set the name of the set based on the URL.

        Args:
            - None

        Returns:
            - None
        """
        name = self.soup.find(class_="infobox-heading sm")

        if not name:
            raise ValueError(f"Set name not found on page: {self.url}")

        self.name = name.get_text(strip=True)

    def setReleaseDate(self) -> None:
        """
        Set the release date of the set based on the URL.

        Args:
            - None

        Returns:
            - None
        """
        infoLine = self.soup.find("div", class_="infobox-line")
        date = None

        # Extract text and split by the bullet (•)
        if infoLine:
            parts = [
                part.strip()
                for part in infoLine.get_text(strip=True, separator="•").split("•")
            ]
            date = dateutil.parser.parse(parts[0].strip())

        if not date:
            raise ValueError(f"Release date not found on page: {self.url}")
        self.releaseDate = date

    def setCardCount(self) -> None:
        """
        Set the card count of the set based on the URL.

        Args:
            - None

        Returns:
            - None
        """
        infoLine = self.soup.find("div", class_="infobox-line")
        cardCount = None

        # Extract text and split by the bullet (•)
        if infoLine:
            parts = [
                part.strip()
                for part in infoLine.get_text(strip=True, separator="•").split("•")
            ]
            # Remove the "cards" part and convert to integer
            if "cards" in parts[1].lower():
                parts[1] = parts[1].lower().replace("cards", "").strip()
            cardCount = int(parts[1].strip())

        if not cardCount:
            raise ValueError(f"Card count not found on page: {self.url}")
        self.cardCount = cardCount

    def setCardInfo(self) -> None:
        """
        Set the card information for the set.

        Args:
            - None

        Returns:
            - None
        """
        self.cards: list[card.Card] = []

        parsedUrl = urlparse(self.url)
        origin = f"{parsedUrl.scheme}://{parsedUrl.hostname}"

        cardsElement = self.soup.find("div", class_="card-search-grid")

        # for a in cardsElement.find_all("a", href=True):
        for a in tqdm.tqdm(
            cardsElement.find_all("a", href=True), desc=f"{self.name} cards"
        ):
            self.cards.append(card.Card(url=f"{origin}{a['href']}"))

    def getCardData(self) -> list:
        """
        Get the card information for the set.

        Args:
            - None

        Returns:
            - List of Card objects
        """
        return [card.getData() for card in self.cards]
