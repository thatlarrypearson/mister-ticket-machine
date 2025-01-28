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
    # print the welcome screen

    # get <CR> input to start ticket purchase process
 
def show_ticket_prices():
    """
    Show customer the available tickets and their prices.
    """
    # tell customer "To purchase a ticket, select one of the ticket types below:" 

    # for each ticket print out the ticket price, ticket name and the ticket number
    # ticket numbers go 1, 2, 3
    # ticket indexes go 0, 1, 2

def get_ticket_selection()->int:
    """
    Get the ticket and return the ticket number index.
    """
    # get input
    # put a small delay in after input
    # catch exceptions
    # test for out of bounds ticket numbers
    # return the ticket index, not the ticket number

def show_ticket_purchased(ticket_number):
    """
    display the purchased ticket
    """
    # tell the customer which ticket they purchased

def show_currency_values():
    """
    Show the customer the currency denominations that can be accepted.
    """
    # tell the customer "To enter money into the machine, select a currency value below:"

    # for each currency value print out the currency value and the currency number
    # currency numbers go 1, 2, 3, ...
    # currency indexes go 0, 1, 2, ...

def get_payment(amount_due:int)->int:
    """
    get payment and return the amount paid.
    
    when the payment was greater than the amount due,
    the remaining balance will be negative and the customer
    is entitled to a refund in the amount of the overage.
    """
    # print out the amount due for the ticket

    # show the currency values

    # get input
    # put a small delay in after input
    # catch exceptions
    # test for out of bounds ticket numbers
    # return the currency index, not the currency number

def give_customer_ticket(ticket:int):
    """
    after customer has paid for ticket, give them the ticket
    """
    # print out a message containing the ticket name 

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
    # print out thankyou message

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