"""
This class stores information related to the match and has methods that allow the game to happen.
These methods involve card handling (shuffling, dealing and exchanging) and bet making.

@ Created by Gabriel Perão in May/2022
"""

# standard library imports
import random

# local application imports
import Player
import Card
import Display


class Game:

    all_values: list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    all_suits: list = ['♠', '♥', '♦', '♣']

    def __init__(self):
        self._is_on: bool = False
        self._all_cards: list = []
        self._available_cards: list = []
        self._bet: int = 0

    @property
    def is_on(self):
        return self._is_on

    @property
    def bet(self):
        return self._bet

    @staticmethod
    def get_card_choice_input(display: Display.Display) -> set:
        """
        Gets from the input the cards that the player wants to change.
        :param display: instance of Display.Display for the messages;
        :return: a set with the number of the cards that will be changed (from 1 to 5);
        """

        choices: set = set()
        print(display.cards_to_change_msg())

        input_is_valid: bool = False
        while not input_is_valid:
            try:
                choices.clear()
                for x in input(">>> ").split():
                    if int(x) < 1 or int(x) > 5:
                        raise ValueError
                    choices.add(int(x))
                input_is_valid = True
            except ValueError:
                print(display.invalid_card_msg())
        return choices

    def start(self) -> None:
        """
        Prepares the environment for a new game. Instantiates new cards and shuffles them.
        """
        for value in self.all_values:
            for suit in self.all_suits:
                self._all_cards.append(Card.Card(value=value, suit=suit))
        self.shuffle_cards()
        self._is_on = True

    def shuffle_cards(self) -> None:
        """
        Shuffles the list with all cards and updates the list with available cards.
        """
        random.shuffle(self._all_cards)
        self._available_cards = self._all_cards.copy()

    def make_new_bet(self, display: Display.Display, player: Player.Player) -> bool:
        """
        Gets from input a new bet and checks whether it's a valid bet.
        :param display: instance of Display.Display for the messages;
        :param player: instance of Player.Player;
        :return: flag indicating whether it was a valid bet or not;
        """

        print(display.bet_msg())

        input_is_valid: bool = False
        while not input_is_valid:
            try:
                bet = int(input(">>> "))
                if bet < 0:
                    raise ValueError
                if not player.new_bet(bet=bet):
                    print(display.insufficient_balance_msg())
                    raise ValueError
                self._bet = bet
                input_is_valid = True
            except ValueError:
                print(display.invalid_bet_msg())

        return self._bet != 0

    def deal_cards(self, player: Player.Player) -> None:
        """
        Picks 5 random cards from the game deck and deals them to the player.
        :param player: instance of Player.Player;
        """

        new_deck: list[Card.Card] = self._all_cards[:5]
        self._available_cards = self._all_cards[5:].copy()
        player.get_new_deck(new_deck)

    def deal_one_card(self, player: Player.Player, card_pos: int) -> None:
        """
        Picks 1 random card from the game deck and gives it to the player.
        :param player: instance of Player.Player;
        :param card_pos: number of the card that will be replaced in the player's hand (from 1 to 5);
        """
        new_card: Card.Card = random.choice(self._available_cards)
        self._available_cards.remove(new_card)
        player.get_new_card(new_card, card_pos)

    def end_game(self):
        self._is_on = False
