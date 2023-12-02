import pandas
import numpy
from scipy import optimize
import yaml

from item import Items
from recipe import Recipes
from building import Buildings

# ------------------------------------------------------------------------------
# Populate the A matrix, c vector, and b_ub vector

# Each row of the A matrix represents a recipe. Each column represents an item.
# Inputs of a recipe are represented by a positive value, outputs are 
# represented by a negative value. The value is the amount of the item used or 
# produced per minute.
A = pandas.DataFrame(columns = ['RECIPE'] + list(Items.keys()))

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

    row = {
        'RECIPE': key
    }
    sink_value = 0

    # turn MJ/sec into MJ/min
    row['POWER'] = 60 * Buildings[recipe.building].power

    for ingredient in recipe.ingredients:
        row[ingredient.item] = ingredient.amount
        sink_value -= ingredient.amount * Items[ingredient.item].sink_value
    
    for result in recipe.result:
        row[result.item] = -result.amount
        sink_value += result.amount * Items[result.item].sink_value

    A = A.append(row, ignore_index = True)
    c = numpy.append(c, sink_value)

A = A.fillna(0)
A = A.set_index('RECIPE')

# build the b_ub vector
for item in list(A.columns):
   b_ub = numpy.append( b_ub, Items[item].limit)

# Currently each column is an ingredient and each row is a recipe.
# We want our objective function to be in terms of the recipes, so we
# need to transpose the matrix.
A = A.transpose()
A = A.rename_axis('ITEM')

# ------------------------------------------------------------------------------
# Solve the linear program

# Solve the linear program - this will minimize the objective function, so we
# need to negate the c vector to maximize the objective function instead.
analysis = optimize.linprog(
    c = -c,
    A_ub = A.values,
    b_ub = b_ub
)

# ------------------------------------------------------------------------------
# Output the results

coefficients =  numpy.around(analysis.x, 2).tolist()
all_recipes = {k:v for k, v in zip(list(A.columns), coefficients)}

# ignore recipes that are not used
used_recipes = {k:v for k, v in all_recipes.items() if v > 0}

summary = {
    "ppm": round(-analysis.fun, 2),
    "recipes": used_recipes
}

with open('summary.yaml', 'w') as file:
    yaml.dump(summary, file, sort_keys=False)
