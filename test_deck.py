from deck import Deck, Card



def test_card():
    # Test creating a card to see if the card is correctly created
    check = Card(5, 'Hearts')
    assert check.rank == 5
    assert check.suite == 'Hearts'

    print('Passed card test')
    pass

def test_card_operators():
    # Test comparing card rank to see if the operators are functioning correctly
    card1 = Card(8, 'Diamonds')
    card2 = Card(8, 'Hearts')
    card3 = Card(3, 'Clubs')
    assert card1 == card2
    assert card3 < card1
    assert card1 != card3
    assert card2 > card3

    print('Passed card operators test')
    
def test_deck_length():
    
    # Test which create card deck to see if the right amount of cards are created
    check = Deck()
    assert len(check) == 55

    print('Passed deck length test')


    
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
    
def test_deck_take():
    # Test taking cards from the top of the card deck to see if it is taking the correct card
    check = Deck()
    assert check.take().rank == 0
    check.sort()
    assert check.take().rank == 13
    assert len(check) == 53

    print('Passed deck take test')
    
def test_deck_put():
    # Test putting cards on top of the card deck to see if it is putting in the right cards
    check = Deck()
    card1 = Card(8, 'Diamonds')
    card2 = Card(8, 'Hearts')
    card3 = Card(3, 'Clubs')
    check.put(card1)
    check.put(card2)
    check.put(card3)
    assert check.take().rank == 3
    assert check.take().rank == 8
    assert check.take().rank == 8
    assert len(check) == 55

    print('Passed deck put test')

def run_deck_test():
    test_deck_length()
    test_sort()
    test_deck_take()
    test_deck_put()

    print('Deck test passed\n')

def run_card_test():
    test_card()
    test_card_operators()

    print('Card test passed\n')

def run_tests():

    run_card_test()
    run_deck_test()

if __name__ == '__main__':

    run_tests()

    
