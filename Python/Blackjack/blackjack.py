import random
# 11 = J, 12 = Q, 13 = K, 14 = A
card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
suits = ["clubs", "diamonds", "hearts", "spades"]
 
face_cards = {
    11: "J",
    12: "Q",
    13: "K",
    14: "A"
}
def generate_cards():
    cards = []
    for value in card_values:
        for suit in suits:
            if value in face_cards:
                _card = (face_cards[value], suit)
            else:
                _card = (value, suit)
            cards.append(_card)
    return cards
 
cards = generate_cards()

def deal_card(cards):
    i = random.randint(0, len(cards)-1)
    card = cards[i]
    cards.pop(i)
    return card, cards
 
def deal2(cards):
    card1, cards = deal_card(cards)
    card2, cards = deal_card(cards)
    you = [card1, card2]
    return you, cards
 
your_hand, cards = deal2(cards)
dealer_hand, cards = deal2(cards)

fc_vals = {
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": (1, 11)
}

def get_hand_val(hand):
    val = 0
    for card in hand:  
        if card[0] in fc_vals:
            if card[0] != 'A':
                val += fc_vals[card[0]]
            else:
                if val + fc_vals[card[0]][1] > 21:
                    val += fc_vals[card[0]][0]
                else:
                    val += fc_vals[card[0]][1]
        else:
            val += card[0]
    return val

def hit_me(hand, cards):
    hit, cards = deal_card(cards)
    hand.append(hit)
    new_hand_val = get_hand_val(hand)
    return hand, new_hand_val, cards

print(f"Your hand: {your_hand}")
your_hand_val = get_hand_val(your_hand)
print(your_hand_val)
if your_hand_val == 21:
    print("Blackjack!")
    exit()
print(f"Dealer hand: {dealer_hand[0]}")
dealer_hand_val = get_hand_val(dealer_hand)
if dealer_hand_val == 21:
    print("Dealer Blackjack!")
    exit()

hit_or_no_hit = input("Do you wish to hit?(y/n) ")
while hit_or_no_hit == "y":
    your_hand, your_hand_val, cards = hit_me(your_hand, cards)
    print(your_hand)
    print(your_hand_val)
    if your_hand_val == 21:
        print("You win!")
        exit()
    elif your_hand_val > 21:
        print("You busted :(")
        exit()
    hit_or_no_hit = input("Do you wish to hit?(y/n) ")

if your_hand_val < 21 and dealer_hand_val < 21:
    if your_hand_val > dealer_hand_val:
        print("You win!")
    elif dealer_hand_val > your_hand_val:
        print("Dealer wins ...")
    else:
        print("Tie!")