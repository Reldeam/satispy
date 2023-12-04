import yaml
import os 

from optimize import optimize_points, optimize_power, optimize_item
  
if not os.path.exists("results"):
    os.makedirs("results")
    
def create_summary(name : str, summary : dict):
    with open('results/' + name + '-summary.yaml', 'w') as file:
        yaml.dump(summary, file, sort_keys=False)

# ------------------------------------------------------------------------------
# Creates a standard optimization with no constraints.
summary = optimize_points()
create_summary('points', summary)

# ------------------------------------------------------------------------------
# I'm looking to make an optimized set of recipies for PPM without creating
# any waste. So I've added two ways to manage this. You can now disable any
# recipe you don't want to use, and you can also set any item to be unsinkable.
# This will make sure that the item is always 0 in the solution (i.e. no excess,
# the item must be produced as much as it is consumed by recipes).
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
# Optimize for the most efficient way to produce power.

summary = optimize_power()
create_summary('power', summary)

# ------------------------------------------------------------------------------
# Optimize for making the most Thermal Propulsion Rockets per minute.

summary = optimize_item('THERMAL_PROPULSION_ROCKET')
create_summary('thermal-propulsion-rocket', summary)