#Database schema
#Items: Name, Tags
#Settlements: Name, x, y, dict<pop_type, population>

#Pop types: Name, consumption per month. (peasant, 1 food; noble, 1 art)
#New Item Production: Settlement name, item, increase per month
#Caravans: Name, load, location, origin, destination, base_cost (cost to make and form a caravan regardless of distance)

from Scripts.model import Settlement

def main():
    #settlements: shows all settlements
        #settlements -v: Shows all settlements, the items they have, and the price of those items, and their population of each type.
    #item <item name>: Shows all settlements with this item, its price at those settlements, sorted by price
    pass
def anaylze_market():
    #foreach settlement 
        #foreach good in settlement
            #Does any other settlement have this more expensively than I do?
                #No: Continue
                #Yes: Have we already identified this settlement as a destination?
                    #Yes: Add this good to the existing caravan
                    #No: Make a new caravan
        #Calculate profit. 
            # If caravan cost (base cost+distance) < Profit
                    # form_caravan(origin, destination, item)
                    #add to Caravan table
            #else, continue
    pass
def distance_calculator(origin, destination):
    distance = origin-destination
    #distance formula
    return distance
    pass

def form_caravan(origin, destination, item):
    pass