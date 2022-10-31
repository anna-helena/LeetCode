from collections import defaultdict
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        recs = {}
        for idx,recipe in enumerate(recipes):
            recs[recipe] = idx
        solution = []
        seen = {}
        def helper_(idx):
            if recipes[idx] in seen:
                if seen[recipes[idx]]:
                    return True
                else:
                    return False
            for ingredient in ingredients[idx]:
                    if ingredient not in supplies:
                        if ingredient in recs:
                            seen[recipes[idx]] = False
                            if not helper_(recs[ingredient]):
                                return False
                        else:
                            seen[recipes[idx]] = False
                            return False
            seen[recipes[idx]] = True
            supplies.add(recipes[idx])
            return True
    
        for idx,recipe in enumerate(recipes):
            if helper_(idx):
                solution.append(recipe)
        return solution
    