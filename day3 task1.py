prices = [120, 450, 300, 80, 950, 210, 600, 150, 400, 720]

avg_price = sum(prices) / len(prices)
above_avg = [p for p in prices if p > avg_price]

print("Average Price:", avg_price)
print("Prices above average:", above_avg)