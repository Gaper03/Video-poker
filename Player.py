"""
This class stores information related to the person who is playing the game, such as the balance and the
cards on the player's hand. It also has methods related to card and balance handling.

@ Created by Gabriel Perão in May/2022
"""

import Card


class Player:

    def __init__(self):
        self._balance: int = 200
        self._deck: list = []

    @property
    def balance(self):
        return self._balance

    @property
    def deck(self):
        return self._deck

    def get_new_deck(self, deck: list) -> None:
        """
        Receives a list of cards and sets it as the player's deck.
        :param deck: a list with 5 cards (Card.Card);
        """
        self._deck = deck.copy()

    def get_new_card(self, new_card: Card.Card, pos: int) -> None:
        """
        Switches one of the player's cards with another card.
        :param new_card: the new card (Card.Card);
        :param pos: the index in the player's deck for the card to be switched with the new card;
        """
        self._deck[pos-1] = new_card

    def new_bet(self, bet: int) -> bool:
        """
        Withholds bet money from the player's balance.
        :param bet: the amount of credits to be withheld;
        :return: a flag indicating whether the 'bet' parameter is a valid amount of credits;
        """

        if bet <= self._balance:
            self._balance -= bet
            return True
        return False

    def add_money(self, money: int) -> None:
        """
        Adds money to the player's balance.
        :param money: amount of credits to be added.
        """
        self._balance += money
