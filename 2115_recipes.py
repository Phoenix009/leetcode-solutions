def solve(recipes, ingredients, supplies):
    def helper(recipe, recipes, supplies, notsupplies, inprogress):
        for ingre in recipes[recipe]:
            if ingre in supplies:
                continue
            if ingre in inprogress:
                return False
            if ingre not in recipes:
                return False
            if ingre in notsupplies:
                return False

            inprogress.add(ingre)
            if helper(ingre, recipes, supplies, notsupplies, inprogress):
                supplies.add(ingre)
                inprogress.remove(ingre)
            else:
                notsupplies.add(ingre)
                inprogress.remove(ingre)
                return False
        return True

    recipes = dict(zip(recipes, ingredients))
    supplies = set(supplies)
    notsupplies = set()
    inprogress = set()
    ans = []
    for recipe in recipes.keys():
        inprogress.add(recipe)
        if helper(recipe, recipes, supplies, notsupplies, inprogress):
            supplies.add(recipe)
            ans.append(recipe)
        else:
            notsupplies.add(recipe)
        inprogress.remove(recipe)
    return ans


print(solve(
    ["bread"],
    [["yeast", "flour"]],
    ["yeast", "flour", "corn"]
))

print(solve(
    ["bread", "sandwich"],
    [["yeast", "flour"], ["bread", "meat"]],
    ["yeast", "flour", "meat"]
))

print(solve(
    ["bread", "sandwich", "burger"],
    [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]],
    ["yeast", "flour", "meat"]
))

print(solve(
    ['A', 'B'],
    [['A'], ['B']],
    []
))
