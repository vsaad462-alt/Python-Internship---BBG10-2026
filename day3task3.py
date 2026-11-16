# 1. Dictionary comprehension for products priced above 100
products = {
    "Pen": 25,
    "Notebook": 120,
    "Mouse": 450,
    "Eraser": 15,
    "Keyboard": 850,
    "Water Bottle": 180
}
expensive_products = {item: price for item, price in products.items() if price > 100}
print("1. Products above 100:", expensive_products)

# 2. Find student with highest marks without using max() directly
students = [
    {"name": "Riya", "marks": 88},
    {"name": "Aman", "marks": 95},
    {"name": "Sara", "marks": 79},
    {"name": "Kabir", "marks": 91}
]
topper = students[0]
for s in students:
    if s["marks"] > topper["marks"]:
        topper = s
print(f"2. Topper: {topper['name']} with {topper['marks']} marks")

# 3. Nested dictionary for a small library & issuing a book
library = {
    "B101": {"title": "Python Crash Course", "author": "Eric Matthes", "copies": 4},
    "B102": {"title": "Clean Code", "author": "Robert Martin", "copies": 2},
    "B103": {"title": "Automate the Boring Stuff", "author": "Al Sweigart", "copies": 5}
}
# Issue book B102 (reduce available copies by 1)
library["B102"]["copies"] -= 1
print("3. Updated Library after issuing B102:", library["B102"])

# 4. Group words by their first letter using setdefault()
words = ["apple", "ant", "banana", "bat", "cat", "carrot"]
grouped_words = {}
for word in words:
    first_letter = word[0]
    grouped_words.setdefault(first_letter, []).append(word)
print("4. Grouped words:", grouped_words)

# 5. Merge default settings and user settings (user overrides default)
default_settings = {"theme": "light", "notifications": True, "font_size": 12, "language": "English"}
user_settings = {"theme": "dark", "font_size": 16}

final_settings = default_settings | user_settings
print("5. Combined Settings:", final_settings)

# 6. Sort employees by salary descending and print top 3
employees = {
    "Riya": 45000,
    "Aman": 72000,
    "Sara": 58000,
    "Kabir": 85000,
    "Zoya": 64000
}
sorted_employees = sorted(employees.items(), key=lambda x: x[1], reverse=True)
top_3 = dict(sorted_employees[:3])
print("6. Top 3 highest paid employees:", top_3)

# 7. Small Inventory System
inventory = {"Laptop": 10, "Mouse": 25, "Keyboard": 15}

def add_stock(item, qty):
    inventory[item] = inventory.get(item, 0) + qty
    print(f"   Added {qty} {item}(s). Current stock: {inventory[item]}")

def sell_item(item, qty):
    if item not in inventory:
        print(f"   Error: '{item}' does not exist in inventory!")
    elif inventory[item] < qty:
        print(f"   Error: Not enough stock for '{item}'. Available: {inventory[item]}")
    else:
        inventory[item] -= qty
        print(f"   Sold {qty} {item}(s). Remaining stock: {inventory[item]}")

print("7. Inventory System:")
add_stock("Mouse", 5)
sell_item("Laptop", 3)
sell_item("Tablet", 2)  # Product that does not exist
print("   Final Inventory:", inventory)