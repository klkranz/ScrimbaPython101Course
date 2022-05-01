sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
sales_w2.append(int(input("Provide the final sales amount for week 2: ")))
sales.extend(sales_w1)
sales.extend(sales_w2)
# cleaner method is sales = sales_wk1 + sales_wk2 because it is easier to put together more than two lists.
# print(sales)
profit_wk1 = sum(sales_w1) * 1.5
best_wk1 = max(sales_w1) * 1.5
worst_wk1 = min(sales_w1) * 1.5
profit_wk2 = sum(sales_w2) * 1.5
best_wk2 = max(sales_w2) * 1.5
worst_wk2 = min(sales_w2) * 1.5
profit_all = sum(sales) * 1.5
profit_best = max(sales) * 1.5
profit_worst = min(sales) * 1.5
print(f"For Week 1 the best day profits were ${best_wk1}, and the worst day profits were ${worst_wk1},")
print(f"for an over all weekly profit of ${profit_wk1}.")
print(f"For Week 2 the best day profits were ${best_wk2}, and the worst day profits were ${worst_wk2},")
print(f"for an over all weekly profit of ${profit_wk2}.")
print(f"The overall best day profits were ${profit_best}, and the overall worst day profits were ${profit_worst}.")
print(f"That brings the total earned both weeks to ${profit_all}.")