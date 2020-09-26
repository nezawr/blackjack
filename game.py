import os
import random


deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4


def deal(cards):
    hand = []
    for i in range(2):
        random.shuffle(cards)
        card = cards.pop()
        if card == 11:
            card = 'J'
        if card == 12:
            card = 'Q'
        if card == 13:
            card = 'K'
        if card == 14:
            card = 'A'
        hand.append(card)
    return hand


def total(hand):
    hand_sum = 0
    for card in hand:
        if card == 'J':
            hand_sum += 10
        elif card == 'Q':
            hand_sum += 10
        elif card == 'K':
            hand_sum += 10
        elif card == 'A':
            if hand_sum >= 11:
                hand_sum += 1
            else:
                hand_sum += 11
        else:

            hand_sum += card

    return hand_sum


def hit(hand):
    random.shuffle(deck)
    card = deck.pop()
    if card == 11:
        card = 'J'
    if card == 12:
        card = 'Q'
    if card == 13:
        card = 'K'
    if card == 14:
        card = 'A'
    hand.append(card)


def print_results(p_hand, d_hand):

    print("Dealer's card are " + str(d_hand) + " for a total sum of " + str(total(d_hand)))
    print("Your cards are " + str(p_hand) + " for a total sum of " + str(total(p_hand)))


def compare_results(p_hand, d_hand):
    p_hand_total = total(p_hand)
    d_hand_total = total(d_hand)
    if p_hand_total == 21 and d_hand_total != 21:
        print_results(p_hand, d_hand)
        print('Congratulations, you got a blackjack!\n')
    elif p_hand_total == 21 and d_hand_total == 21:
        print_results(p_hand, d_hand)
        print("It's a draw\n")
    elif d_hand_total == 21:
        print_results(p_hand, d_hand)
        print("You lose, dealer's got a blackjack\n")
    elif p_hand_total > 21:
        print_results(p_hand, d_hand)
        print("You busted. You lose")
    elif d_hand_total > 21:
        print_results(p_hand, d_hand)
        print("The dealer busted, You win.\n")
    elif p_hand_total < d_hand_total:
        print_results(p_hand, d_hand)
        print("You lose.\n")
    elif d_hand_total < p_hand_total:
        print_results(p_hand, d_hand)
        print("You win.\n")


def play_again():
    again = input("Do you want to play again? (Y/N) : ").lower()
    if again == "y":
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
        game()
    else:
        print("Bye!")
        exit()


def blackjack(dealer_hand, player_hand):
    if total(player_hand) == 21 and total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("It's a draw!\n")
        play_again()
    elif total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Congratulations, you win. You got a blackjack.\n")
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Sorry, you lose. The dealer got a blackjack.\n")
        play_again()


def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')


def game():

    choice = 0
    print('Welcome to BLACKJACK!\n')
    player_cards = deal(deck)
    dealer_cards = deal(deck)
    while choice != 'q':
        print('The dealer is showing a ' + str(dealer_cards[0]))
        print('Your cards are ' + str(player_cards) + ' for a total sum of ' + str(total(player_cards)))
        blackjack(dealer_cards, player_cards)
        choice = input('Do you want to [H]it, [S]tay or [Q]uit?').lower()
        if choice == 'h':
            hit(player_cards)
            if total(player_cards) == 21:
                print("Your cards are " + str(player_cards) + " for a total sum of " + str(total(player_cards)))
                print('Blackjack! You win.\n')
                play_again()
            elif total(player_cards) > 21:
                print("Your cards are " + str(player_cards) + " for a total sum of " + str(total(player_cards)))
                print("You busted. You lose.\n")
                play_again()
            elif total(player_cards) < 21:
                print("Your cards are " + str(player_cards) + " for a total sum of " + str(total(player_cards)))
                choice = input('Do you want to [H]it, [S]tay or [Q]uit?').lower()
        elif choice == 's':
            while total(dealer_cards) < 17:
                hit(dealer_cards)
            compare_results(player_cards, dealer_cards)
            play_again()
        elif choice == 'q':
            print('Goodbye!')
            quit()
        else:
            choice = input('Invalid input, Do you want to [H]it, [S]tay or [Q]uit?').lower()




if __name__ == "__main__":
   game()