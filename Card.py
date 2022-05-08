"""
This class represents a card and stores its value and suit.

@ Created by Gabriel Perão in May/2022
"""


class Card:

    def __init__(self, value: str, suit: str):
        self._value = value
        self._suit = suit

    @property
    def value(self) -> str:
        return self._value

    @property
    def suit(self) -> str:
        return self._suit
