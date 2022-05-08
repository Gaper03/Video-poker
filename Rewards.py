"""
This class analyzes the player's deck and calculates the reward corresponding to each poker hand.

@ Created by Gabriel Perão in May/2022
"""


class Rewards:

    @staticmethod
    def check_two_pairs(deck: list) -> bool:
        """
        Checks whether there are two pairs in the player's deck. A pair consists in two cards with the same value and
        different suits.
        :param deck: a list with 5 cards (Card.Card);
        :return: a flag related to the validity of this poker hand;
        """

        card_count_dict = dict()
        for card in deck:
            try:
                card_count_dict[card.value] += 1
            except KeyError:
                card_count_dict[card.value] = 1

        n_pairs = list(card_count_dict.values()).count(2)
        return n_pairs == 2

    @staticmethod
    def check_three_of_a_kind(deck: list) -> bool:
        """
        Checks whether there are three cards with the same value and different suits in the player's deck.
        :param deck: a list with 5 cards (Card.Card);
        :return: a flag related to the validity of this poker hand;
        """

        card_count_dict = dict()
        for card in deck:
            try:
                card_count_dict[card.value] += 1
            except KeyError:
                card_count_dict[card.value] = 1

        count_list = list(card_count_dict.values())
        return bool(3 in count_list)

    @staticmethod
    def check_straight(deck: list) -> bool:
        """
        Checks whether there is a sequence in the player's deck. In this case, the sequence can involve cards with
        different suits, but the value of these cards must form a sequence.
        :param deck: a list with 5 cards (Card.Card);
        :return: a flag related to the validity of this poker hand;
        """

        sequence_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

        # List with the value of each of the player's cards
        cards_value_list = [card.value for card in deck]

        ordered_values = sorted(cards_value_list, key=lambda x: sequence_order.index(x))
        first_card_index: int = sequence_order.index(ordered_values[0])
        sequence_exists: bool = (ordered_values == sequence_order[first_card_index:][:5])
        return sequence_exists

    @staticmethod
    def check_flush(deck: list) -> bool:
        """
        Checks whether all the cards in the player's deck have the same suit.
        :param deck: a list with 5 cards (Card.Card);
        :return: a flag related to the validity of this poker hand;
        """

        suit = deck[0].suit
        for card in deck[1:]:
            if card.suit != suit:
                return False
        return True

    @staticmethod
    def check_full_house(deck: list) -> bool:
        """
         Checks whether the cards in the player's deck form a full-house. A full-house occurs when two of the cards
         form a pair and the other cards form a three-of-a-kind.
        :param deck: a list with 5 cards (Card.Card);
        :return: a flag related to the validity of this poker hand;
        """

        card_count_dict = dict()
        for card in deck:
            try:
                card_count_dict[card.value] += 1
            except KeyError:
                card_count_dict[card.value] = 1

        count_list = list(card_count_dict.values())
        return bool(3 in count_list and 2 in count_list)

    @staticmethod
    def check_four_of_a_kind(deck: list) -> bool:
        """
        Checks whether there are four cards with the same value in the player's deck.
        :param deck: a list with 5 cards (Card.Card);
        :return: a flag related to the validity of this poker hand;
        """

        card_count_dict = dict()
        for card in deck:
            try:
                card_count_dict[card.value] += 1
            except KeyError:
                card_count_dict[card.value] = 1

        count_list = list(card_count_dict.values())
        return bool(4 in count_list)

    @classmethod
    def check_straight_flush(cls, deck: list) -> bool:
        """
        Checks whether the player's cards form a straight AND a flush.
        :param deck: a list with 5 cards (Card.Card);
        :return: a flag related to the validity of this poker hand;
        """
        return cls.check_straight(deck) and cls.check_flush(deck)

    @classmethod
    def check_royal_flush(cls, deck: list) -> bool:
        """
        Checks whether the player's cards form a royal straight flush: a sequence from '10' to 'A' with all cards of
        the same suit.
        :param deck: a list with 5 cards (Card.Card);
        :return: a flag related to the validity of this poker hand;
        """

        if not cls.check_straight_flush(deck):
            return False

        royal_flush_values = ['10', 'J', 'Q', 'K', 'A']
        for card in deck:
            if card.value not in royal_flush_values:
                return False
        return True

    @classmethod
    def get_reward(cls, deck: list) -> tuple:
        """
        Checks whether there is valid poker hand in the player's deck.
        :param deck: a list with 5 cards (Card.Card);
        :return: name of the poker hand and a multiplier for the bet;
        """
        if cls.check_royal_flush(deck):
            return "ROYAL FLUSH", 200

        if cls.check_straight_flush(deck):
            return "STRAIGHT FLUSH", 100

        if cls.check_four_of_a_kind(deck):
            return "FOUR OF A KIND", 50

        if cls.check_full_house(deck):
            return "FULL HOUSE", 20

        if cls.check_flush(deck):
            return "FLUSH", 10

        if cls.check_straight(deck):
            return "STRAIGHT", 5

        if cls.check_three_of_a_kind(deck):
            return "THREE OF A KIND", 2

        if cls.check_two_pairs(deck):
            return "TWO PAIRS", 1

        return "", 0  # no poker hand at all
