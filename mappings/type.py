class Type:
    decoder = {
        "G": "Grass",
        "R": "Fire",
        "W": "Water",
        "L": "Lightning",
        "P": "Psychic",
        "F": "Fighting",
        "D": "Darkness",
        "M": "Metal",
        "Y": "Fairy",
        "C": "Colorless",
        "0": "Colorless",
    }

    @staticmethod
    def getType(typeCode: str) -> str:
        """
        Get the type.

        Args:
            - None

        Returns:
            - str: The name of the type.
        """
        toret = Type.decoder.get(typeCode, None)

        if toret is None:
            raise ValueError(f"Unknown type code: {typeCode}")

        return toret

    @staticmethod
    def getTypeList() -> list[str]:
        """
        Get the list of all types.

        Args:
            - None

        Returns:
            - list[str]: The list of all type names.
        """
        return list(Type.decoder.values())
