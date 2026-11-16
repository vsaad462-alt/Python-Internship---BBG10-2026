# 1. Function returning (lowest, highest, average) tuple and unpacking it
def analyze_marks(marks):
    lowest = min(marks)
    highest = max(marks)
    average = round(sum(marks) / len(marks), 2)
    return (lowest, highest, average)

student_marks = [78, 92, 65, 88, 95, 71]
low, high, avg = analyze_marks(student_marks)
print(f"1. Lowest: {low}, Highest: {high}, Average: {avg}")

# 2. Product tuple immutability and creating an updated tuple
product = ("Laptop", 55000, 10)
 #product[1] = 52000  # This causes TypeError: 'tuple' object does not support item assignment
updated_product = (product[0], 52000, product[2])
print("2. Updated Product:", updated_product)

# 3. Unpacking (latitude, longitude) tuples inside a loop
locations = [(12.9, 77.5), (19.0, 72.8), (22.5, 72.9)]
print("3. Visited Locations:")
for lat, lon in locations:
    print(f"   Latitude: {lat}, Longitude: {lon}")
    
# 4. Set differences between newsletter subscribers and purchasers
subscribers = {"riya@gmail.com", "aman@gmail.com", "sara@gmail.com", "kabir@gmail.com"}
purchasers = {"aman@gmail.com", "kabir@gmail.com", "zoya@gmail.com"}

never_purchased = subscribers.difference(purchasers)
never_subscribed = purchasers.difference(subscribers)
print("4. Subscribed but never purchased:", never_purchased)
print("   Purchased but never subscribed:", never_subscribed)

# 5. Find unique website visitors and their count using a set
visitor_ids = [101, 102, 101, 105, 103, 102, 104, 105, 106, 101]
unique_visitors = set(visitor_ids)
print("5. Unique visitors:", unique_visitors, "| Count:", len(unique_visitors))

# 6. Simple role-based permission check using sets
admin_permissions = {"read", "write", "delete", "manage_users"}
editor_permissions = {"read", "write"}

user_permissions = editor_permissions
required_action = "delete"

can_perform = required_action in user_permissions and required_action in admin_permissions
print("6. Can editor perform admin action ('delete')?:", can_perform)

# 7. Function returning a frozenset from a list
def to_frozenset(items):
    return frozenset(items)

# A frozenset is immutable and hashable, which is required for any object to be used as a dictionary key.
sample_list = ["python", "sql", "git", "python"]
frozen_result = to_frozenset(sample_list)
print("7. Frozenset result:", frozen_result)