from mappings import Type
from bs4 import element


class AttackCost:

    @staticmethod
    def mapAttackCost(costElements: list[element.Tag]) -> list[str]:
        """
        Map attack cost elements to type names.

        Args:
            - costElements (list[element.Tag]): BeautifulSoup elements containing cost symbols

        Returns:
            - list[str]: List of type names for the attack cost
        """
        costList = []

        for cost in costElements:
            costSymbol = cost.text.strip()

            if len(costSymbol) > 1:
                for letter in costSymbol:
                    costType = Type.getType(letter)
                    costList.append(costType)
            else:
                costType = Type.getType(costSymbol)
                costList.append(costType)

        return costList if costList else ["No Cost"]
