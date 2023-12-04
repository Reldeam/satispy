import yaml
import os 

from optimize import solve
  
if not os.path.exists("results"):
    os.makedirs("results")

# Creates a standard optimization with no constraints.
summary = solve()

with open('results/summary.yaml', 'w') as file:
    yaml.dump(summary, file, sort_keys=False)

# I'm looking to make an optimized set of recipies for PPM without creating
# any waste. So I've added two ways to manage this. You can now disable any
# recipe you don't want to use, and you can also set any item to be unsinkable.
# This will make sure that the item is always 0 in the solution (i.e. no excess,
# the item must be produced as much as it is consumed by recipes).
summary = solve(
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

with open('results/eco-summary.yaml', 'w') as file:
    yaml.dump(summary, file, sort_keys=False)
