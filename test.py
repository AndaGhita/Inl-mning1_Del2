from deck import Deck, Card



def test_card():
    # Test creating a card to see if the card is correctly created
    check = Card(5, 'Hearts')
    assert check.rank == 5
    assert check.suite == 'Hearts'

    print('Passed card test')
    pass


def test_deck():
    # Test creating card deck to see if the right amount of cards are created
    # and if len function returns the right amount of cards
    test_deck = Deck()
    assert len(test_deck) == 55
    
    #check if the deck has the correct number of cards
    assert len(test_deck.cards) == 55
    
    #remove a card from the deck and check if the len() function returns the correct number of cards
    test_deck.cards.pop()
    assert len(test_deck) == 54
    
    #add a card to the deck and check if the len() function returns the correct number of cards
    test_deck.cards.append(Card(rank = 13 , suite = 'Spades'))
    assert len(test_deck) == 55
    

    print('Passed deck creation test')
    
def test_sort():
    # Test sorting the card deck to see if the deck is sorted successfully
    test_deck = Deck()
    test_deck.shuffle()
    
    test_deck.sort()
    previous_card = None
    for card in test_deck.cards:
      if previous_card is not None:
        assert previous_card.rank <= card.rank
        if previous_card.rank == card.rank:
          assert previous_card.suite <= card.suite
      previous_card = card
   

    print('Passed deck sorting test')

    
