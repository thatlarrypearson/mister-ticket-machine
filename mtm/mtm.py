# mister-ticket-machine/mtm/mtm.py
"""
Simulator for the fictitious Mister Ticket Machine used by a fictitious theme park.

Requirements are found in *Ticket Machine Programming Project Document* found in github repository:
https://github.com/thatlarrypearson/mister-ticket-machine
"""
from time import sleep

AFTER_INPUT_DELAY = 2
THEME_PARK_NAME = "Mister Theme Park"
CURRENCY_VALUES = [1, 5, 10, 20]
TICKET_NAMES = ['Child', 'Adult', 'Family']
TICKET_NUMBERS = [ticket + 1 for ticket in range(len(TICKET_NAMES))]
TICKET_PRICES = [6, 10, 20]

def welcome_screen():
    """
    Welcome the customer to the ticket machine simulator
    """
    # center the welcome screen
    print(f"Welcome to {THEME_PARK_NAME} where everyone is welcome!")
    input("Hit return to start...")
    print("\n")

    return

def show_ticket_prices():
    """
    Show customer the available tickets and their prices.
    """
    print("To purchase a ticket, select one of the ticket types below:")

    for ticket in range(len(TICKET_NAMES)):
        # center ticket info on the screen
        print(f"For a ${TICKET_PRICES[ticket]} {TICKET_NAMES[ticket]} Ticket enter {TICKET_NUMBERS[ticket]}")

def get_ticket_selection()->int:
    """
    Get the ticket and return the ticket number index.
    """
    while True:
        try:
            ticket_number = int(input("--> "))
            sleep(AFTER_INPUT_DELAY)

            if ticket_number in TICKET_NUMBERS:
                # return the ticket number index
                return TICKET_NUMBERS.index(ticket_number)

            ticket_numbers = [str(ticket) for ticket in TICKET_NUMBERS]
            print(f"\nOops, you entered a number other than {', '.join(ticket_numbers)}.\n")

        except ValueError:
            print("\nOops, looks like you entered text instead of a number. Please enter a number.\n")
            show_ticket_prices()

def show_ticket_purchased(ticket_number):
    """
    display the purchased ticket
    """
    print(f"\nYou ordered a {TICKET_NAMES[ticket_number]} Ticket\n")

def show_currency_values():
    """
    Show the customer the currency denominations that can be accepted.
    """
    number_of_currency_values = len(CURRENCY_VALUES)

    print("To enter money into the machine, select a currency value below:")

    for currency_index in range(number_of_currency_values):
        print(f"${CURRENCY_VALUES[currency_index]} enter {currency_index + 1}")

    return

def get_payment(amount_due:int)->int:
    """
    get payment and return the amount paid.
    
    when the payment was greater than the amount due,
    the remaining balance will be negative and the customer
    is entitled to a refund in the amount of the overage.
    """
    print(f"Amount due is ${amount_due}")

    show_currency_values()

    while True:
        try:
            currency_input = int(input("--> "))
            sleep(AFTER_INPUT_DELAY)

            currency_inputs = [value + 1 for value in range(len(CURRENCY_VALUES))]

            if currency_input in currency_inputs:
                currency_index = currency_inputs.index(currency_input)
                amount_due = amount_due - CURRENCY_VALUES[currency_index]
                return CURRENCY_VALUES[currency_index]

            print(f"\nOops, you entered a number other than {', '.join(currency_inputs)}.\n")

        except ValueError:
            print("\nOops, looks like you entered text instead of a number. Please enter a number.\n")
            show_currency_values(amount_due)

def give_customer_ticket(ticket:int):
    """
    after customer has paid for ticket, give them the ticket
    """
    print(f"\nHere is your ticket: {TICKET_NAMES[ticket]} Ticket\n")

def give_refund(refund_due:int)->int:
    """
    Give a partial refund.
    Return the amount left to refund.
    """
    # sort the currency values where biggest is first, smallest last
    currency_values = sorted(CURRENCY_VALUES, reverse=True)

    for currency_value in  currency_values:
        if refund_due >= currency_value:
            print(f"You are refunded ${currency_value}")
            return refund_due - currency_value

def thank_customer():
    """
    Thank the customer for their patronage.
    """
    print("\nThank you for visiting us today.  Enjoy!")

def main():
    """
    This is the main module and this is what gets called when the program runs.
    """
    while True:
        welcome_screen()

        show_ticket_prices()

        ticket = get_ticket_selection()

        show_ticket_purchased(ticket)

        amount_due = TICKET_PRICES[ticket]

        total_paid = 0
        while amount_due > 0:
            # get payment
            amount_paid = get_payment(amount_due)
            total_paid += amount_paid
            amount_due = amount_due - amount_paid

        give_customer_ticket(ticket)

        if amount_due < 0:
            # negative amount_due means a refund is due
            print(f"Total Paid: ${total_paid}")
            refund_due = abs(amount_due)
            print(f"Refund Due: ${refund_due}")

            while refund_due > 0:
                # keep refunding until the refund value gets down to zero.
                refund_due = give_refund(refund_due)

        thank_customer()

if __name__ == "__main__":
    main()