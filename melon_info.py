"""Print out all the melons in our inventory."""

# getting all the melons organized in a dictionary

melons = {
    'Honeydew' :  {'seedlessness': 'do not have', 'price' : 0.99, 'flesh color': 'yellow',
    'rind color': 'ripe', 'average weight': 2}, 
    'Crenshaw' :  {'seedlessness': 'have', 'price' : 2.00, 'flesh color': 'orange',
    'rind color': 'green', 'average weight': 2},
    'Crane'    :  {'seedlessness': 'have', 'price' : 2.50, 'flesh color': 'green', 
    'rind color': 'white', 'average weight': 1},
    'Casaba'   :  {'seedlessness': 'have', 'price' : 2.50, 'flesh color': 'green',
    'rind color': 'green', 'average weight': 2},
    'Cantaloupe': {'seedlessness': 'have', 'price' : 0.99, 'flesh color': 'orange',
    'rind color': 'orange', 'average weight': 2},
}
sorted(melons)

melons['define local': ' ']
# from melons import melon_names, melon_seedlessness, melon_prices


def print_melon(name, seedless, price):
    """Print each melon with corresponding attribute information."""
    for melon in melons.items():
    print(melon '{name}: {seedlessness}: {price}')
    
#for unit melon in melons dictionary, respond have or do not have seeds
# then print melon name, seedlessness, price


def melons_with_i(names, seedlessness, price):

    melons_with_i = {}

    for melon in melons:
    return melons_with_i.get(letter, i)

melons_i = melons_with_i(names, seedlessness, price)
        

