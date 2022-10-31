from collections import defaultdict
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        recs = {}
        for idx,recipe in enumerate(recipes):
            recs[recipe] = idx
        solution = []
        seen = {}
        for idx,recipe in enumerate(recipes):
            if self.helper_(idx,recs,recipes,ingredients,supplies,seen):
                solution.append(recipe)
        return solution
    
    def helper_(self,idx,recs,recipes,ingredients,supplies,seen):
        if recipes[idx] in seen:
            if seen[recipes[idx]]:
                return True
            else:
                return False
        for ingredient in ingredients[idx]:
                if ingredient not in supplies:
                    if ingredient in recs:
                        seen[recipes[idx]] = False
                        if not self.helper_(recs[ingredient],recs,recipes,ingredients,supplies,seen):
                            return False
                    else:
                        seen[recipes[idx]] = False
                        return False
        seen[recipes[idx]] = True
        supplies.add(recipes[idx])
        return True