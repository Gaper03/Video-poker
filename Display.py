"""
This class is responsible for displaying information to the user by returning messages or printing them directly on the
screen (output).

@ Created by Gabriel Perão in May/2022
"""

import os


class Display:

    # Colors and effects for terminal
    FLASH_LBL = '\33[6m'
    RED_LBL = '\33[31m'
    RED2_LBL = '\33[91m'
    GREEN_LBL = '\33[92m'
    YELLOW_LBL = '\33[33m'
    YELLOW2_LBL = '\33[93m'
    GREEN2_LBL = '\33[32m'
    BLUE_LBL = '\33[34m'
    VIOLET_LBL = '\33[35m'
    BEIGE_LBL = '\33[36m'
    RESET_LBL = '\33[0m'
    REWARD_COLORS = {
        "": RESET_LBL,
        "TWO PAIRS": YELLOW2_LBL,
        "THREE OF A KIND": GREEN2_LBL,
        "STRAIGHT": RED2_LBL,
        "FLUSH": BEIGE_LBL,
        "FULL HOUSE": BLUE_LBL,
        "FOUR OF A KIND": VIOLET_LBL,
        "STRAIGHT FLUSH": RED_LBL,
        "ROYAL FLUSH": YELLOW_LBL
    }

    @classmethod
    def display_cards(cls, deck: list) -> None:
        """
        Draws the cards on the screen.
        :param deck: list with the 5 cards (Card.Card);
        """

        print("Suas cartas:\n\n")
        print(" +-----+ " * 5)
        print(" |     | " * 5)
        for card in deck:
            value: str = card.value
            suit: str = card.suit
            lbl = cls.RED_LBL if suit in '♥♦' else cls.RESET_LBL

            if value == "10":
                print(f" | {value}{lbl}{suit}{cls.RESET_LBL} | ", end='')
            else:
                print(f" |  {value}{lbl}{suit}{cls.RESET_LBL} | ", end='')
        print()
        print(" |     | " * 5)
        print(" +-----+ " * 5)
        [print(f"   ({x})   ", end='') for x in range(1, 6)]
        print("\n")

    @classmethod
    def display_welcome_msg(cls) -> None:
        print("=== VIDEO POKER ===\n\n\n\n")
        input(f"{cls.FLASH_LBL}Pressione \"ENTER\" para começar...{cls.RESET_LBL}")

    @staticmethod
    def balance_msg(balance: int) -> str:
        return f"Seu saldo: {balance} créditos"

    @staticmethod
    def cards_to_change_msg() -> str:
        return "Digite o número das cartas que deseja trocar, separados por espaço, " +\
               "ou aperte \"ENTER\" para não trocar."

    @classmethod
    def invalid_card_msg(cls) -> str:
        return f"{cls.RED_LBL}Número(s) inválido(s)!{cls.RESET_LBL}\n" +\
               f"Digite apenas números válidos (de 1 a 5), referentes às cartas."

    @staticmethod
    def bet_msg() -> str:
        return "Defina o valor de sua aposta (0 para terminar)."

    @staticmethod
    def invalid_bet_msg() -> str:
        return "Insira apenas valores inteiros e positivos que sejam menores ou iguais ao seu saldo!"

    @classmethod
    def insufficient_balance_msg(cls) -> str:
        return f"{cls.RED_LBL}Saldo insuficiente! Faça uma aposta menor.{cls.RESET_LBL}"

    @staticmethod
    def game_over_msg(balance: int) -> str:
        return f"Fim de jogo. Você encerrou a partida com um saldo de {balance} créditos."

    @classmethod
    def reward_message(cls, reward_name: str, multiplier: int, reward_value: int) -> str:
        lbl = cls.REWARD_COLORS[reward_name]
        if multiplier == 1:
            return f"Parabéns por marcar {lbl}{reward_name}{cls.RESET_LBL}!\nVocê recebeu de volta o valor apostado."
        if multiplier != 0:
            return f"Parabéns por marcar {lbl}{reward_name}{cls.RESET_LBL}!\nVocê recebeu {reward_value} créditos."
        return "Má sorte... você não marcou nada."

    @staticmethod
    def end_of_round_msg() -> str:
        return "\nA rodada terminou. Aperte \"ENTER\" para começar uma nova rodada."

    @staticmethod
    def clear_screen() -> None:
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def display_bet(bet: int) -> None:
        print(f"Valor apostado: {bet} créditos")

    @staticmethod
    def card_change_counter_msg(n: int):
        return f"Trocas realizadas: ({n}/2)"
