import json

class Recipe:
    def __init__(self, recipe_path):
        recipe_dict = self.load_recipe(recipe_path)
        self.name = recipe_dict["name"]
        self.link = recipe_dict["link"]
        self.ingredients = recipe_dict["ingredients"]

    def load_recipe(self, recipe_path):
        with open(recipe_path) as json_file:
            return json.load(json_file)