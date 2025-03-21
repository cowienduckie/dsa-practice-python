from collections import defaultdict
from typing import Dict, List, Set


class Solution:
    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:
        # Use dictionary to store all recipes and ingredients(recipes with no other ingredient)
        cook_book = defaultdict(list)

        # Add all recipes with ingredients
        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                cook_book[recipe].append(ingredient)

        # Add all ingredients
        for ingredient in supplies:
            if ingredient not in cook_book:
                cook_book[ingredient] = []

        # Check all recipes can be cooked
        return [
            recipe for recipe in recipes if self._can_cook(recipe, set(), cook_book)
        ]

    def _can_cook(
        self, recipe: str, visited: Set[str], cook_book: Dict[str, List[str]]
    ) -> bool:
        # Base cases: recipe is not available in cook book or already visited
        if recipe not in cook_book or recipe in visited:
            return False

        # Mark recipe as visited
        visited.add(recipe)

        for ingredient in cook_book[recipe]:
            # Early return if any ingredient cant be cooked
            if not self._can_cook(ingredient, visited, cook_book):
                return False

        # Unmark recipe as visited for backtracking
        visited.remove(recipe)
        return True
