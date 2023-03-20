from accounts_model import AccountsDatabase, Account
from card_model import Card, CardsDatabase


def insert_card():
    validated = False
    inserted_card = None
    print("Choose card to insert:")
    print("  [1] toss card")
    print("  [2] Kb card")
    print("  [3] NH card")
    print("Please type the ID of card; ex) 1")
    print("=======================================")
    while not validated:
        temp = input("INSERT CARD: ")
        if temp not in cards:
            print("Enter valid card ID")
        else:
            inserted_card = cards[temp]
            validated = True

    return inserted_card


def validate_card(card):
    print("Enter PIN to verify; PIN should be 4 digits")
    print("=======================================")
    validate = False
    while not validate:
        temp = input("ENTER PIN: ")
        validate = cardsDatabase.check_pin(card, temp)
        print("ERROR: WRONG PIN")

    return validate


def select_account(inserted_card):
    accounts_list = user_01.get_accounts(inserted_card)
    validate_account_selection = False
    validate_action_selection = False
    validate_amount_selection = False
    selected_account = None
    selected_action = None
    selected_amount = 0

    print("Type in the NUMBER of account name from below: ")
    for i in range(0, len(accounts_list)):

        print("  > [" + str(i) + "] " + accounts_list[i].get_account_name())
    print("=======================================")

    while not validate_account_selection:
        temp = input("SELECT ACCOUNT: ")
        if temp.isdigit() and int(temp) < len(accounts_list):
            selected_account = accounts_list[int(temp)]
            validate_account_selection = True
        else:
            print("ERROR: ENTER VALID ACCOUNT CODE")

    # Show current balance
    print("Current balance in " + selected_account.get_account_name() + ": $" + str(selected_account.get_balance()))
    print("Type in the NUMBER of action from below: ")
    print(" > [0] Deposit")
    print(" > [1] Withdraw")
    print("=======================================")
    while not validate_action_selection:
        action = input("ACTION: ")
        if action == "0":
            selected_action = "Deposit"
            validate_action_selection = True
        elif action == "1":
            selected_action = "Withdraw"
            validate_action_selection = True
        else:
            print("ERROR: ENTER VALID ACTION CODE")

    if selected_action == "Deposit":
        print("How much do you want to DEPOSIT?")
        while not validate_amount_selection:
            amount = input("AMOUNT: ")
            if amount.isnumeric():
                selected_amount = int(amount)
                validate_amount_selection = True
            else:
                print("ERROR: MUST ENTER INTEGER")
        selected_account.deposit(selected_amount)
    elif selected_action == "Withdraw":
        print("How much do you want to WITHDRAW?")
        while not validate_amount_selection:
            amount = input("AMOUNT: ")
            if amount.isnumeric():
                selected_amount = int(amount)
                validate_amount_selection = True
            else:
                print("ERROR: MUST ENTER INTEGER")
        selected_account.withdraw(selected_amount)

    print("Current balance after " + selected_action + " for " + selected_account.get_account_name() + " account: ")
    print("BALANCE: $" + str(selected_account.get_balance()))







# TEST VALUES

# Cards that user can insert
tossCard = Card(card_number="4572-1237-6342-7343", user_id="user01", card_name="toss01", exp_date='2024-05')
kbCard = Card(card_number="4433-2134-2434-8967", user_id="user01", card_name="kb01", exp_date='2030-08')
nhCard = Card(card_number="9872-3248-8903-1233", user_id="user02", card_name="nh01", exp_date='2028-12')

# Add the cards to our cards database
cardsDatabase = CardsDatabase()
cardsDatabase.add_card(card=tossCard, pin=3244)
cardsDatabase.add_card(card=kbCard, pin=2849)
cardsDatabase.add_card(card=nhCard, pin=1234)

# Create account database that will hold different accounts
user_01 = AccountsDatabase()

# Create accounts for each cards
toss_savings_account = Account(account_name= "savings_toss", balance=5400)
toss_spending_account = Account(account_name= "spending_toss", balance=2000)
kb_savings_account = Account(account_name= "savings_kb", balance=8200)
kb_spending_account = Account(account_name= "spending_kb", balance=1500)
nh_savings_account = Account(account_name= "savings_nh", balance=4600)
nh_spending_account = Account(account_name= "spending_nh", balance=300)

# Add accounts to our user's accounts database
user_01.add_account(card=tossCard, account=toss_savings_account)
user_01.add_account(card=tossCard, account=toss_spending_account)
user_01.add_account(card=kbCard, account=kb_savings_account)
user_01.add_account(card=kbCard, account=kb_spending_account)
user_01.add_account(card=nhCard, account=nh_savings_account)
user_01.add_account(card=nhCard, account=nh_spending_account)

# Input codes for our cards
cards = {"1": tossCard, "2": kbCard, "3": nhCard}


# ACTIONS

insertedCard = insert_card()
if validate_card(insertedCard):
    select_account(insertedCard)
