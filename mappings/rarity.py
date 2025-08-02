class Rarity:
    """
    Class for rarity mappings and utilities.
    """

    # Probability per pack type and rarity
    probabilitiesByRow = {
        "1-3 card": {
            "◊": 1,
            "◊◊": 0,
            "◊◊◊": 0,
            "◊◊◊◊": 0,
            "☆": 0,
            "☆☆": 0,
            "☆☆☆": 0,
            "♛": 0,
        },
        "4 card": {
            "◊": 0,
            "◊◊": 0.9,
            "◊◊◊": 0.05,
            "◊◊◊◊": 0.01666,
            "☆": 0.02572,
            "☆☆": 0.005,
            "☆☆☆": 0.00222,
            "♛": 0.0004,
        },
        "5 card": {
            "◊": "0.000%",
            "◊◊": "60.000%",
            "◊◊◊": "20.000%",
            "◊◊◊◊": "6.664%",
            "☆": "10.288%",
            "☆☆": "2.000%",
            "☆☆☆": "0.888%",
            "♛": "0.160%",
        },
    }

    # Crafting costs by rarity
    craftingCosts = {
        "◊": 35,
        "◊◊": 70,
        "◊◊◊": 150,
        "◊◊◊◊": 500,
        "☆": 400,
        "☆☆": 1250,
        "☆☆☆": 1500,
        "♛": 2500,
    }

    # Full art rarities
    fullArtRarities = ["☆", "☆☆", "☆☆☆", "Crown Rare"]

    @staticmethod
    def getProbabilitiesByRarity(rarity: str) -> dict:
        """
        Get probabilities for a specific rarity across all pack types.

        Args:
            - rarity (str): The rarity symbol

        Returns:
            - dict: Dictionary with pack types as keys and probabilities as values
        """
        probabilities = {}
        for row, rates in Rarity.probabilitiesByRow.items():
            if rarity in rates:
                probabilities[row] = rates[rarity]
        return probabilities

    @staticmethod
    def getCraftingCost(rarity: str) -> int:
        """
        Get crafting cost for a specific rarity.

        Args:
            - rarity (str): The rarity symbol

        Returns:
            - int: Crafting cost or None if unknown
        """
        return Rarity.craftingCosts.get(rarity, None)

    @staticmethod
    def isFullArt(rarity: str) -> bool:
        """
        Check if a rarity is considered full art.

        Args:
            - rarity (str): The rarity symbol

        Returns:
            - bool: True if it's a full art rarity
        """
        return rarity in Rarity.fullArtRarities
