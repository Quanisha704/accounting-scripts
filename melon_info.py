"""Print out all the melons in our inventory."""


from melons import melon_names, melon_seedlessness, melon_prices,melon_flesh_color, melon_rind_color, melon_weight


def print_melon(name, seedless, price, flesh_color = None, rind_color = None, weight = None):
    """Print each melon with corresponding attribute information."""

    have_or_have_not = 'have'
    if seedless:
        have_or_have_not = 'do not have'
    
    
    print(f'{name}\nSeedless:{seedless}\nPrice:{price}\nflesh_color:{flesh_color}\nweight:{weight}\nrind_color:{rind_color}')    
    #print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


for i in melon_names:
    print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i], 
                melon_flesh_color[i], melon_rind_color[i], melon_weight[i])
