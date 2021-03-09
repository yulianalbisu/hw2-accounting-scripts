"""Print out all the melons in our inventory."""
melon_total = {
    'Honeydew' :  {'seedlessness': 'True', 'price' : 0.99, 
    'Crenshaw' :  {'seedlessness': 'False', 'price' : 2.00,}
    'Crane'    :  {'seedlessness': 'False', 'price' : 2.50,}
    'Casaba'   :  {'seedlessness': 'False', 'price' : 2.50,}
    'Cantaloupe': {'seedlessness': 'False', 'price' : 0.99, }
}

from melons import melon_names, melon_seedlessness, melon_prices


def print_melon(name, seedless, price):
    """Print each melon with corresponding attribute information."""

    have_or_have_not = 'have'
    if seedless:
        have_or_have_not = 'do not have'

    print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


for i in melon_names:
    print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])
