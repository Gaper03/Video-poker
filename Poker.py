"""
Main file; runs the game.

@ Created by Gabriel Perão in May/2022
"""

import Display
import Game
import Player
import Rewards


def main():
    game = Game.Game()
    display = Display.Display()
    player = Player.Player()
    rewards = Rewards.Rewards()

    game.start()
    display.clear_screen()
    display.display_welcome_msg()

    while game.is_on:
        display.clear_screen()
        game.shuffle_cards()
        print(display.balance_msg(balance=player.balance))

        # This method returns False if the bet was 0, meaning that the player wants to exit the game
        if not game.make_new_bet(display=display, player=player):
            game.end_game()
            print(display.game_over_msg(player.balance))
            break

        game.deal_cards(player=player)
        display.clear_screen()
        display.display_bet(game.bet)
        display.display_cards(deck=player.deck)
        print(display.card_change_counter_msg(0))

        # First change of cards
        cards_to_change: set = game.get_card_choice_input(display=display)
        for card_n in cards_to_change:
            game.deal_one_card(player=player, card_pos=card_n)
        display.clear_screen()
        display.display_bet(game.bet)
        display.display_cards(deck=player.deck)
        print(display.card_change_counter_msg(0 if len(cards_to_change) == 0 else 1))

        # Second change of cards
        if len(cards_to_change) > 0:
            cards_to_change = game.get_card_choice_input(display=display)
            for card_n in cards_to_change:
                game.deal_one_card(player=player, card_pos=card_n)
            display.clear_screen()
            display.display_bet(game.bet)
            display.display_cards(deck=player.deck)
            print(display.card_change_counter_msg(1 if len(cards_to_change) == 0 else 2))

        reward_name, multiplier = rewards.get_reward(deck=player.deck)
        reward_money = game.bet * multiplier
        player.add_money(money=reward_money)
        print(display.reward_message(reward_name=reward_name, multiplier=multiplier, reward_value=reward_money))
        print(display.balance_msg(balance=player.balance))

        print(display.end_of_round_msg())
        input()


if __name__ == "__main__":
    main()
