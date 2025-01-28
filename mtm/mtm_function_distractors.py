# Parson's Problem with Distractors
#
# Rearrange the lines of code making sure each line of code has the proper indentation level.
# Remove any lines that shouldn't be there.
# Test your solution in the REPL or add test code at the end.

CURRENCY_VALUES = [1, 5, 10, 20]

def give_refund(refund_due:int)->int:
    """
    Give a partial refund.
    Choose the largest bill possible without going over the refund value
    Return the amount left to refund.
    """

    currency_values = CURRENCY_VALUES.sort(reverse=True)
    print(f"You are refunded ${currency_value}")
    for currency_value in  currency_values:
    currency_values = CURRENCY_VALUES.sort()
    currency_values = sorted(CURRENCY_VALUES, reverse=True)
    if refund_due >= currency_value:
    # sort the currency values where biggest is first, smallest last
    return refund_due - currency_value
    currency_values = sorted(CURRENCY_VALUES)
