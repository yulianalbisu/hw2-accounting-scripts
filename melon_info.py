"""Print out all the melons in our inventory."""

# getting all the melons organized in a dictionary

melons = {
    'Honeydew' :  {'seedlessness': 'do not have', 'price' : 0.99}, 
    'Crenshaw' :  {'seedlessness': 'have', 'price' : 2.00},
    'Crane'    :  {'seedlessness': 'have', 'price' : 2.50},
    'Casaba'   :  {'seedlessness': 'have', 'price' : 2.50},
    'Cantaloupe': {'seedlessness': 'have', 'price' : 0.99},
}

# from melons import melon_names, melon_seedlessness, melon_prices


def print_melon(name, seedless, price):
    """Print each melon with corresponding attribute information."""
    for melon in melons :
        have_or_have_not = melons[sedlessness]
    print("melon '{name}, {have_or_have_not}, {price})
    
#for unit melon in melons dictionary, respond have or do not have seeds
# then print melon name, seedlessness, price


for i in melon_names:
    print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])
