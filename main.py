import os
from recipe import *

def main():
    recipe_paths = get_recipe_paths()
    recipes = get_recipes_from_paths(recipe_paths)
    for recipe in recipes:
        print("{name}: {link}".format(name=recipe.name, link=recipe.link))

def get_recipe_paths(directory="recipes"):
    filepaths = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            filepaths.append(filepath)
    
    return filepaths

def get_recipes_from_paths(filepaths):
    recipes = []
    for filepath in filepaths:
        recipes.append(Recipe(filepath))
    
    return recipes

if __name__ == "__main__":
   main()