import random

original_prices = [random.randint(-10, 10) for _ in range(5)]
new_prices = [(x if x > 0 else 0) for x in original_prices]
print(original_prices)
print("Мы потеряли: ",  abs(sum(original_prices) - sum(new_prices)))
