import pandas
import numpy
from scipy import optimize
import yaml

from item import Items
from recipe import Recipes
from building import Buildings

A = pandas.DataFrame(columns = ['RECIPE'] + list(Items.keys()))
c = numpy.array([])

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
b_ub = numpy.array([])
for item in list(A.columns):
   b_ub = numpy.append( b_ub, Items[item].limit)

A = A.transpose()
A = A.rename_axis('ITEM')

analysis = optimize.linprog(
    c = -c,
    A_ub = A.values,
    b_ub = b_ub
)

coefficients =  numpy.around(analysis.x, 2).tolist()
result = {k:v for k, v in zip(list(A.columns), coefficients)}
used_recipes = {k:v for k, v in result.items() if v > 0}

summary = {
    "ppm": round(-analysis.fun, 2),
    "recipes": used_recipes
}

print(summary)

with open('summary.yaml', 'w') as file:
    yaml.dump(summary, file, sort_keys=False)
