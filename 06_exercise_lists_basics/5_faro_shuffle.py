deck_of_cards = input().split()

count_of_shuffles = int(input())

for shuffle in range(count_of_shuffles):
    middle_of_the_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[0:middle_of_the_deck]
    right_part = deck_of_cards[middle_of_the_deck:]
    deck_after_shuffing = []
    for card_index in range(len(left_part)):
        deck_after_shuffing.append(left_part[card_index])
        deck_after_shuffing.append(right_part[card_index])
    deck_of_cards = deck_after_shuffing

print(deck_of_cards)