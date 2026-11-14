price_per_notebook = 45
budget = 500
quantity = 7

total_cost = price_per_notebook * quantity
maximum_notebooks = budget // price_per_notebook
money_left = budget % price_per_notebook

print("total cost:", total_cost)
print("notebooks purchasable:", maximum_notebooks)
print("money left:", money_left)

