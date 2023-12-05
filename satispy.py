import yaml
import os 

from optimize import optimize_points, optimize_power, optimize_item
  
if not os.path.exists("results"):
    os.makedirs("results")
    
def create_summary(name : str, summary : dict):
    with open('results/' + name + '.yaml', 'w') as file:
        yaml.dump(summary, file, sort_keys=False)

# The following are some examples of how to use the optimize functions.

# ------------------------------------------------------------------------------
# Creates a standard optimization with no constraints.
summary = optimize_points()
create_summary('points', summary)

# ------------------------------------------------------------------------------
# Optimize for the most efficient way to produce power.

summary = optimize_power()
create_summary('power', summary)

# ------------------------------------------------------------------------------
# Optimize for making the most Thermal Propulsion Rockets per minute.

summary = optimize_item('THERMAL_PROPULSION_ROCKET')
create_summary('thermal-propulsion-rocket', summary)

# ------------------------------------------------------------------------------
# Optimize for making the most points without creating unsinkable waste

summary = optimize_points(
    disable_recipes = ['PLUTONIUM_POWER'],
    disable_items = [],
    unsinkable_items = [
        
        'WATER',
        'CRUDE_OIL',
        'HEAVY_OIL_RESIDUE',
        'FUEL',
        'TURBOFUEL',
        'ALUMINA_SOLUTION',
        'SULFURIC_ACID',
        'NITRIC_ACID',
        'NITROGEN_GAS',
        
        'URANIUM_WASTE', 
        'PLUTONIUM_WASTE',
        'NON_FISSILE_URANIUM',
        'PLUTONIUM_PELLET',
        'ENCASED_PLUTONIUM_CELL',
        
    ]
)
create_summary('sustainable-points', summary)

# ------------------------------------------------------------------------------
# For my own map, I'm looking to make an optimized set of recipies for PPM 
# without creating any waste. I also need some spare power for trains and 
# batteries for drones so that the map is fun (there will be lots of plutonium
# fuel rods avaiable for trucks by vertue of not using them for power and
# preventing any excess uranium waste).

summary = optimize_points(
    disable_recipes = ['PLUTONIUM_POWER'],
    disable_items = [],
    unsinkable_items = [
        
        'WATER',
        'CRUDE_OIL',
        'HEAVY_OIL_RESIDUE',
        'FUEL',
        'TURBOFUEL',
        'ALUMINA_SOLUTION',
        'SULFURIC_ACID',
        'NITRIC_ACID',
        'NITROGEN_GAS',
        
        'URANIUM_WASTE', 
        'PLUTONIUM_WASTE',
        'NON_FISSILE_URANIUM',
        'PLUTONIUM_PELLET',
        'ENCASED_PLUTONIUM_CELL',
        
    ],
    ingredient_bounds = {
        "POWER": (60 * 2000, None), # for trains
        "BATTERY": (500, None) # for drones
    }
)
create_summary('custom', summary)