import json

# Read File
with open('input.json', 'r') as file:
    # Parse Json
    data = json.load(file)

# Calculating average calories for non-homemade purchased food
purchased_foods = [
    entry for entry in data if entry['procedence'] == 'purchased' and entry['type'] != 'homemade'
]
average_calories = sum(item['calories'] for item in purchased_foods) / len(purchased_foods)

# Listing favroite dishes under 1000 calories
favorite_dishes = [
    entry for entry in data if entry['favorite'].lower() == 'true' and entry['calories'] < 1000
]
sorted_favorite_dishes = sorted(favorite_dishes, key=lambda x: x['calories'], reverse=True)[:3]

# Finding 3 meals with highest protien to cost ratio
meals_protien_to_cost = [{
    **entry,
    'protien_to_cost_ratio': entry['protein'] / entry['price']} for entry in data
]
sorted_meals_protien_to_cost = sorted(
    meals_protien_to_cost,
    key=lambda x: x['protien_to_cost_ratio'],
    reverse=True
)[:3]

# Displaying out the results
# 3
print(f'Average Calories: {average_calories:.2f}')

#4
print('Top 3 favorite dishes under 1000 calories:')
for dish in sorted_favorite_dishes:
    print(f"{dish['name']} {dish['date_consumed']} {dish['calories']}")

# 5
print('Top 3 Meals with Highest Protien to Cost Ratio')
for meal in sorted_meals_protien_to_cost:
    print(f"{meal['name']} - {meal['protien_to_cost_ratio']}")