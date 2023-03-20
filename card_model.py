class Card:
    def __init__(self, card_number, user_id, card_name, exp_date):
        self._cardNumber = card_number
        self._cardName = card_name
        self._userId = user_id
        self._expDate = exp_date

    def get_card_name(self):
        return  self._cardName

    def get_user_id(self):
        return self._userId

    def get_card_num(self):
        return self._cardNumber

    def get_exp_date(self):
        return self._expDate


class CardsDatabase:

    def __init__(self):
        # [key]: Card object
        # [value]: PIN value in integer
        self._allCards = {}

    def get_card_list(self):
        return list(self._allCards.keys())

    def add_card(self, card, pin):
        self._allCards[card] = pin

    # returns true if PIN matches
    def check_pin(self, card, pin):
        if self._allCards[card] == int(pin):
            return True
        else:
            return False


