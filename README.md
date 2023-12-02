# SATISPY - Factory Game Production Optimiser

This is just a small tool to find the most Awesome Sink Points you can make
per minute. The objective function is set to the points you get for each
recipe, but this can be set to anything, so in the future I might add updates
to maximise the output of specific recipes instead of points. 

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

Run `py optimize.py` to output a **summary.yaml** that contains the quantities of each recipe needed.

While all of the recipes and alternative recipes in the game have been added,
some may be found to have zero use when trying to maximise the objective function.
All recipes that are not used will be exluded from the **summary.yaml** to help
with readability (i.e. if a recipe is not present in the **summary.yaml** then
you can assume that its value was zero). 

## Currently out of Scope
This tool does not work out how to connect all of these recipies together, but that can be reverse engineered from the summary.