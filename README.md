# SATISPY - Factory Game Production Optimiser

This is just a small tool to find the most Awesome Sink Points you can make
per minute. The objective function is set to the points you get for each
recipe, but this can be set to anything, so in the future I might add updates
to maximise the output of specific recipes instead of points. 

If you are just interested in the current results, I've added the 
[summary.yaml](https://github.com/Reldeam/satispy/blob/main/summary.yaml) to the 
repo, which I will keep updated.

## Assumptions

- All miners, extractors, and pressurizers are overclocked at 250%.
- All other production buildings are clocked at 100% (no underclocking).
- Pure resource node extraction is capped at Mk5. conveyer belt speed 
(780 items per minute).
- The energy cost of resource wells is calculated as the energy cost of the 
pressurizer divided amoung all of it's wells evenly. This will only be
innacurate if not all of the wells are utilized.

## Requirements

- This is a python project.
- I've added a **requirements.txt** to help set up your python environment.

## Run

Run `py optimize.py` to output a 
[summary.yaml](https://github.com/Reldeam/satispy/blob/main/summary.yaml) that 
contains the quantities of each recipe needed.

There are two variables at the start of **optimize.py**:
```python
disable_recipes = ['PLUTONIUM_POWER']
disable_items = ['POWER']
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
```

- `disable_recipes` is a list of recipes that will not be used. Set this to
an empty list `[]` if you want to use all of the recipes.
- `disable_items` is a list of items that are ignored in all recipes for both
inputs and outputs.
- `unsinkable_items` is a list of items that cannot be produced at an excess,
i.e. URANIUM_WASTE can be produced, but all of the produced URANIUM_WASTE must
be used up by other recipes. This is useful if you want to have a "sustainable"
world where no excess waste is produced that can't be sunk. If you don't care
about the environment you can just set this variable to an empty list `[]`.

While all of the recipes and alternative recipes in the game have been added,
some may be found to have zero use when trying to maximise the objective function.
All recipes that are not used will be exluded from the 
[summary.yaml](https://github.com/Reldeam/satispy/blob/main/summary.yaml) to help
with readability (i.e. if a recipe is not present in the 
[summary.yaml](https://github.com/Reldeam/satispy/blob/main/summary.yaml) then
you can assume that its value was zero). 

## Currently out of Scope
This tool does not work out how to connect all of these recipies together, but 
that can be reverse engineered from the summary.