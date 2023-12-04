import pandas
import numpy
from scipy import optimize
import yaml

from item import Items
from recipe import Recipes
from building import Buildings

# I'm looking to make an optimized set of recipies for PPM without creating
# any waste. So I've added two ways to manage this. You can now disable any
# recipe you don't want to use, and you can also set any item to be unsinkable.
# This will make sure that the item is always 0 in the solution (i.e. no excess,
# the item must be produced as much as it is consumed by recipes).
disable_recipes = []
disable_items = []
unsinkable_items = []

# ------------------------------------------------------------------------------
# Populate the A matrix, c vector, and b_ub vector

# Each row of the A matrix represents a recipe. Each column represents an item.
# Inputs of a recipe are represented by a positive value, outputs are 
# represented by a negative value. The value is the amount of the item used or 
# produced per minute.
A_ub = pandas.DataFrame(columns = ['RECIPE'] + list(Items.keys()))

# The c vector represents the sink value of each recipe. This is the objective
# function.
c = numpy.array([])

# The b_ub vector represents the limit of each item. This is the upper bound.
# You can think of this as how many of each item you have available to use.
# Since resource nodes, resource wells, etc are considered items, this is used
# to represent the limit of each of those (how many are in the world).
# All other items have an upper bound of 0.
b_ub = numpy.array([])

# build the A matrix and c vector
for key, recipe in Recipes.items():
    
    if key in disable_recipes:
        continue

    row = {
        'RECIPE': key
    }
    sink_value = 0

    # turn MJ/sec into MJ/min
    row['POWER'] = 60 * Buildings[recipe.building].power

    for input in recipe.input:
        amount_per_min = (60 / recipe.crafting_time) * input.amount
        row[input.item] = amount_per_min
        sink_value -= amount_per_min * Items[input.item].sink_value
    
    for output in recipe.output:
        amount_per_min = (60 / recipe.crafting_time) * output.amount
        row[output.item] = -amount_per_min
        sink_value += amount_per_min * Items[output.item].sink_value

    A_ub = A_ub.append(row, ignore_index = True)
    c = numpy.append(c, sink_value)

A_ub = A_ub.fillna(0)
A_ub = A_ub.set_index('RECIPE')

# remove disabled items
A_ub = A_ub.drop(columns = disable_items)

# build the b_ub vector
for item in list(A_ub.columns):
   b_ub = numpy.append( b_ub, Items[item].limit)

# Currently each column is an ingredient and each row is a recipe.
# We want our objective function to be in terms of the recipes, so we
# need to transpose the matrix.
A_ub = A_ub.transpose()
A_ub = A_ub.rename_axis('ITEM')

# This will make sure that the items that are unsinkable are always 0.
A_eq = A_ub.loc[A_ub.index.isin(unsinkable_items)]
b_eq = numpy.zeros(len(A_eq.index))

# ------------------------------------------------------------------------------
# Solve the linear program

# Solve the linear program - this will minimize the objective function, so we
# need to negate the c vector to maximize the objective function instead.
analysis = optimize.linprog(
    c = -c,
    A_ub = A_ub.values,
    b_ub = b_ub,
    A_eq = A_eq.values,
    b_eq = b_eq,
)

# ------------------------------------------------------------------------------
# Output the results

coefficients =  numpy.around(analysis.x, 2).tolist()
all_recipes = {k:v for k, v in zip(list(A_ub.columns), coefficients)}

# ignore recipes that are not used
used_recipes = {k:v for k, v in all_recipes.items() if v > 0}

excess_power = 0
for key, value in used_recipes.items():
    recipe = Recipes[key]
    excess_power += Buildings[recipe.building].power * value

total_buildings = sum(used_recipes.values())

summary = {
    "ppm": round(-analysis.fun, 2),
    "total_buildings": round(total_buildings, 2),
    "excess_power": round(excess_power, 2),
    "recipes": used_recipes
}

with open('summary.yaml', 'w') as file:
    yaml.dump(summary, file, sort_keys=False)
